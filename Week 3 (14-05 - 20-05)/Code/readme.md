In this weeks code I have used MMU Iris database and tried to detect iris from an eye image.
At first I tried an approach of using Integro differential operators that detects edges and curvatures
over a length and tried to cut out a circle from that but it did'nt give accurate results.
So i then used found contours using python's inbuilt libraries and then applies hough circles 
and found out the largest circle we get which should give us iris.It did better than the first approach
but the circumference wasn't exact as the iris.
