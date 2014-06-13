"""
File: mergevec.py 
Author: blake.w.wulfe@gmail.com 
Date: 6/13/2014
File Description:

	This file contains a function that merges .vec files called merge_vec_files. I made it as a replacement for mergevec.cpp created by Naotoshi Seo (See: http://note.sonots.com/SciSoftware/haartraining/mergevec.cpp.html). 

	To use the function:
	(1) Place all .vec files to be merged in a single directory (vec_directory)
	(2) Go to the bottom of the file and enter this vec_directory along with an output filename
	(3) Navigate to this file in your CLI (terminal or cmd) and type "python mergevec.py"

"""


import sys
import glob
import struct
import traceback

def exception_response(e):
	exc_type, exc_value, exc_traceback = sys.exc_info()
		lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
		for line in lines:
			print(line):

def merge_vec_files(vec_directory, output_vec_file):
	"""
	Iterates throught the .vec files in a directory and combines them. 

	(1) Iterates through files getting a count of the total images in the .vec files
	(2) checks that the image sizes in all files are the same

	The format of a .vec file is:

	4 bytes denoting total images (int)
	4 bytes denoting size of images (int)
	2 bytes denoting min value (short)
	2 bytes denoting max value (short)

	ex: 	6400 0000 4605 0000 0000 0000

		hex		6400 0000  	4605 0000 		0000 	0000
			   	# images  	size of h * w	min		max
		dec	    100         1350			0 		0

	:type vec_directory: string
	:param vec_directory: Name of the directory containing .vec files to be combined

	:type output_vec_file: string
	:param output_vec_file: Name of aggregate .vec file for output

	"""


	files = glob.glob('{0}/*.vec'.format(vec_directory))

	# Check to make sure there are .vec files in the directory
	if len(files) <= 0:
		print('Vec files to be mereged could not be found from directory: {0}'.format(vec_directory))
		sys.exit(1)
	# Check to make sure there are more than one .vec files
	if len(files) == 1:
		print('Only 1 vec file was found in directory: {0}. Cannot merge a single file.'.format(vec_directory))
		sys.exit(1)


	# Get the value for the first image size
	prev_image_size = 0
	try:
		with open(files[0], 'rb') as vecfile:
			content = ''.join(vecfile.readlines())
			val = struct.unpack('<iihh', content[:12])
			prev_image_size = val[1]
	except IOError as e:
		print('An IO error occured while processing the file: {0}'.format(f))
		exception_response(e)


	# Get the total number of images
	total_num_images = 0
	for f in files:
		try:
			with open(f, 'rb') as vecfile:	
				content = ''.join(vecfile.readlines())
				val = struct.unpack('<iihh', content[:12])
				num_images = val[0]
				image_size = val[1]
				if image_size != prev_image_size:
					print('The image sizes in the .vec files differ. These values must be the same.')
					print('The image size of file {0}: {1}'.format(f, image_size))
					print('The image size of previous files: {0}'.format(prev_image_size))
					sys.exit(1)

				total_num_images += num_images
		except IOError as e:
			print('An IO error occured while processing the file: {0}'.format(f))
			exception_response(e)

	
	# Iterate through the .vec files, writing their data (not the header) to the output file
	# '<iihh' means 'little endian, int, int, short, short'
	header = struct.pack('<iihh', total_num_images, image_size, 0, 0)
	try:
		with open(output_vec_file, 'wb') as outputfile:
			outputfile.write(header)

			for f in files:
				with open(f, 'rb') as vecfile:
					content = ''.join(vecfile.readlines())
					data = content[12:]
					outputfile.write(data)
	except Exception as e:
		exception_response(e)


if __name__ == '__main__':
	# fill in the directory name and the output filename below
	vec_directory = 
	output_filename = 
	merge_vec_files(vec_directory, output_filename)

