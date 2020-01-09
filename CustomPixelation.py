import math
from PIL import Image, ImageStat

def custom_pixelation(img, cell_rows, cell_columns, new_image_dimesions, median_or_mean):

	'''
	Description: 
		This function will split the given image into a grid, then
		take median or mean pixel color in each cell of the grid and create
		a new image (at a given resolution) displaying the mean pixel 
		color in each cell

	Args: 
		img(Image): the base image
		cell_rows(int): the number of cells in each row
		bow_columns(int): the number of cells in each column
		new_image_dimesions((int, int)): the dimesions of the new image
		median_or_mean(String): median or mean

	Output: 
		This function outputs a new image
	'''

	base_image_width = img.size[0] # width of the base image
	base_image_height = img.size[1] # height of the base image
	base_cell_width = math.ceil(base_image_width / cell_rows) # width of each cell for the base image
	base_cell_height = math.ceil(base_image_height / cell_columns) # height of each cell for the base image

	new_image_width = new_image_dimesions[0] # width of the new image
	new_image_height = new_image_dimesions[1] # height of the new image
	new_cell_width = math.ceil(new_image_width / cell_rows) # width of each cell for the new image
	new_cell_height = math.ceil(new_image_height / cell_columns) # height of each cell for the new image	
	
	# coordinates to crop the base image (left top (x, y) and right bottom (x, y))
	base_left = 0
	base_top = -base_cell_height
	base_right = base_cell_width
	base_bottom = 0

	# coordinates to paste the new image (left top (x, y) and right bottom (x, y))
	new_left = 0
	new_top = -new_cell_height
	new_right = new_cell_width
	new_bottom = 0

	new_image = Image.new('RGB', new_image_dimesions, color = 'red' )


	for column in range(0, cell_columns):

		base_top += base_cell_height
		base_bottom += base_cell_height
		base_left = 0
		base_right = base_cell_width

		new_top += new_cell_height
		new_bottom += new_cell_height
		new_left = 0
		new_right = new_cell_width

		for row in range(0, cell_rows):

			if median_or_mean == 'median':
				med = ImageStat.Stat(img.crop((base_left, base_top, base_right, base_bottom))).median
			elif median_or_mean == 'mean':
				med = ImageStat.Stat(img.crop((base_left, base_top, base_right, base_bottom))).mean

			# rounds the mean or median rgb values
			med[0] = round(med[0])
			med[1] = round(med[1])
			med[2] = round(med[2])

			new_image.paste((med[0], med[1], med[2]) ,(new_left, new_top, new_right, new_bottom))			

			base_right += base_cell_width 
			base_left += base_cell_width

			new_right += new_cell_width 
			new_left += new_cell_width

	
	new_image.show()
	

iphone8_resolution = [750, 1334]
laptop_resolution = [1920, 1080]

image1 = Image.open(r"C:\Users\img.PNG") # The file path of the image

custom_pixelation(image1, 10, 10, image1.size, 'median')

#image1.show() # shows the original image


