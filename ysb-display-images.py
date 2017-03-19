'''

@author ysbecca Rebecca Stone

Two simple functions which display images using matplotlib.pyplot (http://matplotlib.org/api/pyplot_api.html)
Any image in a format readable by matplotlib.pyplot's imshow() function is good.

'''

import matplotlib.pyplot as plt


def show_images(images, per_row, per_column, patches=False):
    ''' Displays an array of images with per_row images per row, per_column images per column,
    	and an optional predefined mode for displaying patches, which displays up to 100 patches 
    	12x12px each.
    '''
    if(patches):
        fig = plt.figure(figsize=(12, 12))
        data = images[:100]
    else:
        fig = plt.figure(figsize=(25, 25))
        data = images

    for i, image in enumerate(data):
        if(patches):
            plt.subplot(10, 10, i+1)
        else:
            plt.subplot(per_column, per_row, i+1)
        plt.imshow(image)
        plt.axis("off")
    
    plt.show()


def show_image(image):
	''' Display one single image without axis markings. '''
    plt.imshow(image)
    plt.axis("off")
    plt.show()


