# LongCache: Efficient Key-Value Cache Compression for Long-Context LLM Inference

## Authors
Wang Xiaoming, Liu Jia, Zhao Peng

## Abstract
Large language models suffer from quadratic memory growth in key-value (KV) cache during long-context inference. We propose LongCache, a training-free KV cache compression method that combines attention-score-based eviction with temporal smoothing. LongCache reduces KV cache memory by 60% while preserving 97% of the original perplexity on PG-19 and BookSum benchmarks. Our method requires no fine-tuning and is compatible with any Transformer-based LLM. Experiments on LLaMA-2-7B and Mistral-7B show that LongCache enables 32K-context inference on a single 24 GB GPU, compared to 8K baseline context length.

## Method
LongCache operates in three steps:
1. Score-based eviction: at each decoding step, compute attention scores for all cached KV pairs and evict the bottom 40% by score magnitude
2. Temporal smoothing: apply exponential moving average (EMA) to remaining KV pairs to reduce oscillation
3. Budget reallocation: dynamically adjust eviction ratio based on sequence position (more aggressive early, conservative near the end)

Key hyperparameters: eviction_ratio=0.4, ema_alpha=0.9, position_schedule=linear_decay.

## Experiments
- Models: LLaMA-2-7B, Mistral-7B
- Benchmarks: PG-19 (perplexity), BookSum (ROUGE), LongBench (6 tasks)
- Baselines: H2O, StreamingLLM, Scissorhands
- Hardware: single A100 80 GB, batch size 1
- Results: 60% cache reduction, 97.2% perplexity retention on PG-19, 2.3x throughput improvement
- LongBench average: 41.2 (vs 42.1 full cache, 38.7 H2O, 36.1 StreamingLLM)

## Limitations
- Evaluated only on 7B models; scalability to 70B+ not tested
- No latency profiling on consumer GPUs or edge devices
- Eviction ratio schedule is heuristic; no theoretical justification
- No evaluation on retrieval-augmented generation (RAG) tasks
- EMA smoothing adds ~5% overhead; not ablated separately
