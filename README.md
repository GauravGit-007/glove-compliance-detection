# Glove Compliance Detection – ML Assignment

This repository contains my submission for the **Junior ML Engineer technical assessment (Biz-Tech Analytics)**.

The project implements a complete computer vision pipeline to detect **gloved vs ungloved hands** in images, simulating a factory safety compliance use case.

---

## Repository Overview

### Part 1: Glove Detection Pipeline  
`submission/Part_1_Glove_Detection/`

- YOLOv8-based object detection model
- Python inference script with CLI arguments
- Sample input images
- Annotated output images
- Per-image JSON detection logs
- Detailed README explaining dataset, training, and limitations

Detected classes:
- `gloved_hand`
- `bare_hand`

---

### Part 2: Reasoning-Based Answers  
`submission/Part_2_Answers.md`

Written responses covering:
- Model selection strategy
- Debugging poor model performance
- Evaluation metrics under real-world risk
- Handling annotation edge cases

---

## Technical Summary

- **Model:** YOLOv8n (Ultralytics)
- **Framework:** PyTorch
- **Training:** Local CPU training with early stopping
- **Inference:** Fully automated and configurable
- **Logging:** Structured JSON output per image

The focus of this submission is clarity, correctness, and practical engineering decisions rather than benchmark optimization.

---

## How to Review

1. Start with `submission/Part_1_Glove_Detection/README.md`
2. Review `detection_script.py`
3. Inspect sample outputs and JSON logs
4. Read `submission/Part_2_Answers.md`

---

Thank you for reviewing this submission.
