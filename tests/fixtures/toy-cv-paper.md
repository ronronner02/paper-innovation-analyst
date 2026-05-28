# TinyDet: Efficient Small Object Detection on VisDrone via Lightweight Feature Pyramid Enhancement

## Authors
Zhang Wei, Li Ming, Chen Yun

## Abstract
Small object detection in drone-captured images remains challenging due to limited feature resolution and high object density. We propose TinyDet, a lightweight detector based on YOLOv8-nano that introduces a P2-enhanced feature pyramid with a novel attention-guided fusion module (AGF). Experiments on VisDrone2019-DET test-dev show TinyDet achieves 28.3% mAP@0.5 with 3.2M parameters and 8.1 GFLOPs on 640x640 input, outperforming YOLOv8-nano by 2.1% mAP@0.5 while maintaining 45 FPS on RTX 3090. We also evaluate on COCO val2017 and show competitive results.

## Method
Our architecture modifies the YOLOv8-nano backbone with three key changes:
1. We add a P2 detection head (stride 4) for small object detection
2. We introduce an Attention-Guided Fusion (AGF) module between P2 and P3 that uses channel attention to weight feature contributions
3. We replace the standard CIoU loss with a Scale-Aware IoU (SAIoU) loss that applies higher weight to small-object predictions

The AGF module adds approximately 0.3M parameters and 0.8 GFLOPs. SAIoU loss is defined as:
L_SAIoU = L_CIoU * (1 + alpha * exp(-area/area_threshold))
where alpha = 0.5 and area_threshold = 32*32 pixels.

## Experiments
- Dataset: VisDrone2019-DET (6,471 train, 548 val, 1,610 test images)
- Input resolution: 640x640
- Training: 100 epochs, batch size 16, SGD, initial LR 0.01
- Hardware: single RTX 3090 (24 GB), training time ~8 hours
- Results: 28.3% mAP@0.5 on test-dev (vs 26.2% for YOLOv8-nano baseline)
- AP_small: 12.1% (vs 9.8% baseline)

## Limitations
- Only tested on VisDrone; no evaluation on DOTA or other remote-sensing datasets
- No ONNX/TensorRT export or latency profiling on edge devices
- P2 head increases memory usage; peak VRAM not reported
- No ablation on individual AGF components
- SAIoU loss hyperparameters (alpha, area_threshold) not tuned via grid search
