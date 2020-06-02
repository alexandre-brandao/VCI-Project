# VCI - Deliverable 5  
---  
## Tensorflow Installation - GPU
### 1) Requirements
- Python 3.7
- pip (package installer for python)
- Nvidia GPU (GTX 650 or newer)
- CUDA Toolkit v.10.0
- CUDNN 7.6.5
- Visual C++ 2015 Build Tools (for windows)
(**warning:** uninstall other vc_redist_2015 dependencies that you have!)

### 2) Packages for python
```
pip install --upgrade tensorflow-gpu==1.14
pip install pillow
pip install lxml
pip install jupyter
pip install matploblib
pip install opencv-contrib-python
pip install pathlib
pip install Cython
pip install labelImg
```

### 3) Models
- Download [TensorFlow Models v.1.13.0](https://github.com/tensorflow/models/tree/r1.13.0) release models;
- Extract zip in path of your choice;
- Rename "models-1.13.0" folder to "models" only.

### 4) Protobuf
- Download lastest protoc release [here](https://github.com/protocolbuffers/protobuf/releases) that fits your OS (Win, Linux or Osx);
- Extract the contents of the downloaded ```protoc-VERSION-OS.zip``` in a directory ```<PATH_TO_PB>``` of your choice (e.g. ```C:\Program Files\Google Protobuf``` for windows);
- Add ```<PATH_TO_PB>``` to your Path environment variable:
    - **Windows:**  
    In "environment variables" > PATH, add the following (examples):  
    ```C:\Program Files\Google Protobuf\bin ```  
    ```C:\Program Files\Google Protobuf\include ```
    - **Linux:**  
    In a terminal:  
    ``` export PATH="<PATH_TO_PB>/bin/:$PATH" ``` (General)  
    ``` export PATH="/user/jreis/protoc-x.x.x-linux-x86_64/bin/:$PATH" ``` (Example)
- In a new Terminal, cd into ```models/research/``` directory and run the following command:  
``` protoc object_detection/protos/*.proto --python_out=. ```

### 5) Add new PATH
- Change directory to ```models\research``` and execute the following cmd:  
```
pip install .
```
- Add ```research/slim``` to your **PYTHONPATH**:  
    - **Windows:**  
    In "environment variables" > PYTHONPATH, add the following:  
    (Press ```NEW...```  if you don't have PYTHONPATH, and write PYTHONPATH)  
    ```<PATH_TO_YOUR_PROJECT>\models\research\slim ```
    - **Linux:**  
    In a terminal (in ```models/research```):  
    ``` export PYTHONPATH=$PYTHONPATH:<PATH_TO_TF>/TensorFlow/models/research/slim ```

### 6) COCO API
- **Windows:**  
```
pip install git+https://github.com/philferriere/cocoapi.git#subdirectory=PythonAPI
```
- **Linux:**  
```
git clone https://github.com/cocodataset/cocoapi.git
cd cocoapi/PythonAPI
make
cp -r pycocotools <PATH_TO_TF>/TensorFlow/models/research/
```

- The default metrics are based on those used in Pascal VOC evaluation.  
To use the COCO ```object detection``` metrics add metrics_set: ```"coco_detection_metrics"``` to the eval_config message in the config file.

### -- Useful links
[* Windows anaconda install, with CUDA and CUDNN installation steps](https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/install.html#set-env)  

---
## Execute project
### 1) Tensorflow - ModeNet
- Copy  ```research/``` folder into folder ```models/``` (overwrite if necessary?);
- Change directory to ```models/research/object_detection/```;
- ```python object_detection_robots.py``` or ```python3 object_detection_robots.py```.

### 2) Tensorflow - Faster R-CNN trained model
- Copy  ```models/``` folder into your project folder, where ```models/``` is stored (it wont overwrite everything);
- Change directory to ```models/workspace/training_demo/```;
- ```python objectdetection.py``` or ```python3 objectdetection.py```.
