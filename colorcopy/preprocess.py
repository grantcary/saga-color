import os
from os.path import expanduser
from matplotlib import pyplot as plt
from frame import Image

DATASET = f'{expanduser("~")}/Desktop/dataset'
TEST_IMAGE = f'{expanduser("~")}/Desktop/Images/testimage.jpg'

# TODO: make random image processing function
def process_image(path: str) -> None:
  image = Image(path).gray
  return image

# save pairs of images, original with augmented, change filenames to reflect pairs
def process_dataset() -> None:
  dataset_dir = os.listdir(DATASET)
  if 'pairs' not in dataset_dir:
    os.mkdir(f'{DATASET}/pairs')
  for file, file_num in enumerate(dataset_dir):
    # TODO: get file type and append to filename 
    o_name, a_name = f'{file_num:03d}_o', f'{file_num:03d}_a'
    if o_name not in dataset_dir or a_name not in dataset_dir:
      original = Image(file).img
      augmented = process_image(f'{DATASET}/{file}')

      original.save(f'{DATASET}/{o_name}')
      augmented.save(f'{DATASET}/{a_name}')