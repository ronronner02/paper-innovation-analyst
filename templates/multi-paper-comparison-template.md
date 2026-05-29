# Literature Synthesis and Innovation Report

When multiple papers are provided, this is the default template. Do NOT generate one full report per paper. Build synthesis, strong arguments, and innovation frameworks from the paper set.

---

## 0. Corpus Inventory

Perform this step FIRST, before any synthesis or innovation.

- Claimed paper count:
- Detected PDF/document count:
- Successfully parsed:
- Failed/unreadable:
- Duplicates:
- Out-of-domain papers:
- Missing files suspected:
- Proceed / stop decision:

Rules:
- If claimed count differs from detected count, report mismatch explicitly.
- If mismatch is significant, write: `Proceeding with detected papers only. Claimed count mismatch remains unresolved.`
- Do NOT write report titles claiming unverified paper counts.

## 0.5. Paper Tiering

Assign each paper a tier before synthesis:

| Tier | Meaning | Usage rule |
|---|---|---|
| Tier A | Core papers with method + experiment evidence | Can support strong arguments and innovation frameworks |
| Tier B | Relevant papers with partial evidence | Can support background or secondary mechanisms |
| Tier C | Weakly related or cross-domain papers | Use only as analogy or background |
| Excluded | Insufficient evidence or weak relevance | Do not use in final innovation |

| Paper ID | Tier | Reason |
|---|---|---|
|  |  |  |

Rules:
- Cross-domain papers (e.g., LLM architecture for image restoration) can only be `Tier C` with `cross-domain analogy` label unless there is an explicit mechanism mapping and experiment plan.
- Do NOT force Tier C or Excluded papers into the final innovation to appear comprehensive.
- The final innovation may use all, some, or only one paper depending on evidence strength and mechanism compatibility.

## 1. Corpus Overview

- Number of papers (verified):
- Main research domain:
- Core task:
- Time span:
- Main datasets:
- Main model families:
- Main evaluation metrics:
- Deployment or hardware context:

## 2. Paper Evidence Cards

Each paper gets a minimum-quality evidence card, NOT a full report. If a paper was only read at title/abstract level, mark: `Evidence insufficient for mechanism-level synthesis.`

| Paper ID | Title | Domain fit | Extraction confidence | Bibliographic verified | Method evidence | Formula/architecture evidence | Experiment evidence | Limitation evidence | Useful mechanism | Role in synthesis | Reason for use or exclusion |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  |

Domain fit: core / relevant / background / out-of-domain
Extraction confidence: high / medium / low
Role: core evidence / mechanism source / contrastive evidence / background / excluded

Do NOT use insufficiently parsed papers for strong arguments or core innovation support.

## 3. Research Problem Clustering

| Cluster | Papers | Shared problem | Why it matters | Remaining gap |
|---|---|---|---|---|
|  |  |  |  |  |

## 4. Method Family Map

| Method family | Papers | Core mechanism | Strength | Weakness | Compatible with |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## 5. Cross-paper Contradictions and Complementarities

| Finding | Supporting papers | Conflicting or missing evidence | Interpretation |
|---|---|---|---|
|  |  |  |  |

## 6. Strong Argument Construction

Strong arguments are NOT simple summaries. They are claims supported by multi-paper evidence that could be written into a paper's introduction, related work, or motivation section.

Rules:
- Strong arguments require at least 2 Tier A/B papers. If only 1 paper supports, it is a single-paper claim, NOT a cross-paper strong argument.
- Strong arguments MUST NOT be supported only by paper titles or abstracts.
- If cross-domain analogy is used, label: `cross-domain analogy, not direct evidence`.

### Argument 1: `<title>`

- **Argument:**
- **Supporting papers:**
- **Required evidence cards:**
- **Evidence maturity:**
  - directly supported
  - cross-paper inference
  - hypothesis
  - speculative
- **Why this is stronger than a single-paper claim:**
- **Which papers were not used and why:**
- **Possible counter-evidence:**
- **What must be experimentally verified:**
- **Weak argument downgrade:** If < 2 Tier A/B papers support this, label as `weak argument`.

Repeat for each strong argument.

## 7. Innovation Framework Recommendation

Innovation frameworks come from three sources. For each framework, specify the type:

### Type A: Single-paper Extension

Extending one paper's method at architecture, loss, training, data, or deployment level.

- **Base paper:**
- **Original mechanism:**
- **Identified weakness:**
- **Proposed modification:**
- **Layer/module/objective affected:**
- **Expected benefit:**
- **Experiment to validate:**
- **Compute/deployment impact:**

### Type B: Cross-paper Fusion

Fusing mechanisms, modules, assumptions, or experiment designs from two or more papers.

- **Source paper A:**
- **Source paper B:**
- **Optional source paper C:**
- **Mechanism borrowed from each:**
- **Compatibility analysis:**
  - Module compatibility (input/output tensor shapes):
  - Loss/training strategy compatibility:
  - Compute/deployment cost:
  - Additional data or annotation needed:
- **Conflict or mismatch:**
- **Proposed fused framework:**
- **Why fusion is non-trivial:**
- **Minimal viable experiment:**
- **Risk:**

### Type C: New Framework from Shared Gaps

Proposing an entirely new framework based on common problems exposed by the literature set.

- **Shared gap:**
- **Why existing papers do not solve it:**
- **New framework name:**
- **Core idea:**
- **Architecture-level design:**
- **Loss/objective design:**
- **Data or training strategy:**
- **Deployment consideration:**
- **Required evidence:**
- **Minimal viable experiment:**
- **Risk and fallback:**

### Evidence Maturity (for each framework)

| Component | Source paper | Evidence type | Maturity |
|---|---|---|---|
| Problem motivation | | direct / inference / hypothesis | |
| Mechanism A | | direct / inference / hypothesis | |
| Mechanism B | | direct / inference / hypothesis | |
| Fusion design | | hypothesis / speculative | |
| Deployment claim | | measured / assumed / unknown | |

### Mechanism Compatibility Check (for each cross-paper fusion)

- Tensor shape compatibility:
- Feature domain compatibility:
- Loss/objective compatibility:
- Training conflict risk:
- Compute/FLOPs risk:
- Memory/VRAM risk:
- Deployment/operator risk:
- Dataset/protocol compatibility:
- Minimal integration test:

Rules:
- Cross-paper fusion MUST NOT just say "combine A and B"; must explain how mechanisms connect.
- If tensor/feature/loss/training compatibility cannot be explained, lower feasibility score.
- All deployment judgments must be labeled `measured` or `requires validation`.
- All resource estimates must be labeled `assumption` unless backed by profiling.

## 8. Paper Usage Decision

Explain which papers are used, partially used, or excluded in the final innovation. Do not force every paper into the final argument. If a paper weakens coherence, mark it as background, weak relevance, or excluded. The final framework may use all, some, or only one paper depending on evidence strength, relevance, and mechanism compatibility.

| Paper | Used in final argument? | Used in innovation framework? | Role | Reason |
|---|---|---|---|---|
|  |  |  |  |  |

Role options:
- **core evidence** — directly supports the main argument
- **mechanism source** — provides a module or technique used in the framework
- **contrastive evidence** — provides counter-evidence or failure case
- **background** — provides context only
- **excluded due to weak relevance**
- **excluded due to insufficient evidence**

## 9. Recommended Final Direction

Output 1–3 strongest research directions.

### Direction 1: `<title>`

- **One-sentence thesis:**
- **Core supporting papers:**
- **Proposed framework:**
- **Why this is novel:**
- **Why this is feasible:**
- **Key experiment:**
- **Main risk:**
- **Backup plan:**

## 10. References

Use GB/T 7714-2015 formatting. See `references/gbt7714-2015-examples.md`. Do not fabricate missing bibliographic metadata.

## 11. Quality Audit

### Report Quality

| Check | Status: pass / partial / fail | Evidence | Required fix |
|---|---|---|---|
| Corpus count matches detected files |  |  |  |
| Each used paper has sufficient evidence card |  |  |  |
| Bibliographic fields verified for all cited papers |  |  |  |
| Strong arguments supported by multiple Tier A/B evidence cards |  |  |  |
| Innovation frameworks include mechanism compatibility check |  |  |  |
| SOTA claims classified (paper-claimed / supported within baselines / externally verified) |  |  |  |
| "first / 首个" not present even as speculative |  |  |  |
| Engineering claims labeled as assumptions unless measured |  |  |  |
| No unsupported first/SOTA/deployment-ready/real-time claims |  |  |  |
| References follow GB/T 7714-2015 or missing metadata marked |  |  |  |
| Paper tiering completed before synthesis |  |  |  |
| Cross-domain papers labeled as analogy, not direct evidence |  |  |  |
| No Chinese banned words (首个/首次/第一个/完全兼容/实时/零开销/ONNX兼容性好/单GPU 8GB+/VRAM 2-4GB/4K <200ms) |  |  |  |

### Paper Evidence Quality

| Check | Status: pass / partial / fail | Evidence |
|---|---|---|
| Tier A papers provide hardware/latency evidence |  |  |
| Tier A papers provide ablation of core components |  |  |
| Tier A papers provide export/runtime validation |  |  |

Do NOT default all checks to `pass`. If missing metadata exists, reference check is `partial` at most. If corpus count mismatch, corpus check is `fail` or `partial`.
