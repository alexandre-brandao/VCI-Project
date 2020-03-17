#####
# @@Alexandre Brandao
# Transform all XML data in train/test folder to CSV for image processing
###
from xml.etree import ElementTree
import os
import csv

def run_program(directory):

    for XML in os.listdir(directory):
        if '.xml' in XML:
            #GET XML FILE NUMBER
            result = ''.join([i for i in XML if i.isdigit()])

            # Read the file
            tree = ElementTree.parse(directory+'/'+XML)

            # Create xml file
            data = open(directory+'/'+result+'.csv', 'w', newline='', encoding='utf-8')
            csvwriter = csv.writer(data)

            col_names = ['filename','name', 'xmin', 'xmax', 'ymin', 'ymax' ]
            csvwriter.writerow(col_names)

            root = tree.getroot()


            for info in root.findall('object'):

                data_line = []
                data_line.append(root[1].text) # First we append file name
                data_line.append(info.find('name').text) # Second we append object name
                data_line.append(info.find('bndbox').find('xmin').text)  # Third  we append xmin
                data_line.append(info.find('bndbox').find('xmax').text)  # Fourth we append xmax
                data_line.append(info.find('bndbox').find('ymin').text)  # Fith   we append ymin
                data_line.append(info.find('bndbox').find('ymax').text)  # Sixth  we append ymax

                csvwriter.writerow(data_line)

            data.close()



run_program('ObjectDetec/train')
run_program('ObjectDetec/test')