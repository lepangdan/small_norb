import matplotlib.pyplot as plt
from smallnorb.dataset import SmallNORBDataset


plt.ion()


if __name__ == '__main__':

    # Initialize the dataset from the folder in which
    # dataset archives have been uncompressed
    # dataset = SmallNORBDataset(dataset_root='../datasets/smallnorb/')
    #
    # # Dump all images to disk
    # dataset.export_to_jpg(export_dir='smallnorb_export')

    # Explore random examples of the training set
    # to show how data look like
    # dataset.explore_random_examples(dataset_split='train')


    # load and show an image with Pillow
    from PIL import Image
    import os
    import numpy as np
    import glob
    parent_data_path = 'smallnorb_export'
    files = [f for f in glob.glob(os.join(parent_data_path) + "**/*.txt", recursive=True)]


    # load the image
    image = Image.open('smallnorb_export/train/012149_car_04_rt.jpg')
    # summarize some details about the image
    image.load()
    data = np.asarray(image, dtype="int32")
    print(image.format)
    print(image.mode)
    print(image.size)
    print(type(data))
    print('max data:', np.amax(data))
    print('min data:', np.amin(data))

    import glob
    print(glob.glob("smallnorb_export/train"+ "*.jpg"))

    # show the image
    # image.show()