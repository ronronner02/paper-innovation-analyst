# Strong Argument and Research Positioning Template

Use this template when synthesizing multiple papers into thesis-level arguments for writing, positioning, or innovation design.

---

## 1. Claim

- **Strong argument:**
- **Claim type** (select one):
  - empirical — based on consistent experimental findings across papers
  - architectural — based on structural patterns or design choices
  - methodological — based on shared methodological limitations or opportunities
  - deployment-oriented — based on efficiency, hardware, or deployment gaps
  - dataset/evaluation-oriented — based on benchmark, metric, or evaluation gaps
  - theoretical — based on formal analysis or proven properties

## 2. Evidence Base

| Evidence | Paper | What it supports | Strength | Limitation |
|---|---|---|---|---|
|  |  |  |  |  |

Strength labels:
- **strong** — multiple consistent results, well-controlled experiments
- **moderate** — clear result but limited scope or single dataset
- **weak** — suggestive but not conclusive
- **indirect** — supports the argument indirectly through related findings

Rules:
- At least 2 Tier A/B papers required for a strong argument. If < 2, label as `weak argument`.
- If cross-domain analogy is used, label: `cross-domain analogy, not direct evidence`.
- Arguments must NOT be supported only by titles or abstracts.

## 3. Cross-paper Reasoning

- What paper A shows:
- What paper B shows:
- What paper C adds:
- What remains unresolved:
- What can be inferred:
- What is still only a hypothesis:

## 4. Why This Is Stronger Than a Single-paper Argument

- Broader evidence:
- Complementary mechanisms:
- Consistent failure pattern:
- Shared unresolved problem:
- Practical relevance:

## 5. Innovation Implication

- What kind of innovation this argument supports:
- Architecture implication:
- Loss/objective implication:
- Dataset/evaluation implication:
- Deployment implication:

## 6. Verification Plan

- Minimal experiment:
- Baseline:
- Dataset:
- Metric:
- Expected result:
- Failure signal:

## 7. Writing-ready Version

Output a paragraph that could be placed in a paper's introduction, related work, or motivation section. Provide both Chinese and English versions if requested.

### English version

```
[Draft paragraph for paper introduction / related work / motivation]
```

### 中文版本

```
[可放入论文引言 / 相关工作 / 研究动机的段落草稿]
```

## 8. Evidence Maturity

| Evidence source | Paper | Maturity |
|---|---|---|
|  |  | directly supported / cross-paper inference / hypothesis / speculative |

## 9. SOTA Classification

If this argument makes SOTA-type claims, classify:

- `paper-claimed SOTA` — the paper itself claims SOTA
- `supported within evaluated baselines` — outperforms tested baselines only
- `externally verified SOTA` — confirmed by independent external search

## 10. Quality Audit

### Report Quality

| Check | Status: pass / partial / fail | Evidence |
|---|---|---|
| At least 2 Tier A/B papers support this argument |  |  |
| Bibliographic fields verified for all cited papers |  |  |
| No unsupported first/SOTA/deployment-ready claims |  |  |
| SOTA claims classified (paper-claimed / supported within baselines / externally verified) |  |  |
| "first / 首个" not present even as speculative |  |  |
| Cross-domain analogy labeled correctly |  |  |
| Evidence cards exist for all cited papers |  |  |
| No Chinese banned words (首个/首次/第一个/完全兼容/实时/零开销/ONNX兼容性好/单GPU 8GB+/VRAM 2-4GB/4K <200ms) |  |  |

### Paper Evidence Quality

| Check | Status: pass / partial / fail | Evidence |
|---|---|---|
| Supporting papers provide hardware/latency evidence |  |  |
| Supporting papers provide ablation of core components |  |  |

## 11. References

Use GB/T 7714-2015 formatting. See `references/gbt7714-2015-examples.md`. Do not fabricate missing bibliographic metadata.
