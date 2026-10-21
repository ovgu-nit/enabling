---
title: "Vision on the Warehouse Floor: Perceptive HRI for Autonomous Forklifts"
description: |
  We present an integrated vision system for autonomous forklifts that combines RGB-only 6D pallet pose estimation with gesture- and face-based human–robot interaction. The pose estimator is trained exclusively on a synthetic dataset of 109,204 domain-randomized images and reaches an average AUC of 0.484 on real industrial sequences, compared to 0.085 for the DOPE baseline. A safety-by-design protocol keeps the Stop command globally accessible regardless of authorization state. All modules run on-board on an NVIDIA Jetson AGX Orin in an active intralogistics facility.
background: /assets/theme/images/warehouse_forklift.png
image: /assets/theme/images/warehouse_forklift.png
author: "Magnus Jung, Thorsten Hempel, Paul Schulz, Ayoub Al-Hamadi"
categories: [Publication, Journal Paper, Autonomous Forklifts, 6D Pose Estimation, Human-Robot Interaction]
doi: "10.3390/robotics15100191"
journal: "**MDPI Robotics 2026** [[paper]](https://doi.org/10.3390/robotics15100191)"
tags: [MDPI Robotics 2026, Journal Paper, Intralogistics, Pallet Detection, Gesture Recognition]
---

## Vision on the Warehouse Floor: Perceptive HRI for Autonomous Forklifts

The transformation of industrial intralogistics toward Industry 4.0 and 5.0 has made autonomous mobile robots indispensable for flexible material handling, and autonomous forklifts in particular bridge the gap between automated storage and dynamic production environments. Yet traditional systems still rely on rigid markers or laser scanners that struggle with the variability of real warehouses: diverse pallet orientations, fluctuating lighting, and human workers moving through the same aisles. Two capabilities are required for seamless integration into such shared workspaces — robust perception for load handling and intuitive, secure modalities for human–robot interaction — and they have so far been studied almost exclusively in isolation. This paper, developed in an industry–academia collaboration, addresses both on a single vehicle operating in an active industrial facility.

At the core of the perception side is an RGB-only 6D pallet pose estimation pipeline built on the Deep Object Pose Estimation (DOPE) paradigm, with a ViT-B/16 backbone followed by a four-level hourglass network for each prediction branch. The network predicts nine belief maps for the eight projected bounding-box corners and the object centroid, plus sixteen affinity maps that associate corner peaks with individual pallet hypotheses, after which a PnP solver recovers the 6D pose from the known Euro pallet dimensions and the camera intrinsics. To overcome the scarcity of annotated industrial data, the model is trained **exclusively on synthetic data**: a dataset of 109,204 domain-randomized images generated with NVIDIA Omniverse Replicator, covering close- and long-range scenes, single- and multi-object configurations, and randomized poses, viewpoints, lighting, textures, and distractor objects such as boxes and barrels. The result is a substantial reduction in the sim-to-real gap. On three dedicated real-world test sequences recorded in the facility, the method achieves an average AUC@0.5 m of **0.484 against 0.085 for the DOPE baseline** — a more than five-fold improvement — while performing comparably to DOPE on synthetic validation data.

Interaction is handled by two complementary modules. The gesture recognizer is built on the GESTRO framework, whose dataset comprises 3300 samples across 11 classes recorded from 10 subjects. For each frame, 54 upper-body skeletal landmarks are extracted with a ResNet152-based pose estimator and normalized relative to the nose keypoint, making the system invariant to the operator's distance and position; sequences of 30 frames (a 1.5-second window) are then classified by a BiLSTM with multi-head attention. The model reaches an accuracy, precision, recall, and F1-score of **0.98** in the cross-subject split and 0.97 in leave-one-out validation across all ten subjects. On the forklift, the vocabulary is reduced to four commands: *Login* starts an interaction session and triggers operator identification, *Logout* ends it, *Follow* activates person-following behavior, and *Stop* halts the vehicle. The second module performs face recognition with role-based access control, using a FaceNet-based architecture that generates 128-dimensional embeddings. Crucially, the local database stores **three viewpoint-specific embeddings per enrolled person** — front, left, and right, each accepted only within roughly ±10° of the target head orientation — so that an operator approaching the vehicle from the side is still reliably identified. SORT tracking performs full re-identification every fifth frame and bridges the gaps with Kalman predictions, raising the F-score on ChokePoint from 0.81 to 0.94 and the online recognition rate from 76% to 94%.

Safety is treated as a global state rather than a privilege. The system remains passive until a deliberate *Login* gesture is detected — an "intentional handshake" that precedes biometric verification and prevents everyday warehouse movements from being misread as commands — and only then does a database lookup unlock high-level functions according to the identified user's role (Operator, Admin, or Maintenance). The *Stop* gesture, however, is explicitly excluded from role-based access control: it requires no prior login and remains available to **every person** in the vehicle's vicinity at all times, complementing rather than replacing the platform's built-in safety functions. This design is reflected in the hardware layout as well: the camera is mounted on the operator-facing rear of the vehicle to preserve an unobstructed line of sight to human workers throughout the maneuver, which means the forklift localizes the pallet from a frontal standoff position, rotates 180°, and completes the fork insertion in reverse using SLAM-based localization.

The complete system was deployed and evaluated on the vehicle itself — a Martin Systems platform built around an Omron mobile base — with all inference running locally on an **NVIDIA Jetson AGX Orin** without cloud connectivity. The gesture pipeline operates at 4.81 Hz with a steady-state command latency of 2.52 s after the initial activation window, face recognition runs at approximately 35 FPS with 6.7 ms per-frame latency, and the pallet detection module delivers end-to-end poses in 210 ms (5.0 FPS). An end-to-end demonstration in the active facility confirmed the full operational chain from gesture-based login and operator identification through pose estimation to autonomous fork engagement, with the *Stop* gesture reliably forwarded to the navigation stack irrespective of whether the gesturing person was registered. Remaining limitations are discussed openly: the final insertion is executed open-loop, perception degrades under extreme over- or underexposure, and the model trained on Euro pallet geometry cannot yet distinguish other pallet standards.

<img src="/enabling/assets/theme/images/warehouse_forklift.png" width="70%">

## Key Contributions

- **RGB-only 6D pallet pose estimation trained purely on synthetic data**: A ViT-B/16 and hourglass architecture trained on 109,204 domain-randomized images achieves an average AUC of 0.484 on real industrial sequences versus 0.085 for the DOPE baseline, drastically reducing the sim-to-real gap without any depth input
- **Skeleton-based gesture interface**: 54 upper-body landmarks per frame over a 30-frame window, classified by a BiLSTM with attention at 0.98 accuracy, with a Login / Logout / Follow / Stop vocabulary for touchless forklift control
- **Multi-perspective face recognition with role management**: Front, left, and right embeddings per enrolled operator plus SORT tracking raise the online recognition rate from 76% to 94% and gate high-level commands by permission level
- **Safety-by-design command arbitration**: An intentional Login handshake precedes biometric verification, while the Stop command is excluded from access control and remains available to any person at any time
- **On-vehicle evaluation in an active facility**: All three modules run concurrently on an NVIDIA Jetson AGX Orin on a real autonomous forklift, covering the full chain from gesture login to autonomous pallet engagement in a shared human–robot workspace

## Fulltext Access
[https://doi.org/10.3390/robotics15100191](https://doi.org/10.3390/robotics15100191)

## Citation (BibTeX)

```bibtex
@article{jung2026vision,
  author    = {Magnus Jung and Thorsten Hempel and Paul Schulz and Ayoub Al-Hamadi},
  title     = {Vision on the Warehouse Floor: Perceptive {HRI} for Autonomous Forklifts},
  journal   = {MDPI Robotics},
  volume    = {15},
  number    = {10},
  pages     = {191},
  year      = {2026},
  month     = sep,
  doi       = {10.3390/robotics15100191},
  url       = {https://doi.org/10.3390/robotics15100191}
}
```
