#####
# @@Alexandre Brandao
# Global transform xml files into 1 big csc file
###
from xml.etree import ElementTree
import os
import csv

path = 'keras-frcnn/'

def run_program(directory):
    # Create xml file
    data = open(directory + '/global.csv', 'w', newline='', encoding='utf-8')
    csvwriter = csv.writer(data)

    # Write initial line of data
    col_names = ['filename', 'name', 'xmin', 'xmax', 'ymin', 'ymax']
    csvwriter.writerow(col_names)

    for XML in os.listdir(directory):
        if '.xml' in XML:

            # Read the file
            tree = ElementTree.parse(directory+'/'+XML)
            #Get root
            root = tree.getroot()

            for info in root.findall('object'):

                data_line = []
                data_line.append(root[1].text)  # First we append file name
                data_line.append(info.find('name').text) # Second we append object name
                data_line.append(info.find('bndbox').find('xmin').text)  # we append xmin
                data_line.append(info.find('bndbox').find('xmax').text)  # we append xmax
                data_line.append(info.find('bndbox').find('ymin').text)  # we append ymin
                data_line.append(info.find('bndbox').find('ymax').text)  # we append ymax

                csvwriter.writerow(data_line)

    data.close()


run_program(path + 'train')
run_program(path + 'test')