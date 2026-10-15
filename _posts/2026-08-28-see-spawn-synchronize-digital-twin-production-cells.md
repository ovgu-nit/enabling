---
title: "See, Spawn, Synchronize: A Digital Twin Pipeline for Smart Production Cells"
description: |
  We present a digital twin of a smart production cell that synchronizes objects bidirectionally between a real and a virtual workspace using only a single robot-mounted RGB-D camera. A fine-tuned YOLO11 detector locates tools and items, estimates their spatial position, and spawns them in Unity relative to the robot. Experiments across four scanning conditions show a mean planar spawn deviation of 5.82 mm at 0.1 m/s and 0.7 m camera height, and changes planned in the simulation are executed physically by the robot, including stacking cubes into a pyramid.
background: /assets/theme/images/see_spawn_synchronize.png
image: /assets/theme/images/see_spawn_synchronize.png
author: "Malte Herrmann, Dominykas Strazdas, Ayoub Al-Hamadi"
categories: [Publication, Journal Paper, Digital Twin, Object Detection, Industry 5.0]
journal: "**MDPI Machines 2026** [[paper]](https://doi.org/10.3390/machines14090972)"
tags: [MDPI Machines 2026, Journal Paper, Digital Twin, Human-Robot Collaboration]
---

## See, Spawn, Synchronize: A Digital Twin Pipeline for Smart Production Cells

With Industry 5.0, human–robot collaboration has moved to the center of attention, and industrial workspaces have become highly dynamic. Digital twins can plan robot motions remotely and prevent collisions with humans, other robots, or the environment — but only if the digital representation keeps up with the real world. Static replicas quickly become obsolete once tools and products are moved around. This paper closes that gap with a digital twin of a smart production cell that synchronizes objects bidirectionally between the real and the virtual workspace using nothing more than a single RGB-D camera mounted on the robot's end effector.

The real cell consists of two Universal Robots arms — a UR5e on a linear axis with an OnRobot RG6 gripper and a UR10e with a 2FR14 gripper — each carrying an Intel RealSense D435 camera; the experiments use the UR10e. The table acts as the base of the cell and carries an M6 hole grid with 2.5 cm spacing that serves as ground truth. 3D-printed 5 cm cubes with a letter or number on each face stand in for tools and products, and 3D-printed cube holders act as fiducial markers. The digital counterpart is built in Unity from the manufacturer's URDF files, scaled 1 unit to 1 m, and connected to ROS 2 through a ROS-TCP-Endpoint, so the virtual arm mirrors the real joint states in real time.

The pipeline runs in three stages. In the **see** stage, a fine-tuned Ultralytics YOLO11 detector returns bounding box, rotation, and the top-side letter of each cube, while the aligned depth image — sampled at the intersection of the bounding box diagonals and corrected by the 2.5 cm half-cube offset — provides the distance. In the **spawn** stage, a positioning module converts pixel coordinates to world coordinates using the intrinsic camera parameters and Unity's kinematic transforms, and creates the cube relative to the robot base; a tracking filter that requires seven consecutive frames suppresses duplicate spawns. In the **synchronize** stage, the user drags the virtual cubes to arbitrary target positions with mouse, touch, or gamepad, with a ghost version indicating the goal. On confirmation, a task execution planner sorts the cubes by z-height, computes approach, grasp, translation, and release trajectories via MoveIt with the table and obstacles registered for collision avoidance, and the real robot carries out the plan.

The first experiment quantifies spawn accuracy by scanning the workspace orthogonally at constant speed. Four conditions combining camera heights of 0.6 m and 0.7 m with velocities of 0.1, 0.15, and 0.2 m/s were each run 95 times, yielding 1805 cube placements per condition. The best configuration — 0.7 m at 0.1 m/s — reaches a mean planar error of 5.82 mm (standard deviation 2.24 mm, P95 10.02 mm) with a constant height bias of −0.54 mm. Doubling the scan speed to 0.2 m/s nearly doubles the mean planar error to 10.91 mm, an increase of 89.6% that is statistically significant across all pairwise comparisons (p < 0.001, Mann–Whitney U test), and inflates the P95 error to 21.70 mm while losing 2.1% of detections. Per-letter errors range from 5.98 mm for J to 8.12 mm for X. YOLO inference and the subsequent computations fit within a single camera frame of 33 ms, so the perception pipeline runs at camera rate; the seven-frame stability filter adds up to roughly 231 ms during scanning.

<img src="/enabling/assets/theme/images/see_spawn_synchronize.png" width="70%">

The second experiment validates the simulation-to-reality direction. Since the gripper opens to 55 mm and the cubes measure 50 mm, a cube is directly graspable only if its X-axis error stays within ±5 mm. At 0.7 m and 0.1 m/s, the raw grippability rate is 48.4%; compensating the systematic X-axis drift measured in the first experiment raises it to 94.7%, and snapping the cubes to the known hole grid brings it to 100%. This shows that the dominant failure source is not random detection noise but a measurable, correctable drift along the scan direction. As a qualitative proof of concept, a 4-3-2-1 pyramid was planned entirely inside the digital twin after a single workspace scan and built by the real robot with a 100% gripping rate for both the real and the simulated arm.

## Key Contributions

- **Single-camera bidirectional synchronization**: Real and virtual workspaces are kept in sync with only one robot-mounted RGB-D camera — no external cameras, fiducial markers on the objects, or manual scene authoring
- **See–spawn–synchronize pipeline**: A fine-tuned YOLO11 detector, a coordinate-transforming spawner, and a MoveIt-based execution planner form a closed loop from real workspace to Unity and back
- **Quantified scan accuracy**: 5.82 mm mean planar error at 0.1 m/s and 0.7 m height versus 10.91 mm at 0.2 m/s across 95 trials and 1805 placements per condition, establishing the trade-off between scan speed and placement precision
- **Systematic bias correction and grid alignment**: Compensating the measured X-axis drift lifts grippability from 48.4% to 94.7%, and a priori grid knowledge pushes it to 100%
- **Validated sim-to-real transfer**: Drag-and-drop planning in the digital twin was executed physically, including a 4-3-2-1 pyramid stacked with a 100% gripping rate, with the twin usable as digital shadow, motion planning tool, or hardware-free RL environment

## Fulltext Access
[https://doi.org/10.3390/machines14090972](https://doi.org/10.3390/machines14090972)

## Citation (BibTeX)

```bibtex
@article{herrmann2026see,
  author    = {Malte Herrmann and Dominykas Strazdas and Ayoub Al-Hamadi},
  title     = {See, Spawn, Synchronize: A Digital Twin Pipeline for Smart Production Cells},
  journal   = {MDPI Machines},
  volume    = {14},
  number    = {9},
  pages     = {972},
  year      = {2026},
  month     = aug,
  doi       = {10.3390/machines14090972},
  url       = {https://doi.org/10.3390/machines14090972}
}
```
