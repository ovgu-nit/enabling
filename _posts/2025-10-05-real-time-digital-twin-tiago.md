---
title: "A Real-Time Digital Twin Framework for the TIAGo Service Robot"
description: We present a real-time digital twin of the TIAGo service robot built in Unity, featuring authentic kinematic mirroring, real-time sensor fusion, a modular GUI, and procedurally generated virtual environments to enable safe reinforcement learning and autonomous robot development.
background: /assets/theme/images/dg_header.png
image: /assets/theme/images/digital_twin.png
author: "Malte Herrmann, Thorsten Hempel, Ayoub Al-Hamadi"
categories: [Publication, Conference, Digital Twin, Service Robots, Reinforcement Learning]
conference: "**IEEE SMC 2025** [[paper]](https://doi.org/10.1109/SMC58881.2025.11343553)"
tags: [IEEE SMC 2025, Conference, Digital Twin]
---

## A Real-Time Digital Twin Framework for the TIAGo Service Robot

The rapid development of humanoid robots has introduced new possibilities in automation, but also new risks. Unanticipated robot actions can cause damage to the environment or the robot itself, making it essential to have safe testing and development environments. This paper presents a Digital Twin Instance (DTI) of the TIAGo service robot by PAL Robotics, designed to replicate and monitor robotic operations in a virtual environment in real time.

The digital twin operates on three distinct levels. At the **Real2Sim** level, the DTI mirrors the movements of the physical robot and records visual data for downstream machine learning tasks. The **Sim2Real** level enables robot control through isomorphic teleoperation, where configurations defined in the simulation are sent back to the real robot. Finally, the **Sim Only** level allows all sensors and actuators to operate exclusively within the simulation, making it ideal for training neural networks via reinforcement learning (RL) without any real-world risk.

A central design decision is the use of the original TIAGo operating software (TIAGo-OS) running inside a virtual machine on the host PC. This ensures that path and trajectory planning calculations in the simulation are identical to those that would run on the physical robot, eliminating potential discrepancies from re-implemented kinematics. Unity serves as the simulation engine, chosen for its high-fidelity graphics, low latency, scalability for parallel RL training, and strong support for intuitive graphical user interfaces. The URDF-Importer and ROS-TCP-Connector tools connect Unity to the ROS ecosystem, enabling real-time communication between virtual and physical components.

The framework integrates the institute's full suite of ML ROS packages — including object detection, pose estimation, face detection, face recognition, head pose estimation, gaze estimation, and eye contact detection — allowing the digital twin to behave functionally like the real robot. A procedurally generated indoor environment, created with the Infinigen Indoors framework, serves as a proof-of-concept training scenario for RL and SLAM algorithm testing.

![](/enabling/assets/theme/images/digital_twin.png)


## Key Contributions

- **Three-level digital twin architecture**: Real2Sim for supervision, Sim2Real for teleoperation, and Sim Only for autonomous RL training
- **Authentic kinematics via original software**: The TIAGo-OS runs in a virtual machine, ensuring trajectory calculations are identical to the real robot
- **Modular GUI**: Enables seamless mode switching, ROS node management, sensor monitoring, and predefined motion execution
- **ML package integration**: Full suite of in-house perception algorithms operational within the simulation
- **Procedural environment generation**: Dynamic training scenarios via Infinigen Indoors for diverse and unpredictable conditions

## Fulltext Access
[https://doi.org/10.1109/SMC58881.2025.11343553](https://doi.org/10.1109/SMC58881.2025.11343553)

## Citation (BibTeX)

```bibtex
@inproceedings{herrmann2025tiago,
  author    = {Malte Herrmann and Thorsten Hempel and Ayoub Al-Hamadi},
  title     = {A Real-Time Digital Twin Framework for the {TIAGo} Service Robot},
  booktitle = {2025 IEEE International Conference on Systems, Man, and Cybernetics (SMC)},
  pages     = {6065--6068},
  year      = {2025},
  doi       = {10.1109/SMC58881.2025.11343553}
}
```
