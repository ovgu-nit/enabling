---
title: "Automated 3D Dataset Generation for Arbitrary Objects"
description: |
  An end-to-end pipeline that automates all aspects of 3D dataset generation by leveraging Radiance Fields for high-quality 3D modeling and synthetic dataset generation, enabling training of pose estimation networks for arbitrary objects.
background: /assets/theme/images/paul_access.png
author: []
categories: [Publication, Journal Paper, IEEE Access, 3D Dataset Generation, Pose Estimation]
---

## Automated 3D Dataset Generation for Arbitrary Objects

6D pose estimation is a cornerstone of various autonomous systems, including mobile robots and self-driving cars, because it enables fundamental capabilities such as collision-free navigation and object grasping. However, training performant pose estimation models requires large and precisely annotated datasets. Due to the complex, expensive, and time-consuming capturing and annotation process, only few 3D datasets are available, which are also often limited in class diversity.

To provide practitioners with a tool capable of generating 3D datasets for arbitrary objects, we propose an end-to-end pipeline that automates all aspects of dataset generation. By leveraging the implicit modeling capabilities of Radiance Fields, our pipeline constructs high-quality 3D models for arbitrarily complex objects. These 3D models serve as input for a synthetic dataset generator.

A comprehensive evaluation across multiple objects demonstrates that our pipeline is fast, easy to use, and highly automated. Furthermore, we show that pose estimation networks trained on the generated datasets achieve strong performance in typical application scenarios.

## Key Contributions

- **End-to-end automation**: An automated dataset generation pipeline from arbitrary objects to diverse, precisely annotated 3D datasets
- **Neural rendering-based 3D modeling**: Leverages Radiance Fields to create high-quality 3D models without expensive equipment
- **Practical validation**: Demonstrates that networks trained on generated datasets achieve reliable pose estimation performance

## Fulltext Access
[https://doi.org/10.1109/ACCESS.2025.3617952](https://doi.org/10.1109/ACCESS.2025.3617952)

## Citation (BibTeX)

```bibtex
@article{schulz2025automated,
  author    = {Paul Schulz and Thorsten Hempel and Ayoub Al-Hamadi},
  title     = {Automated 3D Dataset Generation for Arbitrary Objects},
  journal   = {IEEE Access},
  volume    = {13},
  pages     = {173813--173828},
  year      = {2025},
  month     = oct,
  doi       = {10.1109/ACCESS.2025.3617952},
  url       = {https://doi.org/10.1109/ACCESS.2025.3617952}
}
```
