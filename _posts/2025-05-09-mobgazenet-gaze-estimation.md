---
title: "MobGazeNet: Robust Gaze Estimation Mobile Network Based on Progressive Attention Mechanisms"
description: |
  An efficient and lightweight network for gaze estimation that leverages progressive attention mechanisms to emphasize crucial eye features while maintaining computational efficiency for mobile and embedded systems.
background: /assets/theme/images/mobgazenet.png
author: []
categories: [Publication, Journal Paper, Machine Vision and Applications, Gaze Estimation]
---

## MobGazeNet: Robust Gaze Estimation Mobile Network Based on Progressive Attention Mechanisms

We introduce MobGazeNet, an efficient and lightweight network that leverages a progressive combination of attention mechanisms, including squeeze-and-excitation, convolutional block attention module, and coordinate attention. The combination of attention mechanisms helps to emphasize crucial eye features and allows the model to consider both local and global spatial relationships without increasing computational overhead. 

Furthermore, we introduce the rotation matrix formalism for gaze ground truth to avoid discontinuity and ambiguity in spherical angle representation. Building upon this, we propose a continuous 6D rotation matrix representation to enable efficient and reliable direct regression which we further enhance with a geodesic-based loss. 

Our proposed model surpasses current state-of-the-art methods in both performance and efficiency, showcasing its superior capability in gaze estimation across three popular datasets collected in unconstrained settings.

## Fulltext Access
[https://doi.org/10.1007/s00138-025-01690-z](https://doi.org/10.1007/s00138-025-01690-z)

## Code
[https://github.com/Ahmednull/MobGazeNet](https://github.com/Ahmednull/MobGazeNet)

## Citation (BibTeX)

```bibtex
@article{abdelrahman2025mobgazenet,
  author    = {Ahmed A. Abdelrahman and Thorsten Hempel and Aly Khalifa and Dominykas Strazdas and Ayoub Al-Hamadi},
  title     = {Mobgazenet: robust gaze estimation mobile network based on progressive attention mechanisms},
  journal   = {Machine Vision and Applications},
  volume    = {36},
  number    = {3},
  pages     = {76},
  year      = {2025},
  month     = may,
  doi       = {10.1007/s00138-025-01690-z},
  url       = {https://doi.org/10.1007/s00138-025-01690-z}
}
```
