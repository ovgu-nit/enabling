---
title: "Gaze Matters: Eye Contact Detection in Unscripted Human-Robot Interaction Scenarios"
description: |
  We conducted a user study in a realistic collaborative human-robot interaction scenario with unscripted tasks to evaluate how well current eye contact detection models perform from the robot's own perspective. A new dataset of 5,888 manually annotated visual engagement instances was created from the robot's on-board camera. Models trained on our NITEC dataset clearly outperform the baselines with an AUC of 0.74, underlining the importance of diverse, unconstrained training data for robust eye contact recognition in HRI.
background: /assets/theme/images/gaze_matters.png
image: /assets/theme/images/gaze_matters.png
author: "Thorsten Hempel, Magnus Jung, Dominykas Strazdas, Ayoub Al-Hamadi"
categories: [Publication, Conference Paper, Eye Contact Detection, Human-Robot Interaction, User Study]
conference: "**IEEE SMC 2025** [[paper]](https://doi.org/10.1109/SMC58881.2025.11343353)"
tags: [IEEE SMC 2025, Conference, Eye Contact, HRI]
---

## Gaze Matters: Eye Contact Detection in Unscripted Human-Robot Interaction Scenarios

Eye contact is one of the key mechanisms of non-verbal communication: it signals the intent to initiate communication, regulates turn-taking, and helps establish joint attention. These effects carry over to human-robot interaction, where mutual gaze increases a robot's perceived likability and human-likeness. Yet eye contact detection *from the robot's perspective* remains largely underexplored. Most existing approaches are evaluated on simulated data, on recordings from constrained laboratory settings, or on isolated images that are not drawn from actual human-robot interaction at all — and therefore fail to reflect the dynamic and unpredictable nature of real encounters.

To close this gap, we conducted a user study in a realistic collaborative setting with the humanoid service robot TIAGo (PAL Robotics). Nine participants (5 male, 4 female, aged 20 to 39) were asked to engage the robot verbally and request the handover of a cube placed on a table behind it. The robot turned away, grasped the object, turned back, and delivered it, after which the participant naturally disengaged. The session followed a Wizard of Oz protocol to keep interaction patterns consistent while preserving the illusion of autonomy. Crucially, participants were never told that the study was about gaze — ensuring that their eye contact behavior remained unaffected and natural.

All data was recorded through the robot's internal ORBBEC Astra S camera at 640×480 pixels and 30 fps using RGB only, yielding 24,682 frames in total. After filtering out segments in which the participant was reading on-screen instructions or the robot was acting independently, the final sequences range from 438 to 1,200 frames and amount to **5,888 hand-annotated data points**. The eye contact ratio per sequence varies widely, from 6.4% up to 53.0%, with a mean of 24.9% across all subjects — clear evidence that participants spontaneously engaged in eye contact with the robot even though they were never instructed to do so.

We evaluated three models on this real-world test set: our previously published NITEC model with a ResNet18 backbone, and the identical architecture trained separately on the OFDIW and DEEPEC datasets. NITEC achieves the highest ROC curve overall and the best AUC for every single subject, with per-subject values between 0.65 and 0.93 and an overall AUC of 0.74, compared to 0.53 for DEEPEC and 0.52 for OFDIW — both barely better than random guessing, with several per-subject scores falling below 0.5. The advantage is most pronounced in difficult sequences: for subject 8, who approaches from the side and stays very close to the robot, NITEC reaches an average precision of 0.35 while both baselines collapse to 0.04. A time-series analysis with a sliding window of 20 frames shows that NITEC tracks the ground-truth eye contact dynamics closely for most subjects, while subject 9 — affected by challenging lighting and worn glasses — remains the hardest case, with consistently low confidence scores.

<img src="/enabling/assets/theme/images/gaze_matters.png" width="70%">

The qualitative samples captured from the robot's point of view illustrate why this setting is demanding: partially occluded and side-facing heads, varying proximity, and strong backlighting from the large TV screen that served as the instruction display throughout the sessions. Despite these conditions, the NITEC model predicts the correct eye contact status, indicated by the green (eye contact) and red (no eye contact) overlays on the faces.

## Key Contributions

- **Unscripted HRI user study**: A realistic, task-based collaboration with the TIAGo robot in which participants were unaware that gaze was being studied, yielding authentic interaction behavior
- **New ego-perspective dataset**: 5,888 hand-annotated data points recorded from the robot's on-board camera, filtered from 24,682 raw frames across nine participants
- **Evidence that eye contact is intuitive in HRI**: A mean eye contact ratio of 24.9% without any instruction to look at the robot, confirming its role in human-centric robot design
- **Benchmark of state-of-the-art detectors**: NITEC reaches an overall AUC of 0.74 versus 0.53 (DEEPEC) and 0.52 (OFDIW), and wins on every individual sequence
- **Importance of unconstrained training data**: The performance gap widens exactly in the hardest sequences (e.g. AP 0.35 vs. 0.04 for subject 8), demonstrating that diverse training data drives real-world robustness

## Fulltext Access
[https://doi.org/10.1109/SMC58881.2025.11343353](https://doi.org/10.1109/SMC58881.2025.11343353)

## Citation (BibTeX)

```bibtex
@inproceedings{hempel2025gaze,
  author    = {Thorsten Hempel and Magnus Jung and Dominykas Strazdas and Ayoub Al-Hamadi},
  title     = {Gaze Matters: Eye Contact Detection in Unscripted Human-Robot Interaction Scenarios},
  booktitle = {2025 IEEE International Conference on Systems, Man, and Cybernetics (SMC)},
  pages     = {7312--7317},
  year      = {2025},
  month     = oct,
  doi       = {10.1109/SMC58881.2025.11343353}
}
```
