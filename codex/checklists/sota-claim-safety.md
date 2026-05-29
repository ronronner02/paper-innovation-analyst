# SOTA Claim Safety Gate

Any claim containing SOTA-type language MUST pass this gate.

## Trigger Words

**English:** first, novel, SOTA, state-of-the-art, fully compatible, ONNX compatible, TensorRT compatible, deployment-ready, real-time, negligible FLOPs, zero overhead, 8GB GPU, 16GB GPU, specific VRAM, low latency, all tasks, all papers, all datasets, safe for edge deployment, production-ready, 4K <200ms, INT8 1.5-2x, VRAM 2-4GB.

**Chinese:** 首个, 首次, 第一个, 首次提出, 全新, 完全兼容, 实时, 零开销, 可忽略, 单卡8GB, 8GB显存, 4K <200ms, VRAM 2-4GB, ONNX兼容性好, 部署完全兼容, 单GPU 8GB+.

## SOTA Tripartite Classification

Every SOTA claim MUST be classified as one of:

| Classification | Meaning | When to use |
|---|---|---|
| `paper-claimed SOTA` | The paper itself claims SOTA | The paper explicitly states "state-of-the-art" or equivalent |
| `supported within evaluated baselines` | Outperforms the baselines tested in the paper | The paper shows better numbers but does NOT claim SOTA |
| `externally verified SOTA` | Confirmed by independent external literature search | You have actually searched and verified against other papers |

## Rules

- Do NOT write `externally verified SOTA` without having performed an actual external literature search.
- If no external search was done, use `paper-claimed SOTA` or `supported within evaluated baselines` instead.
- **If the paper explicitly states "achieving state-of-the-art results" or equivalent SOTA language**, classify as: `paper-claimed SOTA; supported within evaluated baselines; not externally verified.` Do NOT write "the paper did not claim SOTA" when the paper clearly does.
- "first / 首个" is BANNED even when labeled speculative. Rewrite as: `potentially underexplored; requires literature search`.
- "novel / 全新" without external search: write `potentially novel direction (literature search required)`.
- Deployment claims without paper evidence:
  - No ONNX/TensorRT export test → write "requires export validation"
  - No edge-device test → write "edge deployment requires profiling"
  - No VRAM report → write "resource requirement must be profiled"

## Example

**Paper text:** "Our method achieves state-of-the-art results on the COCO benchmark."

**Correct classification:** `paper-claimed SOTA; supported within evaluated baselines; not externally verified.`

**Wrong classification:** "The paper did not explicitly claim SOTA" — this is incorrect when the paper clearly states "state-of-the-art".

## Enforcement

- Reports with unverified SOTA claims MUST have `partial` or `fail` on the SOTA claim safety row in the Quality Audit.
- Innovation ideas containing "first / 首个" MUST be rewritten before presentation, even if labeled speculative.
