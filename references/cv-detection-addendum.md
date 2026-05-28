# CV / Object Detection Addendum

When the paper belongs to computer vision, object detection, remote sensing detection, small object detection, YOLO-style detection, or lightweight deployment, this addendum MUST be consulted and applied.

---

## YOLO-style Detection Analysis Checklist

### Backbone

Must check:
- Architecture: CSP / C2f / C3 / ELAN / RepBlock / MobileNet / ShuffleNet / ConvNeXt / Swin / ViT
- Receptive field size and coverage
- Feature stride at each output level (P3/8, P4/16, P5/32)
- Small-object feature retention at early layers
- Parameter count and FLOPs impact of any backbone change

### Neck

Must check:
- FPN / PAN / BiFPN / PAFPN / NAS-FPN / attention-based fusion variants
- P2/P3/P4/P5 feature paths and their connectivity
- Multi-scale fusion quality and information flow direction
- Small-object information loss during top-down or bottom-up fusion
- Feature aliasing and semantic gap between adjacent levels

### Head

Must check:
- Anchor-based vs anchor-free design
- Decoupled head: separate classification and regression branches
- Classification-regression conflict in shared features
- Objectness branch presence and role
- Distributional regression (DFL) or IoU-aware regression
- Label assignment strategy coupling with head design

### Assignment Strategy

Must check:
- ATSS / SimOTA / TaskAlignedAssigner (TAL) / Hungarian matching
- Dynamic-k assignment behavior
- Positive/negative sample imbalance ratio
- Anchor-free vs anchor-based assignment differences
- Cost function design (classification + regression + IoU)

### Loss Function

Must check:
- Classification: BCE / Focal Loss / Varifocal Loss / Quality Focal Loss
- Regression: CIoU / DIoU / GIoU / SIoU / DFL
- Class imbalance loss variants
- Small-object localization loss sensitivity
- Loss weight balancing between tasks

### Dataset-specific Pain Points

**MS COCO:**
- Scale diversity (tiny to large objects)
- Crowded scenes and occlusion
- Common object bias (80 classes, long-tail distribution)

**VisDrone:**
- Tiny objects (often < 16x16 pixels)
- Dense scenes with hundreds of objects per image
- Heavy occlusion in pedestrian/crowd scenes
- Low resolution aerial images

**DOTA / Remote Sensing:**
- Rotation-invariant detection requirement
- Large image tiling strategy and overlap
- Small vehicles in satellite imagery
- Extreme scale variation within single image

**Medical Images:**
- Low contrast between lesion and background
- Small lesion detection (often < 5% of image)
- Annotation noise from inter-observer variability
- Class imbalance (healthy >> abnormal)

**Industrial Defects:**
- Few-shot defect samples
- Extreme class imbalance (good >> defective)
- Tiny anomaly regions
- Texture-based rather than shape-based detection

### Deployment Constraints

Must check:
- NMS latency: CPU vs GPU implementation, per-class vs global
- TensorRT plugin requirement for custom operators
- ONNX export risk: dynamic shapes, custom ops, control flow
- Dynamic shape risk at inference time
- INT8 calibration: accuracy drop, calibration dataset
- Edge NPU compatibility: operator support, memory constraints
- Unsupported operators: deformable convolution, deformable attention, custom CUDA kernels
- MCU/C51 infeasibility unless model is heavily simplified (< 1M params, integer-only)

---

## Innovation Requirements for CV/Detection Papers

Every proposed innovation idea MUST specify at least 3 of the following:

1. Affected backbone/neck/head layer
2. Feature stride or scale level
3. Tensor fusion path change
4. Loss term or assignment rule modification
5. Dataset characteristic addressed (COCO scale diversity / VisDrone tiny objects / DOTA tiling / medical low contrast)
6. Expected metric movement (mAP@0.5 / mAP@0.5:0.95 / AP_s / AP_m / AP_l)
7. FLOPs/VRAM/latency impact estimate
8. Deployment compatibility (ONNX / TensorRT / edge device)

If an idea cannot satisfy at least 3 of these, label it as `too generic` and refine before presenting.
