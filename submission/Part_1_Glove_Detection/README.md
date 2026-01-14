# Gloved vs Ungloved Hand Detection

This project implements an object detection pipeline to identify whether hands in images are wearing gloves or not.
The system is designed as a safety compliance check for factory or industrial environments and can be applied to images from cameras or snapshots.

---

## Dataset

- Source: Roboflow Universe (forked locally)
- Task Type: Object Detection
- Original Dataset Classes:
  - gloves
  - no-gloves

To align with the assignment requirements, labels are mapped at inference time as follows:

- gloves → gloved_hand  
- no-gloves → bare_hand  

The original dataset labels were not modified. The mapping is handled only in the inference pipeline.

---

## Model

- Architecture: YOLOv8n (Ultralytics)
- Initialization: COCO-pretrained weights
- Framework: PyTorch (Ultralytics)

YOLOv8n was chosen for its balance between accuracy and inference speed, making it suitable for safety monitoring use cases.

---

## Training

- Training Environment: Local machine (CPU-only)
- Reason: CUDA was not available in the local PyTorch setup
- Epochs Completed: 10
- Image Size: 640 × 640
- Batch Size: 4

Training was stopped early once the model showed sufficient convergence for demonstration purposes.
The best-performing weights (best.pt) were used for inference.

---

## Inference Pipeline

The detection pipeline performs the following steps:

1. Reads .jpg images from an input directory
2. Runs object detection using the trained YOLOv8 model
3. Draws bounding boxes and labels on detected hands
4. Saves annotated images to an output directory
5. Logs detections per image into a JSON file

Each image generates a corresponding JSON log in the following structure:

    {
      "filename": "image.jpg",
      "detections": [
        {
          "label": "gloved_hand",
          "confidence": 0.92,
          "bbox": [x1, y1, x2, y2]
        }
      ]
    }

---

## What Worked Well

- The model reliably distinguishes between gloved and bare hands under normal lighting conditions
- Inference-time label mapping cleanly aligns dataset labels with business requirements
- The pipeline is fully reproducible and configurable using CLI arguments

---

## Limitations

- Performance degrades on motion-blurred or partially occluded hands
- Thin gloves with skin-like color can reduce confidence scores
- CPU-based training significantly increased training time

---

## How to Run

From the Part_1_Glove_Detection directory:

    python detection_script.py \
      --model runs/detect/train/weights/best.pt \
      --input sample_images \
      --output output \
      --logs logs \
      --confidence 0.4

---

## Directory Structure

    Part_1_Glove_Detection/
    ├── detection_script.py
    ├── sample_images/
    ├── output/
    ├── logs/
    └── README.md

---

## Notes

- Training artifacts (runs/) and dataset files are excluded from version control
- The project focuses on correctness, clarity, and reproducibility rather than maximizing benchmark metrics
