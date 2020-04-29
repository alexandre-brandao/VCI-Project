# Info
- For 8GB RAM ownership i recommend images up 1280x720. 
- Do consider resizing your image properly otherwise the trainer won't work due to insufficient RAM
- Do keep the files as they are and only edit what must be edited

# Reference Links
### Tensorflow GPU installation guide: https://medium.com/better-programming/install-tensorflow-1-13-on-ubuntu-18-04-with-gpu-support-239b36d29070
### Tensorflow General Reference:  https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/
### Extra: https://gist.github.com/douglasrizzo/c70e186678f126f1b9005ca83d8bd2ce
### LabelImg Installation:  https://github.com/tzutalin/labelImg

# To run a model you must 
1.  Make sure your .jpg(JPEG)
2.  Make sure your images are labeled 1.jpg, 2.pjg, 3.jpg,... and so on
3.  val.txt file must be created with each line consisting of all image numbering, keep the other in check.(sort)
4.  Make sure you the labelImg program and label your boxes accordingly.
5.  Copy all the XML files to the annotations/xmls folder
6.  Run "python3 create_tf_record.py" on the command line
7.  Create/get the appropriate .config and edit the .config file of the next line accordingly
8.  Run "python3 train.py --logtostderr --train_dir=%ABSOLUTE_PATH%/training/ -- --pipeline_config_path%ABSOLUTE_PATH%/training/faster_rcnn_inception_v2_coco.config  ...This is a mere example
9.  Once you think it's trained you may cancel anytime halfway
10. Run "python3 export_inference_graph.py --input_type=tensor_image --pipeline_config_path=training/*.config --trained_checkpoint_prefix=training/model.cpkt-#### --output_directory=inference_graph/"
11. Run "python3 objectdetection_v2.py"




