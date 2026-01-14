import os
import json
import argparse
import cv2
from ultralytics import YOLO

LABEL_MAP = {
    "gloves": "gloved_hand",
    "no-gloves": "bare_hand"
}

def run_detection(model_path, input_dir, output_dir, logs_dir, conf):
    model = YOLO(model_path)

    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(logs_dir, exist_ok=True)

    for img_name in os.listdir(input_dir):
        if not img_name.lower().endswith(".jpg"):
            continue

        img_path = os.path.join(input_dir, img_name)
        image = cv2.imread(img_path)

        results = model(image, conf=conf)[0]

        detections = []

        if results.boxes is not None:
            for box in results.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                score = float(box.conf[0])
                cls_id = int(box.cls[0])
                raw_label = model.names[cls_id]
                label = LABEL_MAP.get(raw_label, raw_label)

                detections.append({
                    "label": label,
                    "confidence": round(score, 3),
                    "bbox": [x1, y1, x2, y2]
                })

                cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(
                    image,
                    f"{label} {score:.2f}",
                    (x1, max(y1 - 10, 10)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 255, 0),
                    2
                )

        cv2.imwrite(os.path.join(output_dir, img_name), image)

        log_data = {
            "filename": img_name,
            "detections": detections
        }

        with open(os.path.join(logs_dir, img_name.replace(".jpg", ".json")), "w") as f:
            json.dump(log_data, f, indent=2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", default="output")
    parser.add_argument("--logs", default="logs")
    parser.add_argument("--confidence", type=float, default=0.5)
    parser.add_argument("--model", required=True)

    args = parser.parse_args()

    run_detection(
        model_path=args.model,
        input_dir=args.input,
        output_dir=args.output,
        logs_dir=args.logs,
        conf=args.confidence
    )
