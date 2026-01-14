# Part 2 – Reasoning-Based Answers

## Q1: Choosing the Right Approach

I would use object detection because the task requires locating whether a label exists on a product, not just classifying the entire image. Classification would fail if the label is missing or partially visible, since the product itself remains visually similar. Detection allows the system to explicitly check for the presence and position of the label. If detection performs poorly due to small or subtle labels, I would fall back to segmentation to capture finer spatial details. Segmentation would help in cases where precise boundaries of the label are required.

---

## Q2: Debugging a Poorly Performing Model

First, I would compare training and inference images to check for distribution shifts such as lighting, camera angle, or background differences. I would visualize predictions on both training and validation images to detect overfitting or label noise. Next, I would inspect annotations to ensure bounding boxes are accurate and consistently labeled. I would also evaluate performance per class to see if one class dominates errors. Finally, I would test simple augmentations or fine-tune on a small set of real factory images.

---

## Q3: Accuracy vs Real Risk

Accuracy is not the right metric in this case because it can hide critical false negatives. Missing defective products is more costly than occasionally flagging good ones. I would focus on recall, false negative rate, and precision-recall tradeoffs. Monitoring recall ensures that most defective products are detected. In safety or quality control systems, minimizing missed detections is more important than maximizing overall accuracy.

---

## Q4: Annotation Edge Cases

Blurry or partially visible objects should be included selectively in the dataset. Keeping some of these examples helps the model generalize to real-world conditions where perfect images are rare. However, extremely ambiguous cases should be excluded to avoid confusing the model during training. The trade-off is between robustness and label noise. A balanced approach improves generalization without degrading model reliability.
