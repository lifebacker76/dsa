# 🖼️ Project 3: Image Classifier

**Computer Vision with Transfer Learning**

| | |
|---|---|
| **Difficulty** | ⭐⭐⭐ Intermediate+ |
| **Time Estimate** | 10–15 hours |
| **Prerequisites** | Deep Learning Fundamentals, PyTorch basics |

---

## Overview

Build an image classification system that categorizes images into predefined classes. First train a CNN from scratch to understand the fundamentals, then use **transfer learning** with a pretrained ResNet to achieve much better results with less data and training time.

**Goal:** Classify images into categories (e.g., 10 classes in CIFAR-10).

---

## Dataset

Choose one:
- **CIFAR-10** (built into torchvision) — 60,000 32x32 color images in 10 classes
  - Classes: airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck
- **Custom Dataset** — Use `torchvision.datasets.ImageFolder` with your own images
  - Organize as: `data/train/class_name/image.jpg`
  - Good sources: [Kaggle Datasets](https://www.kaggle.com/datasets), Google Images

CIFAR-10 is great for fast iteration. A custom dataset teaches you real-world data loading.

---

## Steps

### Step 1: Data Loading with Augmentation
- Load dataset with `torchvision.datasets`
- Apply transforms: resize, normalize, random flip, random crop, color jitter
- Create `DataLoader` objects for train/val/test
- Visualize a batch of images with their labels
- Understand the impact of augmentation (show augmented vs original)

### Step 2: Train a CNN from Scratch
- Design a simple CNN architecture:
  - Conv2d → ReLU → MaxPool (repeat 2-3 times)
  - Flatten → Linear → ReLU → Linear → Output
- Train for 10-20 epochs
- Plot training/validation loss and accuracy curves
- Evaluate on test set

### Step 3: Transfer Learning with Pretrained ResNet
- Load `resnet18` (or `resnet50`) pretrained on ImageNet
- Freeze all layers except the final classifier
- Replace the final `fc` layer to match your number of classes
- Fine-tune for 5-10 epochs (much fewer needed!)
- Compare training speed and convergence vs from-scratch

### Step 4: Compare From-Scratch vs Transfer Learning
- Create comparison table:
  | Model | Test Accuracy | Training Epochs | Training Time |
  |-------|--------------|-----------------|---------------|
  | CNN from scratch | ? | ? | ? |
  | ResNet (transfer) | ? | ? | ? |
- Discuss: why is transfer learning so effective?

### Step 5: Visualize Predictions and Errors
- Show a grid of test images with predicted vs true labels
- Highlight correct (green) and incorrect (red) predictions
- Create a confusion matrix heatmap
- Find the most confused class pairs
- (Optional) Visualize feature maps / Grad-CAM

---

## What You'll Learn

| Skill | Notebook Topic |
|-------|---------------|
| PyTorch tensors & autograd | `08_Deep_Learning/` |
| Building CNN architectures | `10_Computer_Vision/` |
| Data augmentation | `10_Computer_Vision/` |
| Transfer learning | `10_Computer_Vision/` |
| Training loops & optimization | `08_Deep_Learning/` |
| Model evaluation & visualization | `06_Classical_ML/`, `04_Visualization/` |

---

## Deliverables Checklist

- [ ] Data loading pipeline with augmentation transforms
- [ ] CNN architecture defined from scratch
- [ ] Training loop with loss/accuracy tracking
- [ ] Training curves (loss and accuracy) plotted
- [ ] Transfer learning model with frozen layers
- [ ] Comparison table: from-scratch vs transfer learning
- [ ] Prediction visualization grid (correct/incorrect)
- [ ] Confusion matrix heatmap
- [ ] Clean `main.py` with modular functions
- [ ] Brief write-up: what you learned about CNNs and transfer learning

---

## Starter Code

See [`main.py`](main.py) for the project skeleton.

```
project_3_image_classifier/
├── README.md
├── main.py              # Main pipeline script
├── notebook.ipynb       # Experimentation (create this)
├── models/              # Saved models (create this)
└── data/                # Downloaded data (auto by torchvision)
```
