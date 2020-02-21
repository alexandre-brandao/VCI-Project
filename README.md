## VCI-Project
Deliverables

# Deliverable 1 (26/02/2020):

Acquire images using the Raspberry camera or webcam connected to your computer. Explore saving videos using compression algorithms (ex. H.264, MJPEG, etc.). Apply color calibration (intensity normalization, white balance, etc). Include a watermark (it can be a string identifying the group or a chosen picture). Video player able to work with the camera in real-time and read video files.

# Deliverable 2 (11/03/2020):

Transform the acquired images to other color spaces, namely YUV and HSV. Calculate and display the histograms in real-time of the acquired and transformed images. Convert the acquired images to grayscale and apply histogram equalization. Apply gaussian and blur filters to the acquired images, exploring different filter kernels.

# Deliverable 3 (25/03/2020):

Interact with the OpenCV windows, namely using the mouse (you have to implement the method cv.setMouseCallback()) and trackbars (see for example the methods cv.getTrackbarPos(), cv.createTrackbar()). Segment the most important colors of the CAMBADA soccer field based on color threshold. This threshold is controlled by the developed trackbars in the previous exercise. Perform object detection on grayscale images, resulting from the previous segmentation, morphological operators and low level image features (ball, goals, soccer lines, robots, referee / people, etc). Extra mile: Explore automatic segmentation algorithms (e.g. watershed, region growing, etc).

# Deliverable 4 (15/04/2020):

Find image gradients (Sobel, Scharr and Laplacian derivatives). Apply the Canny edge detection algorithm, exploring its parameters. Explore how to manipulate the corresponding contours. Perform object detection using contour detection. Perform line detection and ball detection using the Hough transform (ex. this should allow the detection of balls with different colors and balls in the air). Extra mile: Explore other object detection algorithms (e.g. Machine Learning).

# Deliverable 5 (06/05/2020):

Perform intrinsic and extrinsic camera parameter calibration using a chess board.

# Deliverable 6 (20/05/2020):

Explore the Lucas-Kanade optical flow algorithm to perform object tracking. Using the developed object detection algorithms, the software must be able to distinguish which objects are being tracked (multiple balls and robots; assigning an unique ID, etc). Estimate the travelled distance of the ball and teams during a game.

# Deliverable 7 (June): 

Demo in a soccer game between CAMBADA and a human team. 
Build an application that is able to:

