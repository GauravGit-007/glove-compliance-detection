# Part 2 – Reasoning-Based Questions

---

## Q1: Choosing the Right Approach

You are tasked with identifying whether a product is missing its label on an assembly line. The products are visually similar except for the label.

**Q:** Would you use classification, detection, or segmentation? Why? What would be your fallback if the first approach doesn’t work?

**Answer:**  
I would use object detection because the problem is not about recognizing the product itself, but about checking whether a specific component, the label, is present or missing. Since the products look almost identical without considering the label, a classification model would struggle and likely give misleading results. Detection allows the system to explicitly search for the label and reason about its presence or absence. If detection does not work well, for example if the label is very small, reflective, or blends into the background, my fallback would be segmentation. Segmentation would help capture fine-grained visual details when the exact shape or region of the label becomes important.

---

## Q2: Debugging a Poorly Performing Model

You trained a model on 1000 images, but it performs poorly on new images from the factory.

**Q:** Design a small experiment or checklist to debug the issue. What would you test or visualize?

**Answer:**  
My first step would be to visually compare the training images with the new factory images to look for obvious differences such as lighting, camera position, motion blur, or background changes. I would then run the model on a few training images to check whether it performs well there, which helps identify overfitting. Visualizing predictions on new images can reveal whether the model is making consistent mistakes or failing completely. I would also review the annotations to ensure they are accurate and consistent. Finally, I would test the model on a small, newly collected subset of factory images to see whether the issue is data mismatch or model capacity.

---

## Q3: Accuracy vs Real Risk

Your model has 98% accuracy but still misses 1 out of 10 defective products.

**Q:** Is accuracy the right metric in this case? What would you look at instead and why?

**Answer:**  
Accuracy is misleading in this scenario because it does not capture how costly missed defects are. Missing defective products can have serious business or safety consequences, even if the overall accuracy looks high. Instead, I would focus on recall and the false negative rate for defective items. A precision–recall analysis would help understand the trade-off between catching defects and raising false alarms. In real production systems, evaluation metrics should reflect operational risk rather than just overall prediction correctness.

---

## Q4: Annotation Edge Cases

You’re labeling data, but many images contain blurry or partially visible objects.

**Q:** Should these be kept in the dataset? Why or why not? What trade-offs are you considering?

**Answer:**  
I would keep some blurry or partially visible objects in the dataset because real-world data is rarely perfect. Including such examples helps the model become more robust to challenging conditions it may encounter in production. However, I would remove cases where the object is too ambiguous to label confidently, as this introduces noise and confuses the model during training. The main trade-off is between improving generalization and maintaining label quality. A balanced selection of edge cases usually leads to better real-world performance.
