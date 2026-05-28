# Reviewer Report Template

## Summary

Briefly summarize the paper in 3-5 sentences covering: problem, method, key results, and main contribution.

## Strengths

- S1:
- S2:
- S3:

## Weaknesses

- W1:
- W2:
- W3:

## Technical Concerns

### Novelty

- Is the problem new, or a restatement of an existing one?
- Is the method a genuine advance, meaningful recombination, or mostly engineering integration?
- Are the correct prior-art families compared?
- Are strong recent baselines included?

### Soundness

- Are assumptions explicit and reasonable?
- Are equations and algorithm steps well specified?
- Does the method logically address the stated problem?
- Are there hidden dependencies (large-scale pretraining, proprietary data, expensive search)?

### Experimental Design

- Are datasets appropriate and diverse?
- Are train/validation/test splits clear and leakage-free?
- Are metrics aligned with the claimed objective?
- Are baselines strong and fairly tuned?

### Ablations

- Are core components individually ablated?
- Are loss terms, augmentation, model size, and hyperparameters tested?
- Is training stability examined?
- Is compute/latency tradeoff reported?

### Reproducibility

- Is code available?
- Are seeds, configs, and hyperparameters complete?
- Are training schedules and data preprocessing specified?

### Hardware and Deployment Evidence

- Training hardware: GPU model, device count, batch size, precision, training time, peak VRAM
- Inference hardware: target device, latency/FPS, RAM/VRAM, precision
- Model complexity: parameters, FLOPs/MACs, activation memory
- Export/runtime path: PyTorch-only, ONNX, TensorRT, OpenVINO, CoreML, TFLite, vendor NPU SDK
- Operator support: deformable convolution, attention, dynamic shapes, NMS, interpolation, custom CUDA kernels
- Quantization compatibility: FP16/BF16/INT8, QAT, calibration, accuracy drop
- Deployment constraints: power, thermal, sustained throughput, CPU fallback risk

## Questions for Authors

1. 
2. 
3. 

## Suggested Improvements

- 

## Overall Assessment

- Score: (1-10)
- Confidence: (1-5)
- Rationale:

## References

Use GB/T 7714-2015 formatting. See `references/gbt7714-2015-examples.md`. Do not fabricate missing bibliographic fields.
