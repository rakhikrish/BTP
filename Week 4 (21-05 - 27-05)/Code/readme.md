In this week's code I tried to locate the iris precisely and segment out the iris part from the eye
image.So to do that in various steps
```
-Grayscaled the image first
-Performed canny edge detection to generate an edge map
-Applied Gaussian blur
-Applied non-max suppression
-Applies hysteresis thresholding
-Apllied circular hough transform
```
By these we located the iris and then segmented out the iris from eye image.
And then did like a test run on gabor filtering for a sample image.
And tried a hand on applying gamma inflation too but it didn't have any effect
so isolated that part at the end of notebook.
