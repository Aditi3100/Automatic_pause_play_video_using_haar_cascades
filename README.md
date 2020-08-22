# Automatic pausing and playing of Video Player

The code is supposed to be run before playing any video on any player which has the pause/play feature associated to the spacebar. For example: VLC Media player, YouTube and many more.

The project is written in Python 3.6. Libraries used in this project and necessary to be added for running the code are as follows:

	1. OpenCV (4.2.0)
	2. pyautogui (0.9.50)

The face and eyes are detected from the captured frames with the help of Haar Cascade Classifiers. The xml files used for training the classifier are included in the project. The detected areas in the are to be seen bounded by rectangles of different colors in the real time frame from the video being captured by your camera. The python program is coded to pause the video on the active window when no face is detected for a certain time interval, and plaqy as soon as a face is detected.

For accurate detections, it is recommended to run the code in a bright room and the background should not have any photos with faces or anything resembling a face except the ones to be detected. Also, the accuracy is high if th face is kept upright with respect to the camera.
