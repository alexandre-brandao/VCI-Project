import pandas as pd
import os
from matplotlib import patches
import matplotlib.pyplot as plt

"""
def run_csvreader(directory):
    for CSV in os.listdir(directory):
        if '.csv' in CSV:
            train = pd.read_csv(directory+'/'+CSV)
            train.head()
        
        if('.png' in CSV)
            image = plt.imread('images/1.jpg')
            plt.imshow(image)
"""
"""
run_csvreader('ObjectDetec/train')
run_csvreader('ObjectDetec/test')
"""

path = 'ObjectDetec/train/1'
train = pd.read_csv(path + '.csv')
train.head()

image = plt.imread(path + '.png')
plt.imshow(image)
#plt.show()

# Number of unique training images
train['filename'].nunique()

# Number of classes
train['name'].value_counts()

fig = plt.figure()

# add axes to the image
ax = fig.add_axes([0, 0, 1, 1])

# read and plot the image
image = plt.imread(path+".png")
plt.imshow(image)

print(train[train.name == 'Referee'])


# iterating over the image for different objects
for _, row in train[train.filename == "1.png"].iterrows():

    xmin = row.xmin
    xmax = row.xmax
    ymin = row.ymin
    ymax = row.ymax

    width = xmax - xmin
    height = ymax - ymin

    print('('+str(width)+','+str(height)+')\n')
    pos = (xmax - 4git 0, ymin - 20)
    # assign different color to different classes of objects
    if row[1] == 'Ball':
        edgecolor = 'r'
        ax.annotate('Ball', xy=pos)

    if row[1] == 'Referee':
        edgecolor = 'r'
        ax.annotate('Referee', xy=pos)

    elif row[1] == 'BLUE2':
        edgecolor = 'b'
        ax.annotate('BLUE2', xy=pos)

    elif row[1] == 'BLUE3':
        edgecolor = 'g'
        ax.annotate('BLUE3', xy=pos)

    elif row[1] == 'BLUE4':
        edgecolor = 'g'
        ax.annotate('BLUE4', xy=pos)

    elif row[1] == 'BLUE5':
        edgecolor = 'g'
        ax.annotate('BLUE5', xy=pos)

    elif row[1] == 'BLUE6':
        edgecolor = 'g'
        ax.annotate('BLUE6', xy=pos)

    elif row[1] == 'R_Goalie':
        edgecolor = 'g'
        ax.annotate('R_Goalie', xy=pos)

    elif row[1] == 'RED2':
        edgecolor = 'g'
        ax.annotate('RED2', xy=pos)

    elif row[1] == 'RED3':
        edgecolor = 'g'
        ax.annotate('RED3', xy=pos)

    elif row[1] == 'RED4':
        edgecolor = 'g'
        ax.annotate('RED4', xy=pos)

    elif row[1] == 'RED5':
        edgecolor = 'g'
        ax.annotate('RED5', xy=pos)

    elif row[1] == 'B_Goalie':
        edgecolor = 'g'
        ax.annotate('B_Goalie', xy=pos)

    # add bounding boxes to the image
    rect = patches.Rectangle((xmin, ymin), width, height, edgecolor=edgecolor, facecolor='none')

    ax.add_patch(rect)

plt.show()


