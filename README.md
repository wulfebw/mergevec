mergevec
========

Mergevec.py is used to merge .vec files for use in training a cascade classifier with openCV's opencv_traincascade. This code was made as replacement for mergevec.cpp (created by Naotoshi Seo. See: http://note.sonots.com/SciSoftware/haartraining/mergevec.cpp.html) in order to avoid recompiling opencv with mergevec.cpp. 

#To use mergevec.py:

	(1) Place all .vec files to be merged in a single directory ("vec_directory").
	(2) Download mergevec.py
	(3) Navigate to mergevec.py in your CLI (terminal or cmd) and enter "python mergevec.py -v your_vec_directory -o your_output_filename.vec".

#To test the output of mergevec.py:

	(1) Install openCV.
	(2) Navigate to the output file in your CLI (terminal or cmd).
	(3) Type "opencv_createsamples -w img_width -h img_height -vec your_output_filename.vec". This should show the .vec files in sequence.

The aggregate .vec output from mergevec.py has successfully been used to train a cascade. See the below for resources on training cascade classifiers.
#opencv_traincascade Resources

OpenCV:
http://docs.opencv.org/doc/user_guide/ug_traincascade.html

Naotoshi Seo:
http://note.sonots.com/SciSoftware/haartraining.html

Coding Robin:
http://coding-robin.de/2013/07/22/train-your-own-opencv-haar-classifier.html

StackOverflow:
http://stackoverflow.com/questions/16058080/how-to-train-cascade-properly
