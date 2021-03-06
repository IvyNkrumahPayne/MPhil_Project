"""
Usage:
  # From tensorflow/models/
  # Create train data:
  python generate_tfrecord.py --input_csv=data/train_labels.csv  --output_tfrecord=train.record

  # Create test data:
  python generate_tfrecord.py --input_csv=data/test_labels.csv  --output_tfrecord=test.record
"""
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

import os
import io
import pandas as pd
import tensorflow as tf

from PIL import Image
from object_detection.utils import dataset_util
from collections import namedtuple, OrderedDict
import argparse


# TO-DO replace this with label map
def class_text_to_int(row_label):
    if row_label.strip() == 'skimming':
        print ('skimming matched')
        return 1
    elif row_label == 'occlusion':
        print ('occlusion matched')
        return 2
    elif row_label == 'logical attack':
        print ('logical attack matched')
        return 3
    elif row_label == 'physical attack':
        print ('physical attack matched')   
        return 4
    elif row_label == 'robbery':
        print ('robbery matched') 
        return 5
    elif row_label == 'malware':
        print ('malware matched')
        return 6
    elif row_label == 'jackpotting':
        print ('jackpotting matched') 
        return 7
    elif row_label == 'ATM out of service':
        print ('ATM out of service matched') 
        return 8
    elif row_label == 'transaction reversal fraud':
      print ('transaction reversal fraud matched')   
      return 9
    elif row_label == 'logical attack':
       print ('logical attack matched')
       return 10
    elif row_label == 'cash trapping':
       print ('cash trapping matched')
       return 11       
    elif row_label == 'card trapping':
       print ('card trapping matched')
       return 12
    elif row_label == 'normal':
       print ('normal')
       return 13
    else:
        print ('problem at row: ')
        print (row_label)
        print ('name not existing...')
        return 0


def split(df, group):
    data = namedtuple('data', ['filename', 'object'])
    gb = df.groupby(group)
    return [data(filename, gb.get_group(x)) for filename, x in zip(gb.groups.keys(), gb.groups)]


def create_tf_example(group, path):
    with tf.gfile.GFile(os.path.join(path, '{}'.format(group.filename)), 'rb') as fid:
        encoded_jpg = fid.read()
    encoded_jpg_io = io.BytesIO(encoded_jpg)
    image = Image.open(encoded_jpg_io)
    width, height = image.size

    filename = group.filename.encode('utf8')
    image_format = b'jpg'
    xmins = []
    xmaxs = []
    ymins = []
    ymaxs = []
    classes_text = []
    classes = []

    for index, row in group.object.iterrows():
        xmins.append(row['xmin'] / width)
        xmaxs.append(row['xmax'] / width)
        ymins.append(row['ymin'] / height)
        ymaxs.append(row['ymax'] / height)
        classes_text.append(row['class'].encode('utf8'))
        classes.append(class_text_to_int(row['class']))

    tf_example = tf.train.Example(features=tf.train.Features(feature={
        'image/height': dataset_util.int64_feature(height),
        'image/width': dataset_util.int64_feature(width),
        'image/filename': dataset_util.bytes_feature(filename),
        'image/source_id': dataset_util.bytes_feature(filename),
        'image/encoded': dataset_util.bytes_feature(encoded_jpg),
        'image/format': dataset_util.bytes_feature(image_format),
        'image/object/bbox/xmin': dataset_util.float_list_feature(xmins),
        'image/object/bbox/xmax': dataset_util.float_list_feature(xmaxs),
        'image/object/bbox/ymin': dataset_util.float_list_feature(ymins),
        'image/object/bbox/ymax': dataset_util.float_list_feature(ymaxs),
        'image/object/class/text': dataset_util.bytes_list_feature(classes_text),
        'image/object/class/label': dataset_util.int64_list_feature(classes),
    }))
    return tf_example


def main(_):

     # Taking command line arguments from users
    parser = argparse.ArgumentParser()
    parser.add_argument('-in', '--input_csv', help='define the input xml file', type=str, required=True)
    parser.add_argument('-out', '--output_tfrecord', help='define the output file ', type=str, required=True)
    args = parser.parse_args()
    writer = tf.python_io.TFRecordWriter(args.output_tfrecord)
    path = os.path.join(os.getcwd(), 'images/ATM tampering/image2')
    examples = pd.read_csv(args.input_csv)
    grouped = split(examples, 'filename')
    for group in grouped:
        tf_example = create_tf_example(group, path)
        writer.write(tf_example.SerializeToString())

    writer.close()
    output_path = os.path.join(os.getcwd(), args.output_tfrecord)
    print('Successfully created the TFRecords: {}'.format(output_path))


if __name__ == '__main__':
    tf.app.run()
