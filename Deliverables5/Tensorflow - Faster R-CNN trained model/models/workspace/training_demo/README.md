# Info
- For 8Gb RAM ownership i recommend images up 1280x720. 
- Do consider resizing your image properly otherwise the trainer won't work due to insufficient RAM
- Do keep the files as they are and only edit what must be edited

# To run a model you must 
1.  Make sure your .jpg(JPEG)
2.  Make sure your images are labeled 1.jpg, 2.pjg, 3.jpg,... and so on
3.  val.txt file must be created with each line consisting of all image numbering, keep the other in check.(sort)
4.  Make sure you the labelImg program and label your boxes accordingly.
5.  Copy all the XML files to the annotations/xmls folder
6.  Run "python3 create_tf_record.py" on the command line
7.  Create/get the appropriate faster_rcnn_inception_v2_coco.config and edit the faster_rcnn_inception_v2_coco.config file pathways
8.  Run "python3 train.py --logtostderr --train_dir=%ABSOLUTE_PATH%/training/ --pipeline_config_path=%ABSOLUTE_PATH%/training/faster_rcnn_inception_v2_coco.config  ...This is a mere example
9.  Once you think it's trained you may cancel anytime halfway
10. Run "python3 export_inference_graph.py --input_type=image_tensor --pipeline_config_path=training/faster_rcnn_inception_v2_coco.config --trained_checkpoint_prefix=training/model.cpkt-#### --output_directory=inference_graph/"
11. Run "python3 objectdetection_v2.py"

**Note:** The #### represents a number which is the checkpoint number of the weights of the model that were saved at a certain point in training.

**Extra:** In case of an ERROR related to the checkpoint, it is recommend to clear the checkpoints and all associated weight and retrain the model from scratch.

