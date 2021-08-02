# Advanced Road Lane Detection

## Camera Calibration

When a camera captures an image of the 3D world, it transforms it into a 2D image through multiple lenses. Lenses can introduce **distortion**, since light rays often bend too much or too little at the edges of the curved lens, causing  images to result distorted (curved) at their edges. This type of distortion is called ***radial distortion***. A different type of distortion is the so-called ***tangential distortion***, which can occur when a camera's lens is not perfectly parallel to the imaging plane. Tangential distortion causes the image to look tilted, vertically or horizontally. Consequently, distortion can change both the shape and the size of an object.

#@# Distortion correction

A radially distorted image can be corrected by a spatial transformation, according to some parameters k_1,k_2 and k_3. In particular, we can calculate the distance r between a point (x_{corrected},y_{corrected}) in the undistorted image and the center of the image distortion (x_c,y_c), often coinciding with the image center.

    x_{distorted} = x_{ideal}\left(1+k_1r^2 + k_2r^4 + k_3r^6\right)
    y_{distorted} = y_{ideal}\left(1+k_1r^2 + k_2r^4 + k_3r^6\right)

In the case of tangential distortion, the parameters become $p_1$ and $p_2$, and the correction formula becomes:

    x_{corrected} = x + \left[2p_1xy + p_2 (r^2 + 2x^2) \right]
    y_{corrected} = y + \left[p_1(r^2 + 2y^2) + 2p_2xy \right]
    
    

## Perspective Transformation

Perspectivity is the formation of an image in a picture plane of a scene viewed from a fixed point. Perspective is the phenomenon where an object appears smaller the farther away it is from the viewpoint, and parallel lines appear to converge to a point called *point at infinity*, or *ideal point*. The greater the magnitude of an object's *z*-coordinate, or distance from the camera, the smaller it will appear in the 2D image. A perspective transform maps the points in an image to different ones with a new perspective. It essentially transform the apparent *z*-coordinate of object points which in turn changes that object 2D image representation. In other words it "pushes away" points that are closer to the viewpoint, and "pushes towards" points that are far from the viewpoint.

Transforming a 2D image in a bird's-eye view that will facilitate the task of interpolating the lines and determining their curvature. The process of applying a perspective transform is similar to fix image distortion, but in this case, instead of mapping object points to image points, we will map the points in a given image to different, desired, image points with a new perspective.



## HLS

The HLS space (hue, lightness, and saturation). To get some intuition about these color spaces, you can generally think of Hue as the value that represents color independent of any change in brightness. So if you imagine a basic red paint color, then add some white to it or some black to make that color lighter or darker -- the underlying color remains the same and the hue for all of these colors will be the same. On the other hand, Lightness and Value represent different ways to measure the relative lightness or darkness of a color. For example, a dark red will have a similar hue but much lower value for lightness than a light red. Saturation also plays a part in this; saturation is a measurement of colorfulness. So, as colors get lighter and closer to white, they have a lower saturation value, whereas colors that are the most intense, like a bright primary color (imagine a bright red, blue, or yellow), have a high saturation value. 


## Histogram Peak

Peaks in the histogram of the lower half of the thresholded warped image indicate a concentration of white pixels, meaning that a line is likely to be present at that *x* position. That information can be used as a starting point for where to search for the lines. From that point, we can use a sliding window, placed around the line centers, to find and follow the lines up to the top of the frame.




## Sliding Window

We can use the two highest peaks in the histogram as a starting point fordetermining where the lane lines are, and then use sliding windows moving upward in the image, further along the road, to determine where the lines go. We proceed as follows:

    1. Split the histogram into two sides, one for each line.
    2. Set up hyperparameters related to the sliding window.
    3. Iterate through the windows, re-centering the given window sliding left or right if it finds the mean position of the activated pixels within the window to have shifted more than a certain, specified, value.
    4. At each iteration, append to lists `left_lane_inds` and `right_lane_inds` the activated pixels that fall into the window.
    5. After we have found all the pixels belonging to each line through the sliding window, we fit a polynomial to the line.
