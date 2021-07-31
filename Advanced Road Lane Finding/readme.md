## Camera Calibration

When a camera captures an image of the 3D world, it transforms it into a 2D image through multiple lenses. Lenses can introduce **distortion**, since light rays often bend too much or too little at the edges of the curved lens, causing  images to result distorted (curved) at their edges. This type of distortion is called ***radial distortion***. A different type of distortion is the so-called ***tangential distortion***, which can occur when a camera's lens is not perfectly parallel to the imaging plane. Tangential distortion causes the image to look tilted, vertically or horizontally. Consequently, distortion can change both the shape and the size of an object.

#@# Distortion correction

A radially distorted image can be corrected by a spatial transformation, according to some parameters k_1,k_2 and k_3. In particular, we can calculate the distance r between a point (x_{corrected},y_{corrected}) in the undistorted image and the center of the image distortion (x_c,y_c), often coinciding with the image center.

    x_{distorted} = x_{ideal}\left(1+k_1r^2 + k_2r^4 + k_3r^6\right)
    y_{distorted} = y_{ideal}\left(1+k_1r^2 + k_2r^4 + k_3r^6\right)

In the case of tangential distortion, the parameters become $p_1$ and $p_2$, and the correction formula becomes:

    x_{corrected} = x + \left[2p_1xy + p_2 (r^2 + 2x^2) \right]
    y_{corrected} = y + \left[p_1(r^2 + 2y^2) + 2p_2xy \right]
    
    
