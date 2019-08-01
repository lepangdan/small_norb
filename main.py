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
    # parent_data_path = 'smallnorb_export'
    # files = [f for f in glob.glob(os.join(parent_data_path) + "**/*.txt", recursive=True)]


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

    def load_data(dataset_split):
        import glob
        first_flag = True
        x_data = None
        y_data = None
        for image_path in glob.glob('smallnorb_export/'+str(dataset_split)+'/*.jpg'):
            # print(glob.glob("smallnorb_export/train/"+"*.jpg"))
            print(image_path)
            image = Image.open(image_path)
            image.load()
            image_np = np.asarray(image, dtype="int32")
            y_data = image_path.split(str(dataset_split))[1].split('_')[1]
            print(y_data)
            if first_flag:
                x_data = image_np
                first_flag = False
            else:
                x_data = np.stack((x_data, image_np))
            print(x_data)

            break
        return (x_data, y_data)

    load_data('train')


    # show the image
    # image.show()