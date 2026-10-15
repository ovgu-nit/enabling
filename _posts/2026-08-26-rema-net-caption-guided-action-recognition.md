---
title: "REMA-Net: Real-Time Human Action Recognition via Caption-Guided Dual-Stream Attention"
description: |
  REMA-Net is a lightweight dual-stream framework for real-time human action recognition that pairs RGB visual features with semantic embeddings derived from automatically generated image captions. Temporal order is injected through sinusoidal positional encoding, multi-head self-attention models inter-frame dependencies, and a confidence-gated cross-modal distillation strategy transfers semantic knowledge from the caption stream into the visual stream. The model reaches 96.8%, 73.0%, and 38.2% accuracy on UCF101, HMDB51, and HAA500 with only 13.01M parameters, and runs on an NVIDIA Jetson Orin mounted on a TIAGo robot at 35 FPS.
background: /assets/theme/images/rema_net.png
image: /assets/theme/images/rema_net.png
author: "Basheer Al-Tawil, Magnus Jung, Ayoub Al-Hamadi"
categories: [Publication, Preprint, Action Recognition, Human-Robot Interaction]
journal: "**SSRN Preprint 2026** [[preprint]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7357566)"
tags: [Preprint, SSRN, Action Recognition, Knowledge Distillation]
---

## REMA-Net: Real-Time Human Action Recognition via Caption-Guided Dual-Stream Attention

Human action recognition (HAR) is a prerequisite for robots that are expected to read human intentions and respond naturally. In human–robot interaction, however, the useful window for a reaction is short, and the hardware available on a mobile platform is modest. Most high-performing HAR models sit uncomfortably with both constraints: they depend on long video sequences or on expensive auxiliary modalities such as optical flow, skeleton extraction, or object detection, each of which adds parameters, latency, and failure modes. This work — currently available as a preprint on SSRN — asks how much of that machinery can be removed without giving up accuracy.

REMA-Net answers with a dual-stream design. The **visual stream** extracts frame-level features with a ResNet-18 backbone, augments them with sinusoidal positional encoding so that the temporal order of a clip is preserved, and passes the sequence through a lightweight multi-head self-attention module that reweights frames by their discriminative content before global temporal pooling. The **semantic stream** replaces motion-heavy modalities with language: frames are ranked by a Farnebäck optical-flow motion score, only the top 25% are captioned by a frozen BLIP model (the remainder inherit the nearest preceding caption), and the resulting captions are encoded by a frozen BERT-tiny text encoder into one embedding per frame. A second self-attention module refines these embeddings, and a learned confidence gate estimates how trustworthy each caption is before it is allowed to influence the prediction. Four candidate stream configurations were compared on UCF101: RGB alone reaches 93.50%, adding pose reaches 94.40% at 25.0 ms inference, adding pose and object detection reaches 94.60% at 28.0 ms — while RGB + caption reaches 96.80% at 1.82 ms, which is why it became the final architecture.

The two streams are tied together by **confidence-aware cross-modal knowledge distillation**. The caption stream acts as teacher and the RGB stream as student: both are supervised against the ground truth with cross-entropy, and the student additionally matches the teacher's temperature-softened distribution through a KL-divergence term (α = 0.3, T = 3), with the teacher treated as a stop-gradient target so that guidance flows in one direction only. The practical payoff is at deployment time, where the caption branch can be dropped entirely and only the distilled visual student is shipped — the semantic knowledge has already been absorbed into the RGB weights. An ablation on the official HMDB51 test split (n = 1,530) confirms that each component earns its place: removing positional encoding costs 2.79 pp, removing distillation 2.50 pp, removing self-attention 2.12 pp, the confidence gate 1.80 pp, and late fusion 1.20 pp.

Across the three benchmarks REMA-Net reaches **96.8% on UCF101, 73.0% on HMDB51, and 38.2% on HAA500** using 20 input frames, 13.01M parameters, and 2.5 GFLOPs — compared against baselines requiring up to 732M parameters and roughly 65 GFLOPs. The distilled visual-only variant runs at 120 FPS on a desktop GPU. On embedded hardware, the model was benchmarked on an **NVIDIA Jetson Orin mounted on a TIAGo robot**, subscribing to the robot's onboard camera over a live ROS2 topic: the visual-only distilled configuration averages **352.6 ms latency at 35.0 FPS using 322.0 MB of GPU memory**, whereas the multimodal hybrid with on-device BLIP captioning is substantially slower at 861.0 ms and 12.0 FPS while consuming 1283.7 MB. Both held a single stable prediction across the full 60-second session with zero label switches. The authors are explicit about scope: this is a real-time perception benchmark under live sensing, not a closed-loop control or HRI user study, and the lower HAA500 figure reflects the genuine difficulty of fine-grained recognition at 500-class scale, where BLIP captions become less discriminative.

<img src="/enabling/assets/theme/images/rema_net.png" width="70%">

## Key Contributions

- **Lightweight dual-stream framework**: REMA-Net fuses RGB visual features with caption-derived semantic embeddings, reaching 96.8% on UCF101 with only 13.01M parameters and 2.5 GFLOPs
- **Attention-based temporal modeling**: Sinusoidal positional encoding combined with multi-head self-attention captures inter-frame dependencies without 3D convolutions or optical flow
- **Confidence-aware cross-modal distillation**: A confidence-gated teacher–student scheme transfers semantic knowledge from the caption stream to the visual stream, so only the compact RGB student is deployed
- **Semantics instead of sensor-heavy modalities**: Captioning just the top 25% most motion-informative frames outperforms pose and object streams while cutting inference latency from 28.0 ms to 1.82 ms
- **Embedded robotic validation**: Benchmarked on an NVIDIA Jetson Orin aboard a TIAGo robot over a live ROS2 camera stream, running at 35.0 FPS with 322.0 MB GPU memory, leaving headroom for concurrent SLAM and navigation

## Fulltext Access
[https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7357566](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7357566)

## Citation (BibTeX)

{% raw %}
```bibtex
@misc{altawil2026remanet,
  author       = {Basheer Al-Tawil and Magnus Jung and Ayoub Al-Hamadi},
  title        = {{REMA-Net}: Real-Time Human Action Recognition via Caption-Guided Dual-Stream Attention},
  year         = {2026},
  howpublished = {SSRN preprint, abstract id 7357566 (not peer reviewed)},
  note         = {Preprint},
  url          = {https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7357566}
}
```
{% endraw %}
