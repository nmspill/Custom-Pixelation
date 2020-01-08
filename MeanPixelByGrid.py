import math
from PIL import Image, ImageStat

image1 = Image.open(r'img.jpg')

def mean_pixels(img, box_rows, box_columns, new_image_dimesions):

	base_image_width = img.size[0] # width of the base image
	base_image_height = img.size[1] # height of the base image
	base_box_width = math.ceil(base_image_width / box_rows) # width of each box for the base image
	base_box_height = math.ceil(base_image_height / box_columns) # height of each box for the base image

	new_image_width = new_image_dimesions[0] # width of the new image
	new_image_height = new_image_dimesions[1] # height of the new image
	new_box_width = math.ceil(new_image_width / box_rows) # width of each box for the new image
	new_box_height = math.ceil(new_image_height / box_columns) # height of each box for the new image	
	
	# coordinates to crop the base image (left top (x, y) and right bottom (x, y))
	base_left = 0
	base_top = -base_box_height
	base_right = base_box_width
	base_bottom = 0

	# coordinates to paste the new image (left top (x, y) and right bottom (x, y))
	new_left = 0
	new_top = -new_box_height
	new_right = new_box_width
	new_bottom = 0

	new_image = Image.new('RGB', new_image_dimesions, color = 'red' )


	for column in range(0, box_columns):

		base_top += base_box_height
		base_bottom += base_box_height
		base_left = 0
		base_right = base_box_width

		new_top += new_box_height
		new_bottom += new_box_height
		new_left = 0
		new_right = new_box_width

		for row in range(0, box_rows):
			
			mean = ImageStat.Stat(img.crop((base_left, base_top, base_right, base_bottom))).mean

			# rounds the mean rgb values
			mean[0] = round(mean[0])
			mean[1] = round(mean[1])
			mean[2] = round(mean[2])

			new_image.paste((mean[0], mean[1], mean[2]) ,(new_left, new_top, new_right, new_bottom))			

			base_right += base_box_width 
			base_left += base_box_width

			new_right += new_box_width 
			new_left += new_box_width

iphone8_resolution = [750, 1334]
laptop_resolution = [1920, 1080]
mean_pixels(image1, 5, 10, iphone8_resolution)


