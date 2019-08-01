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

    dataset.group_dataset_by_category_and_instance('train')

    # load and show an image with Pillow
    from PIL import Image
    import numpy as np

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

    # show the image
    # image.show()