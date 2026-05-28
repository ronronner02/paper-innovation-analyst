# Literature Synthesis and Innovation Report

When multiple papers are provided, this is the default template. Do NOT generate one full report per paper. Build synthesis, strong arguments, and innovation frameworks from the paper set.

---

## 1. Corpus Overview

- Number of papers:
- Main research domain:
- Core task:
- Time span:
- Main datasets:
- Main model families:
- Main evaluation metrics:
- Deployment or hardware context:

## 2. Paper Evidence Cards

Each paper gets a concise evidence card, NOT a full report. Only include information valuable for the final synthesis.

| Paper | Problem | Core method | Key evidence | Limitation | Relevance to synthesis |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

Relevance labels:
- **core evidence** — directly supports the final argument
- **mechanism source** — provides a reusable module or technique
- **contrastive evidence** — shows what does NOT work or provides counter-evidence
- **background** — provides context but not directly used in innovation
- **weak relevance** — marginal connection to the synthesis
- **excluded** — insufficient evidence or too weak to include

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

### Argument 1: `<title>`

- **Argument:**
- **Supporting papers:**
- **Evidence type:** direct evidence / cross-paper inference / hypothesis
- **Why stronger than single-paper claim:**
- **Possible weakness:**
- **How to verify experimentally:**

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
