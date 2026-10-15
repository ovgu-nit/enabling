---
title: "SAR-SLAM: Semantic-Aware Recognition for Dynamic SLAM in Robotic Applications"
description: |
  SAR-SLAM is an RGB-D SLAM framework that keeps tracking reliable when people and objects move through the scene. It combines YOLOv8 semantic segmentation with RANSAC-based Homography motion verification, so that only objects whose independent motion is actually confirmed are filtered out, while stationary people and parked objects are preserved as stable landmarks. Implemented as a modular ROS2 package on top of an unmodified ORB-SLAM3, it reduces Absolute Trajectory Error by up to 96% on the dynamic sequences of the TUM RGB-D benchmark.
background: /assets/theme/images/sar_slam.png
image: /assets/theme/images/sar_slam.png
author: "Basheer Al-Tawil, Magnus Jung, Thorsten Hempel, Ayoub Al-Hamadi"
categories: [Publication, Journal Paper, SLAM, Dynamic Environments, Robotics]
journal: "**MDPI Robotics 2026** [[paper]](https://doi.org/10.3390/robotics15070136)"
tags: [MDPI Robotics 2026, Journal, SLAM, Semantic Segmentation]
---

## SAR-SLAM: Semantic-Aware Recognition for Dynamic SLAM in Robotic Applications

Simultaneous Localization and Mapping is the foundation of autonomous navigation, but it rests on an assumption that human-centric environments routinely break: that the world stands still. Visual SLAM systems such as ORB-SLAM3 estimate camera motion by tracking visual features across consecutive frames. When a person walks through a hospital corridor or a shared workspace, features on their clothing and body enter the tracking process and move independently of the camera, violating the geometric constraints the system depends on. The result is incorrect motion estimates, accumulating drift, and in many cases complete tracking failure. Existing remedies each pay a price. Purely semantic methods remove every instance of a potentially mobile class and discard valuable static information along with the genuine movers — a stationary person in a waiting room or a parked car provides exactly the kind of stable, long-lived features a localizer wants. Purely geometric methods avoid over-removal but are noise-sensitive, missing slow motion and mistaking camera-induced parallax for independent motion.

SAR-SLAM replaces the usual remove-everything reflex with a **verify-before-remove** strategy organized in three stages. First, **YOLOv8-seg semantic segmentation** proposes dynamic object candidates, keeping detections above a confidence of 0.5 and marking the mobile classes *person, car, bicycle, bus, truck*. Crucially, pixel-level filtering uses the instance masks rather than bounding boxes, so static background that merely falls inside a mover's box is not thrown away. Second, **RANSAC-based Homography analysis** performs geometric motion verification. ORB features are matched between consecutive frames and filtered with Lowe's ratio test at 0.75; a Homography estimated by RANSAC captures the single consistent pattern in which the static background shifts under camera motion. Points whose re-projection error stays within 2.0 pixels are inliers that move with the background, while larger errors mark independent motion. A semantic region is declared truly dynamic only when more than 30% of its features are outliers — and rather than a binary label, the median outlier displacement yields each object's motion direction and magnitude.

The third stage is an **adaptive fusion** mechanism. A scalar scene-complexity score measures the fraction of image area occupied by motion-verified mobile objects, weighted by motion magnitude against a significance threshold of 0.7 calibrated on the TUM data. That score drives a controller that switches operating mode per frame: below 0.3 only semantic regions are considered, between 0.3 and 0.6 only geometric regions, and at 0.6 and above both cues are fused. Semantic and geometric masks are then combined by a pixel-wise maximum and merged with the broadcast complexity term, so confidence is raised inside the selected dynamic regions without adding spurious evidence to the static background. The ablation study confirms that adapting beats any fixed configuration: on fr3_walk_xyz the semantic-only and ROI-only threads bring ATE down from a baseline 0.166 m to 0.035 m and 0.045 m respectively, while the adaptive variant reaches 0.015 m, and it achieves the best result on all four walking sequences (0.015 m, 0.002 m, 0.016 m and 0.013 m) while capturing the most dynamic content at the highest mask confidence.

The complete pipeline is realized as a modular **ROS2** package layered on top of ORB-SLAM3 without any modification to the SLAM core. The filtered RGB and depth images are fed directly into the unmodified backend, a plug-and-play design that works with any SLAM system expecting RGB-D input. RGB, depth, and mask messages share identical, strictly monotonic timestamps and are published together using ROS2 message synchronization, guaranteeing that the correct mask is always applied to the correct frame pair.

<img src="/enabling/assets/theme/images/sar_slam.png" width="70%">

On the **TUM RGB-D benchmark**, the gap to the baseline is substantial. SAR-SLAM reduces ATE RMSE on fr3_walk_xyz from 0.404 m to 0.015 m (96%) and on fr3_walk_rpy from 0.492 m to 0.033 m (93%), with fr3_walk_half improving from 0.297 m to 0.026 m (91%). Against the state of the art it is competitive or better: on fr3_walk_rpy it records the lowest RMSE (0.033 m) and standard deviation (0.018 m) of all compared methods, outperforming NGD-SLAM, RED-SLAM and DIG-SLAM, and on fr3_walk_static it achieves the best RMSE (0.005 m) and SD (0.002 m). Importantly, robustness in dynamic scenes does not cost accuracy in static ones — on fr3_sit_static it matches DynaSLAM, RED-SLAM and DIG-SLAM at 0.006 m, and it improves the static fr2_xyz sequence from 0.018 m to 0.003 m. Relative Pose Error tells the same story locally, with the lowest translational drift across all dynamic walking sequences (0.015 m/s, 0.020 m/s and 0.031 m/s). Beyond the benchmark, the framework was deployed on a TIAGo PAL robot with an NVIDIA Jetson Orin for a six-minute indoor laboratory drive, sustaining 34.89 fps at a mean latency of 14.97 ms and a 92.5% real-time compliance rate against a 30 FPS deadline, using roughly 4.7 of the 12 ARM cores and a stable 761.51 MB of memory.

## Key Contributions

- **Verify-before-remove filtering**: Semantically detected objects are filtered only after RANSAC-based Homography confirms independent motion, so stationary people and objects are preserved as stable landmarks instead of being discarded
- **Continuous motion characterization**: The geometric thread recovers each object's motion direction and magnitude from the median outlier displacement, replacing the binary moving/not-moving decision used by most hybrid methods
- **Adaptive mode selection**: A scene-complexity score switches the system per frame between semantic-only, geometric-only and fused operation, trading accuracy against online computational cost
- **Plug-and-play ROS2 integration**: The full pipeline runs on top of an unmodified ORB-SLAM3 with synchronized RGB, depth and mask topics, making it compatible with existing navigation frameworks
- **Validated accuracy and real-time deployment**: Up to 96% ATE reduction over ORB-SLAM3 on TUM RGB-D, plus real-time operation at 34.89 fps on an embedded TIAGo/Jetson Orin platform

## Fulltext Access
[https://doi.org/10.3390/robotics15070136](https://doi.org/10.3390/robotics15070136)

## Citation (BibTeX)

{% raw %}
```bibtex
@article{altawil2026sarslam,
  author    = {Basheer Al-Tawil and Magnus Jung and Thorsten Hempel and Ayoub Al-Hamadi},
  title     = {{SAR-SLAM}: Semantic-Aware Recognition for Dynamic {SLAM} in Robotic Applications},
  journal   = {MDPI Robotics},
  volume    = {15},
  number    = {7},
  pages     = {136},
  year      = {2026},
  month     = jul,
  doi       = {10.3390/robotics15070136},
  url       = {https://doi.org/10.3390/robotics15070136}
}
```
{% endraw %}
