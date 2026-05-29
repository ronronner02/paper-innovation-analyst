# Experiment Plan Template

## 1. Research Question

State the question in one sentence.

## 2. Hypothesis

- Primary hypothesis:
- Secondary hypotheses:

## 3. Baseline Reproduction

- Original paper method:
- Public code availability:
- Dataset:
- Input size / batch size / precision:
- Expected reproduced metric:
- Reported training hardware and time:
- Reported inference hardware and latency/FPS:
- Reported parameters / FLOPs / MACs / memory:
- Reproduction risk:

## 4. Proposed Method

- Modification:
- Architecture/pipeline changes:
- Layer/module-level changes:
- Loss/objective changes:
- Data changes:
- Inference/postprocessing changes:
- Export/quantization changes, if any:

## 5. Datasets and Protocol

- Dataset(s):
- Dataset-specific pain points, e.g. small objects, long-tail classes, occlusion, resolution, annotation noise, domain shift:
- Split:
- Preprocessing:
- Evaluation protocol:
- Leakage controls:

## 6. Metrics

- Primary metric:
- Secondary metrics:
- Efficiency metrics: parameters, FLOPs/MACs, peak VRAM/RAM, training time, latency, FPS, power if available:
- Robustness metrics:

## 7. Hardware & Deployment Constraints

- Training hardware target, e.g. GPU model/count, available VRAM, CPU/RAM, storage:
- Inference/deployment hardware target, e.g. RTX-class GPU, Jetson, RK3588, Raspberry Pi, Android NPU, FPGA, MCU, C51-class embedded environment:
- Expected VRAM/RAM consumption:
- Expected FLOPs/MACs and parameter count:
- Expected latency/FPS target at specific input size and batch size:
- Precision target: FP32 / FP16 / BF16 / INT8 / mixed precision:
- Runtime/export path: PyTorch / ONNX / TensorRT / OpenVINO / CoreML / TFLite / vendor NPU SDK / C or C++ / embedded C:
- Operator-support risks: dynamic shape, custom CUDA op, deformable convolution, attention, NMS, interpolation, indexing, unsupported activation:
- Required low-level optimization: pruning, distillation, quantization-aware training, kernel fusion, memory reuse, tiling, C/C++ rewrite, C51-style embedded C rewrite:
- Profiling tools to use:

## 8. Baselines

| Baseline | Purpose | Expected difficulty | Hardware/compute requirement |
|---|---|---|---|
| Original method | Direct comparison |  |  |
| Strong prior method | Literature comparison |  |  |
| Simple baseline | Sanity check |  |  |

## 9. Ablation Matrix

| Ablation | Purpose | Expected outcome | VRAM/Compute Cost Estimate | Failure signal | Debug action |
|---|---|---|---|---|---|
| Remove component A | Test contribution |  |  |  |  |
| Change loss weight | Sensitivity |  |  |  |  |
| Smaller data setting | Generalization |  |  |  |  |
| Quantize/export variant | Deployment feasibility |  |  |  |  |

## 10. Milestones

| Milestone | Deliverable | Success criterion | Engineering check |
|---|---|---|---|
| 1 | Environment and data ready | Training pipeline runs | Dataset checksum, dataloader speed, GPU visibility |
| 2 | Baseline reproduced | Metric close to paper or explained gap | Same input size, batch size, seed, precision where possible |
| 3 | Proposed method implemented | No training/runtime errors | Shape checks, gradient checks, unit tests |
| 4 | Main experiments completed | Results table available | Logs, checkpoints, resource profile saved |
| 5 | Ablations completed | Contribution isolated | Same schedule and hyperparameters unless justified |
| 6 | Deployment test completed | Export/profile report available | ONNX/TensorRT/target-device test passes or failure explained |
| 7 | Report written | Claims supported by evidence | References formatted in GB/T 7714-2015 |

## 11. Failure Criteria and Fallbacks

For every failure, provide a direct debugging action and a scoped fallback.

### Loss divergence

- Diagnosis plan: check learning rate, label format, loss scale, AMP overflow, bbox normalization, class index range, unstable augmentation, inspect first batch, monitor gradient norm
- Immediate fallback: lower learning rate, disable AMP, clip gradients, freeze backbone, reduce augmentation strength, use warmup or gradient clipping, verify loss on tiny batch

### NaN / Inf

- Diagnosis plan: check loss scale, gradient norm, input normalization, label range, AMP autocast, division by zero in custom ops
- Immediate fallback: disable AMP, reduce learning rate, add epsilon to denominators, clip gradients, check for empty batches

### Training collapse or no metric improvement

- Diagnosis plan: overfit 8-32 samples, compare baseline configs, inspect predictions, validate metric code, check class imbalance
- Immediate fallback: start from pretrained weights, simplify module, use original loss, reduce modification scope

### GPU OOM

- Diagnosis plan: record peak allocated/reserved memory with `torch.cuda.memory_summary()`, log activation sizes, input resolution, batch size, dataloader workers, checkpointing behavior
- Immediate fallback:
  1. Reduce batch size
  2. Reduce input resolution
  3. Enable AMP (FP16/BF16)
  4. Enable gradient accumulation
  5. Enable gradient checkpointing
  6. Freeze backbone or early layers
  7. Remove high-memory module
  8. Profile feature maps to identify memory hotspot
  9. Simplify neck/head architecture
  10. Test with smaller data subset first

### CPU RAM OOM

- Diagnosis plan: monitor RSS with `psutil`, check dataloader num_workers, inspect dataset caching behavior
- Immediate fallback: reduce num_workers, disable dataset caching, use memory-mapped data, reduce batch pre-fetch

### CUDA kernel error

- Diagnosis plan: check CUDA/driver version compatibility, verify custom op compilation, test with CPU fallback
- Immediate fallback: replace custom kernel with PyTorch equivalent, update CUDA toolkit, disable problematic augmentation

### Dataloader bottleneck

- Diagnosis plan: profile data loading time vs GPU compute time, check num_workers, pin_memory, prefetch_factor
- Immediate fallback: increase num_workers, enable pin_memory, pre-process dataset offline, use memory-mapped format

### Deployment export failure (ONNX / TensorRT)

- Diagnosis plan: export minimal graph, inspect unsupported ops with `onnx.checker`, compare ONNX vs PyTorch outputs, profile pre/postprocessing separately
- Immediate fallback: replace unsupported ops, simplify dynamic shapes, move NMS/postprocess to supported runtime, use INT8/FP16, rewrite critical path in C/C++

### Edge-device latency too high

- Diagnosis plan: profile per-layer latency on target device, identify compute/memory bottleneck ops, measure power consumption
- Immediate fallback: reduce input resolution, prune channels, use depthwise separable convolutions, quantize to INT8, simplify postprocessing

### Metric regression

- Diagnosis plan: compare against baseline with identical config, check data preprocessing, verify metric implementation, inspect failure cases
- Immediate fallback: revert to baseline config, add modification incrementally, isolate the regressing component

### Reproduction gap

- Diagnosis plan: verify dataset version, check preprocessing pipeline, compare model config line-by-line with paper, check random seed
- Immediate fallback: contact authors for config, use official code if available, document gap and proceed with adjusted baseline

## 12. Reproducibility and Experiment Logging

- Git commit:
- Config file:
- Random seeds:
- Environment: Python / PyTorch / CUDA / cuDNN:
- Dataset checksum/version:
- Exact training command:
- Exact evaluation command:
- Logging backend: TensorBoard / W&B / CSV / MLflow:
- Checkpoint policy:
- Resume policy:
- Deterministic setting:
- Hardware inventory:
- Driver version:
- Training time estimate:
- Evaluation protocol:
- Result table format:
- Failure log location:

## 13. Claim Safety Check

For any claim in this experiment plan containing trigger words (first / 首个 / 首次 / novel / SOTA / ONNX compatible / real-time / 部署完全兼容 / specific VRAM / 4K <200ms):

| Claim | Evidence level | Required validation | Rewrite if unsafe |
|---|---|---|---|
|  |  |  |  |

Rules:
- "first / 首个 / 首次" without literature search → `potentially underexplored; requires literature search`
- "ONNX/TensorRT compatible" without export test → `requires export validation`
- Specific VRAM/latency/FPS → `Engineering hypothesis requiring validation`
- All deployment estimates → `Engineering hypothesis requiring validation`

## 14. References

Use GB/T 7714-2015 formatting. See `references/gbt7714-2015-examples.md`. Do not fabricate missing bibliographic fields.
