# Copyright 2017 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import hashlib
import io
import logging
import os
import random
import re

import contextlib2
from lxml import etree
import numpy as np
import PIL.Image
import tensorflow as tf

from object_detection.dataset_tools import tf_record_creation_util
from object_detection.utils import dataset_util
from object_detection.utils import label_map_util

data_dir = os.getcwd()
output_dir = os.getcwd() + '/tf_record/'

# Train/val ratio
ratio = 0.9

def get_class_name_from_filename(file_name):
    """Gets the class name from a file.

    Args:
      file_name: The file name to get the class name from.
                 ie. "american_pit_bull_terrier_105.jpg"

    Returns:
      A string of the class name.
    """
    match = re.match(r'([A-Za-z_]+)(_[0-9]+\.jpg)', file_name, re.I)
    return match.groups()[0]


def dict_to_tf_example(data,
                       label_map_dict,
                       image_subdirectory,
                       ignore_difficult_instances=False):
    """Convert XML derived dict to tf.Example proto.

    Notice that this function normalizes the bounding box coordinates provided
    by the raw data.

    Args:
      data: dict holding PASCAL XML fields for a single image (obtained by
        running dataset_util.recursive_parse_xml_to_dict)
      label_map_dict: A map from string label names to integers ids.
      image_subdirectory: String specifying subdirectory within the
        Pascal dataset directory holding the actual image data.
      ignore_difficult_instances: Whether to skip difficult instances in the
        dataset  (default: False).

    Returns:
      example: The converted tf.Example.

    Raises:
      ValueError: if the image pointed to by data['filename'] is not a valid JPEG
    """

    img_path = os.path.join(image_subdirectory, data['filename'])

    with tf.gfile.GFile(img_path, 'rb') as fid:
        encoded_jpg = fid.read()
    encoded_jpg_io = io.BytesIO(encoded_jpg)
    image = PIL.Image.open(encoded_jpg_io)
    if image.format != 'JPEG':
        raise ValueError('Image format not JPEG')
    key = hashlib.sha256(encoded_jpg).hexdigest()

    width = int(data['size']['width'])
    height = int(data['size']['height'])

    xmin = []
    ymin = []
    xmax = []
    ymax = []
    classes = []
    classes_text = []
    truncated = []
    poses = []
    difficult_obj = []

    try:
        for obj in data['object']:
            difficult = bool(int(obj['difficult']))
            if ignore_difficult_instances and difficult:
                continue
            difficult_obj.append(int(difficult))
            xmin.append(float(obj['bndbox']['xmin']) / width)
            ymin.append(float(obj['bndbox']['ymin']) / height)
            xmax.append(float(obj['bndbox']['xmax']) / width)
            ymax.append(float(obj['bndbox']['ymax']) / height)
            classes_text.append(obj['name'].encode('utf8'))
            classes.append(label_map_dict[obj['name']])
            truncated.append(int(obj['truncated']))
            poses.append(obj['pose'].encode('utf8'))
    except:
        print('no object in %s' % data['filename'])

    example = tf.train.Example(features=tf.train.Features(feature={
        'image/height': dataset_util.int64_feature(height),
        'image/width': dataset_util.int64_feature(width),
        'image/filename': dataset_util.bytes_feature(
            data['filename'].encode('utf8')),
        'image/source_id': dataset_util.bytes_feature(
            data['filename'].encode('utf8')),
        'image/key/sha256': dataset_util.bytes_feature(key.encode('utf8')),
        'image/encoded': dataset_util.bytes_feature(encoded_jpg),
        'image/format': dataset_util.bytes_feature('jpeg'.encode('utf8')),
        'image/object/bbox/xmin': dataset_util.float_list_feature(xmin),
        'image/object/bbox/xmax': dataset_util.float_list_feature(xmax),
        'image/object/bbox/ymin': dataset_util.float_list_feature(ymin),
        'image/object/bbox/ymax': dataset_util.float_list_feature(ymax),
        'image/object/class/text': dataset_util.bytes_list_feature(classes_text),
        'image/object/class/label': dataset_util.int64_list_feature(classes),
        'image/object/difficult': dataset_util.int64_list_feature(difficult_obj),
        'image/object/truncated': dataset_util.int64_list_feature(truncated),
        'image/object/view': dataset_util.bytes_list_feature(poses),
    }))
    return example


def create_tf_record(output_filename,
                     label_map_dict,
                     annotations_dir,
                     image_dir,
                     examples):
    """
    Creates a TFRecord file from examples.

    Args:
      output_filename: Path to where output file is saved.
      label_map_dict: The label map dictionary.
      annotations_dir: Directory where annotation files are stored.
      image_dir: Directory where image files are stored.
      examples: Examples to parse and save to tf record.
    """

    writer = tf.python_io.TFRecordWriter(output_filename)
    for idx, example in enumerate(examples):
        if idx % 100 != 0:
            logging.info('On image %d of %d', idx, len(examples))
        path = annotations_dir + '/xmls'
        path = os.path.join(path, example+'.xml')

        if not os.path.exists(path):
            logging.warning('Could not find %s, ignoring example.', path)
            continue
        with tf.gfile.GFile(path, 'r') as fid:
            xml_str = fid.read()
            xml = etree.fromstring(xml_str)
        data = dataset_util.recursive_parse_xml_to_dict(xml)['annotation']

        tf_example = dict_to_tf_example(data, label_map_dict, image_dir)
        writer.write(tf_example.SerializeToString())

    writer.close()


# Main
def main(_):

  annotations_dir = os.path.join(data_dir, 'annotations')
  label_map_path = os.path.join(annotations_dir,'label_map.pbtxt')

  logging.info('Reading from dataset.')
  image_dir = os.path.join(data_dir, 'images')

  examples_path = os.path.join(annotations_dir, 'trainval.txt')
  examples_list = dataset_util.read_examples_list(examples_path)

  label_map_dict = label_map_util.get_label_map_dict(label_map_path)

  random.seed(42)
  random.shuffle(examples_list)
  num_examples = len(examples_list)
  num_train = int(ratio * num_examples)
  train_examples = examples_list[:num_train]
  val_examples = examples_list[num_train:]
  logging.info('%d training and %d validation examples.',
               len(train_examples), len(val_examples))

  train_output_path = os.path.join(output_dir, 'train.record')
  val_output_path = os.path.join(output_dir, 'test.record')

  create_tf_record(
      train_output_path,
      label_map_dict,
      annotations_dir,
      image_dir,
      train_examples)

  create_tf_record(
      val_output_path,
      label_map_dict,
      annotations_dir,
      image_dir,
      val_examples)

if __name__ == '__main__':
  tf.app.run()