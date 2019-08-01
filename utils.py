from PIL import Image
import numpy as np
import glob

def load_data(dataset_split):

    first_flag = True
    x_data = None
    y_data = None
    for image_path in glob.glob('smallnorb_export/' + str(dataset_split) + '/*.jpg'):
        # print(glob.glob("smallnorb_export/train/"+"*.jpg"))
        print(image_path)
        image = Image.open(image_path)
        image.load()
        image_np = np.asarray(image, dtype="int32")
        y_data = image_path.split(str(dataset_split))[1].split('_')[1]
        # print(y_data)
        if first_flag:
            x_data = image_np

            first_flag = False
        else:
            x_data = np.concatenate((x_data, image_np), axis=0)
        # print(x_data)
    return x_data, y_data
