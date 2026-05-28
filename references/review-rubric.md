# Paper Review and Innovation Rubric

Use this rubric when critiquing a paper or generating innovation points.

## 1. Problem and Motivation

- Is the research problem clearly defined?
- Is the problem important, timely, or technically challenging?
- Does the paper explain why existing methods are insufficient?
- Is the setting realistic or artificially constrained?

## 2. Related Work Positioning

- Does the paper compare against the correct families of prior work?
- Are strong recent baselines included?
- Is the claimed novelty incremental or substantial?
- Does the paper ignore obvious competing methods?

## 3. Method Novelty

Assess whether the method introduces:

- a new formulation
- a new architecture or module
- a new objective or loss
- a new training strategy
- a new inference algorithm
- a new data pipeline
- a new benchmark/evaluation protocol
- a new theoretical result

Classify novelty as:

- Low: mostly direct application or small engineering change
- Medium: meaningful recombination or targeted improvement
- High: new formulation, strong mechanism, or broadly reusable contribution

## 4. Technical Soundness

- Are assumptions explicit and reasonable?
- Are equations and algorithm steps well specified?
- Does the method logically address the stated problem?
- Are there hidden dependencies such as large-scale pretraining, proprietary data, or expensive search?
- Are edge cases handled?

## 5. Experimental Design

- Are datasets appropriate and diverse?
- Are train/validation/test splits clear?
- Are metrics aligned with the claimed objective?
- Are baselines strong and fairly tuned?
- Are hyperparameters, seeds, and compute details reported?
- Are confidence intervals or statistical tests included when needed?

## 6. Ablation Quality

Look for ablations on:

- each core component
- loss terms
- data augmentation
- model size
- dataset size
- hyperparameters
- training stability
- inference strategy
- compute/latency tradeoff

## 7. Generalization and Robustness

Check whether the paper tests:

- cross-domain transfer
- out-of-distribution data
- adversarial or noisy inputs
- low-resource settings
- long-tail cases
- different model scales
- different languages/modalities/tasks where relevant

## 8. Efficiency, Hardware, and Deployment Practicality

Separate training feasibility from deployment feasibility. A method that trains well on large RTX-class or data-center GPUs may still be unusable on embedded or MCU-class targets.

### 8.1 Training-side evidence

- GPU/TPU/NPU/CPU model and number of devices
- batch size, input resolution, precision, and training schedule
- training time and energy if reported
- peak VRAM and activation memory pressure
- dataloader and preprocessing bottlenecks
- whether reported throughput depends on high-end GPU parallelism

### 8.2 Inference-side evidence

- target hardware: data-center GPU, RTX-class GPU, Jetson, RK3588, Raspberry Pi, mobile NPU, FPGA, MCU, or C51-class embedded environment
- latency, FPS, batch size, input resolution, and precision
- parameters, FLOPs/MACs, peak RAM/VRAM, memory bandwidth pressure
- preprocessing and postprocessing cost, especially NMS, tiling, resizing, and CPU fallback
- power, thermal, and sustained-throughput constraints if relevant

### 8.3 Operator and runtime compatibility

- ONNX exportability
- TensorRT/OpenVINO/CoreML/TFLite/vendor NPU SDK support
- unsupported or expensive ops: dynamic shapes, custom CUDA kernels, deformable convolution, attention, interpolation, gather/scatter/indexing-heavy ops, NMS variants
- quantization compatibility: FP16/BF16/INT8, quantization-aware training, calibration data, accuracy drop
- need for C/C++ rewrite, embedded C rewrite, or C51-style constrained implementation

### 8.4 Domain-specific deployment pressure

- small-object detection: feature stride, high-resolution input, dense prediction memory
- remote sensing: image tiling, overlap, geospatial postprocessing, large-image IO
- real-time video: end-to-end pipeline latency, frame buffering, tracking/postprocessing cost
- edge robotics: sensor IO, control-loop deadlines, thermal throttling

### 8.5 Missing-evidence flags

Flag the paper if it omits any required dimension for its claims:

- no hardware details
- no latency/FPS on target device
- no peak memory or model-size report
- no export/runtime validation
- no ablation of efficient module versus accuracy
- no comparison under matched compute budgets

## 9. Limitations and Risks

- Dataset bias or leakage
- Metric gaming
- Overfitting to benchmark
- Weak baselines
- Missing negative results
- Ethical/safety concerns
- Privacy/security risks
- Environmental cost

## 10. Innovation Mining Heuristics

Generate ideas by asking:

- What assumption can be relaxed?
- What setting is missing?
- What component lacks ablation?
- What would fail under distribution shift?
- Can this be made cheaper, smaller, faster, safer, or more interpretable?
- Can the method be transferred to another domain or modality?
- Can evaluation be improved with a harder benchmark or diagnostic metric?
- Can multiple papers be synthesized into a stronger method?
- Can a negative result or failure case become a contribution?

## 11. Idea Scoring

Score each innovation idea from 1 to 5.

### Feasibility

1. Very hard; requires unavailable data, compute, or expertise
2. Hard; possible but risky for an individual project
3. Moderate; feasible with careful scope control
4. Good; implementable with common resources
5. Excellent; quick prototype possible

### Novelty

1. Very common or obvious
2. Minor extension
3. Plausible workshop-level contribution
4. Strong thesis or conference-submission candidate
5. Potentially high-impact direction

### Risk

1. Low risk; likely to produce interpretable results
2. Some risk but manageable
3. Moderate uncertainty
4. High chance of null result or engineering blockage
5. Very high uncertainty or dependency risk


## 12. Citation and Reference Formatting

When reports include citations or references, use GB/T 7714-2015 formatting. Do not fabricate missing authors, titles, venues, years, volume/issue numbers, pages, DOI, arXiv IDs, or URLs. If a bibliographic field is unavailable in the provided material, mark it as missing and keep the reference auditable.
