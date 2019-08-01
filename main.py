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

    # load the image
    image = Image.open('smallnorb_export/train/012149_car_04_rt.jpg')
    # summarize some details about the image
    print(image.format)
    print(image.mode)
    print(image.size)
    print(image)

    # show the image
    # image.show()