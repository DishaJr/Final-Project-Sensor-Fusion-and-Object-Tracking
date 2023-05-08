# Final-Project-Sensor-Fusion-and-Object-Tracking

## **Task :**

* Implement an EKF to track a single real-world target with lidar measurement input over time.
* Implement the track management to initialize and delete tracks, set a track state and a track score.
* Implement a single nearest neighbor data association to associate measurements to tracks.
* Implement the nonlinear camera measurement model.

#

In each step a set of instructions are followed which are set in Udacity's project instructions tabs as well as providing the TODO's to each file. The result of following these steps can be seen below.

**Step 1 :**

![Figure_1](https://github.com/DishaJr/Final-Project-Sensor-Fusion-and-Object-Tracking/blob/main/AAAA)

**Step 2 :**

![Figure_2](https://github.com/DishaJr/Final-Project-Sensor-Fusion-and-Object-Tracking/blob/main/Screenshot%20from%202023-05-07%2011-20-16.png)

**Step 3 :**

![Figure_3](https://github.com/DishaJr/Final-Project-Sensor-Fusion-and-Object-Tracking/blob/main/Screenshot%20from%202023-05-07%2015-22-05.png)
![Figure_4](https://github.com/DishaJr/Final-Project-Sensor-Fusion-and-Object-Tracking/blob/main/Screenshot%20from%202023-05-07%2015-22-13.png)
![Figure_5](https://github.com/DishaJr/Final-Project-Sensor-Fusion-and-Object-Tracking/blob/main/Screenshot%20from%202023-05-07%2015-22-45.png)
![Figure_6](https://github.com/DishaJr/Final-Project-Sensor-Fusion-and-Object-Tracking/blob/main/Screenshot%20from%202023-05-07%2015-23-09.png)

**Step 4 :**

![Figure_7](https://github.com/DishaJr/Final-Project-Sensor-Fusion-and-Object-Tracking/blob/main/Screenshot%20from%202023-05-07%2015-41-22.png)
![Figure_8](https://github.com/DishaJr/Final-Project-Sensor-Fusion-and-Object-Tracking/blob/main/Screenshot%20from%202023-05-07%2015-41-43.png)
![Figure_9](https://github.com/DishaJr/Final-Project-Sensor-Fusion-and-Object-Tracking/blob/main/BBBBBBB)

#


* Do you see any benefits in camera-lidar fusion compared to lidar-only tracking (in theory and in your concrete results)?

There are several benefits to using camera-lidar fusion compared to lidar-only tracking. Camera sensors provide high-resolution images that can help in detecting and tracking objects with greater accuracy. Lidar sensors, on the other hand, provide accurate distance measurements but with lower resolution. By combining the two, we can get the best of both worlds and improve the overall accuracy of object tracking.

Camera sensors can provide additional information about the objects being tracked, such as their color, shape, and texture. This information can be useful in distinguishing between objects that are similar in shape and size, but different in appearance.

In my concrete results, I observed that camera-lidar fusion improved the tracking accuracy and reduced the number of false positives compared to lidar-only tracking.

Overall, camera-lidar fusion has the potential to improve the accuracy and robustness of object tracking in various scenarios, especially in complex environments where objects have similar shapes and sizes.

#

* Which challenges will a sensor fusion system face in real-life scenarios? Did you see any of these challenges in the project?

Sensor fusion systems can face several challenges in real-life scenarios :
  * Sensor Calibration
  * Sensor Occlusion
  * Sensor Noise
  * Computational Complexity
  * Environmental Variability

#

* Can you think of ways to improve your tracking results in the future?

  * Improved Sensor Calibration
  * Advanced Data Association Techniques
  * Multi-Object Tracking
  * Incorporating additional sensors, such as radar and GPS, to provide more accurate and reliable tracking results
  * Using more advanced filtering techniques such as the Unscented Kalman filter or the Particle filter
