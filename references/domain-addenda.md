# Domain-Specific Addenda

Apply the relevant addendum when the paper falls into a specific domain. These addenda supplement, not replace, the core workflow in SKILL.md.

---

## 1. Machine Learning / Computer Vision (ML/CV)

### Limitation Mining — Additional Angles

- Backbone efficiency: parameter count, FLOPs, latency at common input resolutions (224, 320, 416, 640, 800, 1024+)
- Feature pyramid design: stride coverage, top-down/bottom-up fusion cost, memory at high-resolution inputs
- Detection head complexity: anchor-based vs anchor-free, label assignment strategy, NMS cost and sensitivity
- Segmentation memory: per-pixel prediction cost at high resolution, boundary quality, stuff/thing class handling
- Data pipeline: augmentation policy, mosaic/mixup cost, tiling for large images, annotation noise handling
- Pretraining dependency: ImageNet, COCO, Objects365, CLIP, DINOv2 — and transfer gap to target domain

### Innovation Vocabulary

Affected pipeline stage: backbone, neck (FPN/PAN/BiFPN/NAS-FPN), feature fusion, detection/segmentation head, label assignment (ATSS/SimOTA/OTA), loss term (focal/GIoU/CIoU/Dice), postprocessing (NMS variants, soft-NMS, learned NMS), preprocessing (tiling, resizing, normalization).

### Deployment Checklist

- ONNX export with dynamic batch/shape
- TensorRT INT8 calibration accuracy drop
- Deformable convolution / deformable attention support
- NMS implementation: GPU kernel vs CPU fallback
- Input tiling for remote-sensing / satellite imagery
- Real-time video: end-to-end pipeline latency including pre/postprocessing

---

## 2. Natural Language Processing / Large Language Models (NLP/LLM)

### Limitation Mining — Additional Angles

- Token efficiency: sequence length scaling, context window limits, long-range dependency handling
- Training data: corpus composition, contamination, deduplication, multilingual coverage, toxicity/bias
- Instruction tuning: alignment tax, catastrophic forgetting, instruction following fidelity
- RLHF / DPO: reward model quality, reward hacking, preference data cost and bias
- Inference cost: KV-cache memory, decoding strategy (greedy/beam/nucleus), speculative decoding, batch serving throughput
- Evaluation contamination: benchmark leakage into training data, static vs dynamic benchmarks
- Hallucination: factual grounding, attribution, faithfulness to source documents
- Multilinguality: cross-lingual transfer gap, low-resource language coverage, script/tokenizer bias

### Innovation Vocabulary

Affected module: tokenizer, embedding layer, positional encoding (sinusoidal/RoPE/ALiBi), attention mechanism (MHA/MQA/GQA/linear attention), FFN/MLP block, layer normalization (pre-norm/post-norm/RMSNorm), output head (LM head/classification head), loss function (cross-entropy/contrastive/RLHF reward), decoding strategy, prompt template, retrieval module (for RAG).

### Deployment Checklist

- Quantization: GPTQ/AWQ/GGUF, bit-width, perplexity degradation
- KV-cache: memory per token, cache eviction policy, paged attention
- Serving: continuous batching, tensor parallelism, pipeline parallelism
- Latency: time-to-first-token (TTFT), inter-token latency (ITL), tokens/second
- Context length: memory scaling, positional encoding extrapolation, retrieval-augmented fallback

---

## 3. Systems / Networking / Databases

### Limitation Mining — Additional Angles

- Throughput vs latency tradeoff: tail latency (p99/p999), batch efficiency, queueing dynamics
- Fault tolerance: failure detection, recovery time, consistency guarantees under partition
- Scalability: single-node vs distributed, horizontal scaling bottleneck, coordination overhead
- Resource efficiency: CPU/memory/disk/network utilization, cost-per-query, energy per operation
- Reproducibility: workload specification, hardware dependency, configuration sensitivity
- Realism: synthetic benchmarks vs production traces, workload skew, burstiness

### Innovation Vocabulary

Affected component: data structure, algorithm, scheduling policy, caching layer, replication protocol, consensus mechanism, query optimizer, storage engine, network protocol, serialization format, concurrency control, memory allocator, garbage collector.

### Deployment Checklist

- Benchmark setup: hardware spec, workload generator, warm-up, measurement methodology
- Scalability test: single-node baseline, multi-node scaling curve, bottleneck identification
- Failure injection: crash, network partition, Byzantine behavior, recovery validation
- Comparison fairness: same hardware, same workload, same correctness guarantees

---

## 4. Robotics / Embodied AI

### Limitation Mining — Additional Angles

- Sim-to-real gap: domain randomization fidelity, physics engine limitations, visual realism
- Sensor noise: camera distortion, IMU drift, LiDAR sparsity, GPS accuracy
- Real-time constraints: control loop frequency, sensor-to-actuator latency, planning horizon
- Safety: collision avoidance, human-robot interaction safety, fail-safe mechanisms
- Generalization: novel environments, object variations, lighting/weather changes
- Data collection: teleoperation cost, demonstration quality, reward engineering

### Innovation Vocabulary

Affected module: perception encoder, state estimator, policy network (MLP/CNN/Transformer), planner (MPC/RRT/PRM), reward function, world model, action space discretization, observation space design, sim-to-real transfer method (domain adaptation/domain randomization/system identification).

### Deployment Checklist

- Onboard compute: Jetson/Intel NUC/embedded GPU, power budget, thermal constraints
- Control frequency: policy inference latency vs required Hz
- Sensor suite: camera resolution, LiDAR point density, IMU sample rate
- Safety validation: simulation testing, physical sandbox testing, human oversight

---

## 5. Human-Computer Interaction (HCI)

### Limitation Mining — Additional Angles

- User study design: sample size, demographic diversity, task ecological validity, counterbalancing
- Measurement: objective task metrics (time, error rate) vs subjective metrics (SUS, NASA-TLX, Likert)
- Generalization: lab vs field, expert vs novice, accessibility (vision, motor, cognitive)
- Interaction modality: input device, modality combination, error recovery, feedback design
- Longitudinal effects: learning curve, retention, fatigue, novelty effect
- Ethics: informed consent, data privacy, vulnerable populations, deception

### Innovation Vocabulary

Affected component: input modality (touch/gaze/gesture/voice/EEG/EMG), feedback channel (visual/haptic/auditory), interaction technique, interface layout, information architecture, adaptive/personalized system, accessibility feature, evaluation protocol (between-subjects/within-subjects/mixed), analysis method (qualitative coding/thematic analysis/statistical test).

### Deployment Checklist

- Participant recruitment: IRB approval, inclusion criteria, compensation
- Study apparatus: hardware setup, software version, environmental controls
- Data collection: logging, screen recording, think-aloud, post-task questionnaire
- Analysis: statistical power, effect size, multiple comparison correction, inter-rater reliability
