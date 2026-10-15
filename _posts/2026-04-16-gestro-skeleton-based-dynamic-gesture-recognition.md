---
title: "GESTRO: Skeleton-Based Dynamic Gesture Recognition for Robot Teleoperation"
description: |
  We introduce GESTRO, a dataset of 11 dynamic gestures for the intuitive teleoperation of mobile robots, comprising 3,300 samples recorded from ten participants. Based on upper-body landmarks, we propose a bidirectional LSTM with an attention mechanism that reaches 98% accuracy and outperforms GRU, RNN, Transformer and CNN baselines. The model is deployed on the humanoid robot TIAGo, demonstrating robust real-time gesture recognition in a realistic human-robot interaction setting.
background: /assets/theme/images/gestro.png
image: /assets/theme/images/gestro.png
author: "Thorsten Hempel, Magnus Jung, Arman Ahmed Khan, Ayoub Al-Hamadi"
categories: [Publication, Journal Paper, Gesture Recognition, Human-Robot Interaction, Robot Teleoperation]
journal: "**Journal of Intelligent & Robotic Systems 2026** [[paper]](https://doi.org/10.1007/s10846-026-02395-9) [[code]](https://github.com/thohemp/gestro)"
tags: [JINT 2026, Journal Paper, Gesture Recognition, Teleoperation]
---

## GESTRO: Skeleton-Based Dynamic Gesture Recognition for Robot Teleoperation

Efficient human-robot interaction increasingly depends on a robot's ability to understand and act on human gestures, particularly in industrial settings where operators need to command mobile platforms hands-free. Vision-based gesture recognition is challenging under real-world conditions: varying lighting, background clutter, occlusions and user-specific variations all place heavy demands on the recognition system. Static gesture recognition, which classifies a single frame, discards the temporal dimension that distinguishes many natural commands from one another. This work addresses dynamic gesture recognition for mobile robots with limited onboard hardware capacity.

Because no existing dataset was tailored to the intuitive commanding of mobile robots, we introduce **GESTRO**. Ten fundamental teleoperation commands were identified — Follow, Go to Base, Idle, Login, Logout, Move Backward, Move Forward, Stop, Turn Left and Turn Right — complemented by an eleventh *Unknown* rest class that captures non-gestures and movements not directed at the robot, reducing false positives. Ten participants varying in race, age, gender, stature and background each performed every gesture 30 times, recorded by a laptop camera at 800 x 600 pixels. Each atomic gesture is encapsulated in 30 frames, equal to 1.5 seconds, yielding 300 samples per class and 3,300 samples in total — roughly double the size of comparable teleoperation datasets and more than seven times the 450 samples of the closest related set.

<img src="/enabling/assets/theme/images/gestro.png" width="70%">

Preprocessing extracts human pose landmarks with a top-down heatmap-based ResNet152 estimator trained on COCO-WholeBody, which predicts 133 2D whole-body landmarks. From these, the 54 upper-body keypoints covering face, arms and hands are retained; the remaining 79 are omitted as they are not involved in the chosen gestures. Landmarks are normalized to the frame size and then standardized relative to the nose keypoint, making the representation agnostic to the person's position in the image plane. The recognition model consists of two stacked bidirectional LSTM layers (512 hidden units each, with normalization and dropout at p = 0.5), followed by an eight-head attention layer that weights the most informative time steps into a context vector, and a dense softmax layer over the 11 classes. Training used the Adam optimizer at a learning rate of 0.0001 for 30 epochs, with temporal masking and global scaling (factor 0.3 to 1.3) as augmentations to simulate incomplete executions and varying subject distance.

Evaluated with a subject-disjoint split (eight subjects for training, two for testing), **GESTRO-LSTM reaches 0.98 across accuracy, recall, precision and F1**, outperforming the Transformer and plain Bi-LSTM baselines (both 0.96 F1), GRU (0.85), RNN (0.85) and the image-based ResNet50 and ResNet18 variants (0.91 and 0.90). Removing the attention layer costs 2% F1 and 3% accuracy. A one-vs-all protocol, training on nine subjects and testing on the tenth, averages 0.97 accuracy and 0.98 F1, confirming that performance is stable across individuals. Class-wise results are near-perfect except for the *Idle* class at 0.85 precision, which contains no movement and therefore absorbs ambiguous samples. A sequence-length analysis shows that the model discriminates gestures reliably from very short sequences, while the Transformer needs considerably longer ones — direct evidence that temporal dynamics, not static poses, carry the discriminative signal.

Finally, both GESTRO-LSTM and the Transformer were deployed on the humanoid robot TIAGo from PAL Robotics. Frames were processed without a queue, so that any frame arriving faster than the system could handle was skipped — a setup that guarantees real-time behaviour but stresses temporal robustness. On the robot's Jetson AGX Orin, images were published at 29.94 FPS, with the pose estimation node running at 6.972 Hz and the gesture recognition node at 4.81 Hz. The initial 5.528 s detection latency reflects the 30-frame buffer the LSTM must fill; the steady-state latency from the first image to the first gesture change was 2.519 s. Under these conditions the Transformer showed greater robustness problems than its dataset scores suggested, whereas GESTRO-LSTM remained stable, recognized the safety-critical *Stop* gesture immediately, and used the *Unknown* class effectively to absorb outliers.

## Key Contributions

- **GESTRO dataset**: 3,300 dynamic samples across 11 teleoperation gesture classes, recorded from ten diverse participants in 30-frame sequences, publicly released together with training, testing and evaluation scripts at [github.com/thohemp/gestro](https://github.com/thohemp/gestro)
- **Landmark-based efficiency**: Only 54 upper-body landmarks from a whole-body pose estimator are used, normalized and nose-centered, keeping the input compact enough for mobile robot hardware
- **BiLSTM with attention**: Two bidirectional LSTM layers plus an eight-head attention layer achieve 0.98 accuracy, precision, recall and F1, beating Transformer, GRU, RNN and CNN baselines
- **Evidence for temporal dynamics**: Sequence-length and one-vs-all analyses show that motion over time, not static posture, drives reliable classification, with average 0.97 accuracy across all held-out subjects
- **Real robot deployment**: Implementation on the TIAGo humanoid with a Jetson AGX Orin demonstrates real-time operation, immediate recognition of the safety-critical Stop gesture, and robust rejection of unknown movements

## Fulltext Access
[https://doi.org/10.1007/s10846-026-02395-9](https://doi.org/10.1007/s10846-026-02395-9)

## Citation (BibTeX)

{% raw %}
```bibtex
@article{hempel2026gestro,
  author    = {Thorsten Hempel and Magnus Jung and Arman Ahmed Khan and Ayoub Al-Hamadi},
  title     = {{GESTRO}: Skeleton-Based Dynamic Gesture Recognition for Robot Teleoperation},
  journal   = {Journal of Intelligent \& Robotic Systems},
  volume    = {112},
  number    = {2},
  pages     = {51},
  year      = {2026},
  month     = apr,
  doi       = {10.1007/s10846-026-02395-9},
  url       = {https://doi.org/10.1007/s10846-026-02395-9}
}
```
{% endraw %}
