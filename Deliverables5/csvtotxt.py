from matplotlib import patches
import pandas as pd
import matplotlib.pyplot as plt


path = 'train/'

def csv2txt(dir):
    train = pd.read_csv(dir + 'global.csv')
    train.head()

    data = pd.DataFrame()
    data['format'] = train['filename']

    # as the images are in train_images folder, add train_images before the image name
    for i in range(data.shape[0]):
        data['format'][i] = 'train/' + data['format'][i]

    # add xmin, ymin, xmax, ymax and class as per the format required
    for i in range(data.shape[0]):
        data['format'][i] = data['format'][i] + ',' + str(train['xmin'][i]) + ',' + str(train['ymin'][i]) + ',' + str(train['xmax'][i]) + ',' + str(train['ymax'][i]) + ',' + train['cell_type'][i]

    data.to_csv('annotate.txt', header=None, index=None, sep=' ')

csv2txt(path)