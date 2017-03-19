'''

@author ysbecca Rebecca Stone

Two simple functions which display images using matplotlib.pyplot (http://matplotlib.org/api/pyplot_api.html)
Any image in a format readable by matplotlib.pyplot's imshow() function is good.

'''

import matplotlib.pyplot as plt


def show_images(images, per_row, per_column):
    ''' Displays up to per_row*per_column images with per_row images per row, per_column images per column.
	'''
    fig = plt.figure(figsize=(25, 25))
    data = images[:(per_row*per_column)]

    for i, image in enumerate(data):
        plt.subplot(per_column, per_row, i+1)
        plt.imshow(image)
        plt.axis("off")
    
    plt.show()


def show_patches(images):
    ''' A quick way of displaying up to 100 patches of 12x12px. You can easily change the default number
    	of patches below; remember to change the number of images per column to match.
    '''
    fig = plt.figure(figsize=(12, 12))
    data = images[:100]

    for i, image in enumerate(data):
		plt.subplot(10, 10, i+1)
        plt.imshow(image)
        plt.axis("off")

    plt.show()

def show_image(image):
	''' Display one single image without axis markings. '''
    plt.imshow(image)
    plt.axis("off")
    plt.show()


