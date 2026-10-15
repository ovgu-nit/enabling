---
title: "Robot System Assistant (RoSA): evaluation of touch and speech input modalities for on-site HRI and telerobotics"
description: |
  RoSA 3 extends the Robot System Assistant framework with a React-based touchscreen interface and a locally running speech pipeline that work identically on-site and remotely. A user study with ten participants compared both modalities on an industrial UR5e arm and the humanoid robot Ari. Touch proved faster and more reliable, while speech was preferred for free, exploratory interaction — a trade-off that transfers directly to telerobotic supervision.
background: /assets/theme/images/rosa_touch_speech.png
image: /assets/theme/images/rosa_touch_speech.png
author: "Dominykas Strazdas, Matthias Busch, Rijin Shaji, Ingo Siegert, Ayoub Al-Hamadi"
categories: [Publication, Journal Paper, Human-Robot Interaction, Telerobotics, Multimodal Interaction]
journal: "**Frontiers in Robotics and AI 2025** [[paper]](https://doi.org/10.3389/frobt.2025.1561188)"
tags: [Frontiers 2025, Journal Paper, Human-Robot Interaction, Telerobotics]
---

## Robot System Assistant (RoSA): evaluation of touch and speech input modalities for on-site HRI and telerobotics

As robot autonomy increases, the operator's role shifts towards that of a supervisor who oversees and directs task-oriented robots — either standing next to them on the shop floor or connected from somewhere else entirely. That hybrid working style only becomes practical if the same interaction modalities, and the same feedback, are available in both situations. This paper addresses that requirement by evaluating touch and speech input within the third iteration of the Robot System Assistant (RoSA) framework, covering on-site human-robot interaction and telerobotics through one shared interface.

RoSA 3 builds on earlier versions — RoSA 1 as a Wizard-of-Oz study and RoSA 2 as the first fully operational speech-and-gesture system — and adds a touchscreen modality plus a second robot. The system drives **Rosa**, a stationary industrial UR5e fitted with an OnRobot RG6 gripper that manipulates letter cubes, and **Ari**, a wheeled humanoid from PAL Robotics with a 10-inch chest touchscreen, a built-in RGB camera and two RGB-D cameras. All modules run as ROS 1 (Noetic) nodes feeding a central *Commander*, which replaces the first-in-first-out handling of earlier versions with a "buffered multimodality" scheme: it progressively collects partial messages from any modality until a complete `RobotAction` can be assembled, eliminating the race conditions that limited RoSA 2. The touch interface is a React web app connected through roslibjs and rosbridge, so it runs unchanged on the robot's own screen, on the Universal Robots teach pendant repurposed as a GUI, or in a remote browser. The speech interface is a classical dialogue pipeline built on Picovoice's spoken language understanding, mapping audio signals directly to intents locally on the robot without any cloud service.

<img src="/enabling/assets/theme/images/rosa_touch_speech.png" width="70%">

The user study followed ten participants (five male, five female, aged between 20 and 40) through four task sets alternating between *learning* phases, where a single prescribed modality had to be used, and *exploration* phases, where participants freely chose how to interact. Tasks ranged from waking and sleeping both robots, through personalisation such as changing Rosa's voice or Ari's eye colour, to cube manipulation — spelling words and building pyramids. A supervisor logged noteworthy events behind a partition while multiple cameras recorded the sessions. After the main questionnaire battery (UMUX, SUS, ASQ, PSSUQ, UEQ-S and custom 7-point Likert items), a remote segment used think-aloud exploration followed by an interview.

The results show a clear division of labour between the two modalities. Touch was the fastest route to a completed cube task at **27.8 s** on average, compared with **43.5 s** for the free exploration task and **77.2 s** for speech. Reliability followed the same ordering: **81.6%** of touch commands executed successfully against **67.2%** for speech, although simple intents such as *Help*, *Wake Up* and *Sleep* were recognised correctly in 95% of cases. Preference, however, initially ran the other way — participants chose speech for 90% of the personalisation and motion interactions, and for 58% of the cube tasks at the start, a share that fell to 47% as people switched to touch once precision mattered. The UEQ-S breakdown explains the split: touch scored higher on pragmatic quality (efficiency, clarity, reliability) while speech scored higher on hedonic quality (enjoyment and engagement). Satisfaction also differed per robot — for Ari, where speech only selected among simple options, both modalities were rated equally, whereas Rosa's multistep spoken cube commands were rated considerably lower than its touchscreen.

Across the three RoSA generations, the system-level gains are substantial: RoSA 3 completed the comparable task block in **3:46 min**, against 19:35 min for RoSA 1 and 25:20 min for RoSA 2, helped considerably by the newly introduced structured learning phase. Normalised across the standardised questionnaires, RoSA 3 reached an average of **75.58%** (SUS 82.00, PSSUQ 77.05, ASQ 72.86, UMUX 70.42), the best overall result of the three versions. In the remote interviews, participants confirmed that commands learned on-site carried over to the remote setting without relearning, while asking for live audio and video feeds — or a 3D digital twin — plus progress indicators to compensate for the reduced sense of the robot's state.

## Key Contributions

- **One interface, two locations**: A React-based touch UI and a locally running speech pipeline that work identically for on-site HRI and telerobotic supervision, with no interface changes between the two
- **Buffered multimodality**: The *Commander* module progressively aggregates partial messages from multiple modalities into a single robot action, removing the race conditions and input conflicts of RoSA 2
- **Two heterogeneous platforms**: The same framework controls both an industrial UR5e arm (*Rosa*) and the PAL Robotics humanoid *Ari*, enabling a direct comparison of modality preference across robot embodiments
- **Empirical modality trade-off**: Touch was faster (27.8 s vs. 77.2 s) and more reliable (81.6% vs. 67.2% command success), while speech was preferred in 90% of free exploratory interactions and rated higher on hedonic quality
- **Cross-generation evaluation**: A like-for-like comparison with RoSA 1 and RoSA 2 showing task time dropping from 25:20 min to 3:46 min and the highest usability scores of the series, underlining the value of a structured learning phase

## Fulltext Access
[https://doi.org/10.3389/frobt.2025.1561188](https://doi.org/10.3389/frobt.2025.1561188)

## Citation (BibTeX)

```bibtex
@article{strazdas2025rosa,
  author    = {Dominykas Strazdas and Matthias Busch and Rijin Shaji and Ingo Siegert and Ayoub Al-Hamadi},
  title     = {Robot System Assistant ({RoSA}): evaluation of touch and speech input modalities for on-site {HRI} and telerobotics},
  journal   = {Frontiers in Robotics and AI},
  volume    = {12},
  pages     = {1561188},
  year      = {2025},
  month     = jul,
  doi       = {10.3389/frobt.2025.1561188},
  url       = {https://doi.org/10.3389/frobt.2025.1561188}
}
```
