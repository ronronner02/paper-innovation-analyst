# Changelog

## v0.5.5-beta — 2026-05-29

### Added

- **Cross-platform quality alignment** between Claude Skill and Codex Adapter.
- **Codex report depth requirements** to avoid overly shallow reports. Codex single-paper reports must include 15 minimum sections (Bibliographic Verification through Quality Audit).
- **Shared Claim Safety, Table Identity, Ablation Integrity, and Quality Audit rules** across both platforms.
- **Chinese strong-claim trigger detection**: 首个, 首次, 第一个, 首次提出, 全新, 完全兼容, 实时, 零开销, ONNX兼容性好, 部署完全兼容, 单GPU 8GB+, VRAM 2-4GB, 4K <200ms, 8GB显存, 单卡8GB.
- **Report version consistency checks** in templates and quality audit.
- **Ablation table integrity enhancements**: fixed/changed variables, final configuration distinction, delta recalculation, kernel-size context rules.
- **Platform positioning documentation** in README.md and codex/AGENTS.md.
- **Innovation point depth requirements** for Codex: each idea must include technical route, mechanism compatibility, deployment risk, minimal experiment, failure criteria.
- **tests/test_cross_platform_alignment.py**: cross-platform alignment tests.
- **tests/test_report_claim_safety.py**: claim safety tests including Chinese trigger words.
- **tests/test_codex_depth_profile.py**: Codex report depth profile tests.

### Changed

- Claude reports retain deep analysis but must downgrade unverified deployment and novelty claims.
- Codex reports must include technical routes, compatibility checks, minimal experiments, and quality audits instead of direction-only summaries.
- Innovation templates now require evidence level, mechanism compatibility, deployment risk, and validation plan.
- Experiment plan template now includes Claim Safety Check section.
- codex/checklists/sota-claim-safety.md now includes Chinese trigger words.
- codex/checklists/quality-audit.md now includes Chinese banned words and ablation integrity checks.
- codex/prompts/validate-report-quality.md now scans for Chinese trigger words.

### Fixed

- Reduced unsupported "first/首个/首次", ONNX/TensorRT, real-time, VRAM, and latency claims.
- Reduced ablation-table context errors such as kernel-size and final-configuration misinterpretation.
- Release packages now exclude cache, bytecode, old dist, nested zip, and nested skill artifacts.
- CI now explicitly validates both Claude Skill and Codex Adapter packages.

## v0.5.4-beta — 2026-05-29

### Added

- **Bibliographic Verification Gate** (rule 8): every cited paper must verify Title, Authors, Year, Venue, DOI against provided material. Unverified fields must be marked explicitly.
- **Table Identity Gate** (rule 9): every experimental table must specify Table ID, noise setting, metric, dataset. Do NOT re-label table results.
- **SOTA Claim Classification** (rule 10): SOTA claims classified as `paper-claimed SOTA` / `supported within evaluated baselines` / `externally verified SOTA`. Without external search, do NOT write `externally verified SOTA`.
- **first/首个 banned even as speculative**: rewrite as `potentially underexplored; requires literature search`.
- **Quality Audit two-distinction**: templates now distinguish "Report Quality" from "Paper Evidence Quality" in all audits.
- **Codex Adapter** (`codex/` directory): Codex CLI entry points with AGENTS.md, task-specific prompts, and verification checklists.
- **Root AGENTS.md**: Codex auto-entry point referencing codex/AGENTS.md.
- **codex/prompts/validate-report-quality.md**: report quality self-check prompt.
- **codex/README.md**: Codex adapter documentation.
- **scripts/package_codex_adapter.py**: packaging script for Codex adapter archive.
- **tests/test_codex_adapter.py**: tests for Codex adapter structure and v0.5.4 gates.

### Changed

- Quality Audit in all templates split into Report Quality and Paper Evidence Quality sections.
- Evidence cards in multi-paper template now include Bibliographic verified column.
- Innovation brief template includes SOTA classification field per idea.
- Strong argument template includes SOTA Classification section.
- `validate_skill.py` checks v0.5.4 gates and codex adapter structure.
- CI workflow includes `package_codex_adapter.py` compile and packaging check.

## v0.5.3-beta — 2026-05-28

### Added

- **Evidence Strength / Claim Safety rules** for single-paper and innovation reports. Any claim containing trigger words (first, novel, SOTA, fully compatible, ONNX compatible, deployment-ready, real-time, negligible FLOPs, specific VRAM, etc.) must be labeled with an evidence level (1-5) and validated before inclusion.
- **Two-pass Literature Synthesis** workflow for batch paper analysis: Pass 0 (Corpus Inventory) detects paper-count mismatches before synthesis; Pass 1 (Evidence Card Construction) requires minimum-quality cards for all papers; Pass 2 (Synthesis and Innovation) only proceeds after Pass 0 and 1 are complete.
- **Corpus Inventory** step to detect paper-count mismatches before synthesis.
- **Paper Tiering** (A/B/C/Excluded) and minimum evidence card requirements for batch analysis.
- **Evidence Maturity** table for innovation frameworks: tracks whether each component is direct/inference/hypothesis/speculative.
- **Mechanism Compatibility Check** for cross-paper innovation frameworks: tensor shape, feature domain, loss, training conflict, compute, memory, deployment, and dataset compatibility.
- **Three-state Quality Audit**: pass / partial / fail across all templates (replaces checkbox-only self-checks).
- **Ablation Table Integrity Check** in single-paper analysis template.
- **Claim Safety Check** in innovation-brief and paper-analysis templates.
- **Example prompts** for strict evidence mode and no-strong-claims batch analysis.

### Changed

- Batch mode now delays innovation generation until corpus inventory and evidence cards are complete.
- Strong arguments require multiple Tier A/B evidence cards or must be downgraded to `weak argument`.
- Engineering and deployment claims must be labeled as assumptions unless measured by the paper.
- Quality self-checks use pass / partial / fail instead of only checkboxes.
- Cross-domain papers (e.g., LLM architecture for image restoration) must be labeled as `cross-domain analogy`.

### Fixed

- Reduced risk of unsupported "first", "SOTA", "fully compatible", "real-time", and exact resource-estimate claims.
- Reduced risk of misleading ablation-table summaries (selected rows without noting omitted rows).
- Reduced risk of paper-count mismatch in batch mode reports.

## v0.5.2-beta — 2026-05-28

### Added

- **Paper Set Routing Logic**: SKILL.md now distinguishes single-paper analysis from multi-paper literature synthesis. Multiple papers default to `literature_synthesis_and_innovation`, NOT per-paper full reports.
- **Literature Synthesis Template**: `templates/multi-paper-comparison-template.md` completely rewritten with: Paper Evidence Cards, Research Problem Clustering, Method Family Map, Strong Argument Construction, Innovation Framework Recommendation (Type A: single-paper extension, Type B: cross-paper fusion, Type C: new framework from shared gaps), Paper Usage Decision table.
- **Strong Argument Template**: `templates/strong-argument-template.md` for thesis-level positioning from multiple papers, with claim type, evidence base, cross-paper reasoning, innovation implication, and writing-ready paragraph output.
- **Framework Source Type**: `templates/innovation-brief-template.md` now requires each innovation idea to declare its source type (single-paper extension / cross-paper fusion / new framework from shared gaps / engineering deployment / dataset/evaluation / loss/objective / architecture).
- **Cross-paper Fusion Compatibility Check**: Innovation template now checks module compatibility, loss/training strategy compatibility, compute cost, and additional data requirements for cross-paper fusion ideas.
- **Example Prompts**: Added single-paper deep analysis, literature synthesis, selective paper usage, and framework innovation prompts.
- **README**: Added Single Paper vs Literature Set Behavior section.
- **Validator**: Added checks for Paper Set Routing Logic, strong-argument-template.md, multi-paper template sections (Strong Argument Construction, Innovation Framework Recommendation, Paper Usage Decision, Paper Evidence Cards), and innovation template Framework Source Type.
- **Tests**: Added `TestLiteratureSynthesisRouting` class with 15 tests covering routing logic, template content, and new file existence.

### Changed

- Phase 7 renamed to "Paper Set Routing and Synthesis" with explicit hierarchy for multi-paper analysis.
- Phase 8 output selection now distinguishes single-paper vs multi-paper defaults with specific format names.
- Multi-paper comparison template now prioritizes synthesis, argument construction, and innovation design over batch summary.

### Fixed

- Synchronized packaging tests with the v0.5.2-beta artifact names; tests now use dynamic version lookup via `DEFAULT_VERSION` constant instead of hardcoded strings.
- Corrected GB/T 7714-2015 journal examples so the Journal [J] section does not contain monograph [M] entries.
- Strengthened validator checks for GB/T reference-type section consistency (Journal section must not contain [M], [C], [D]).

### Clarified

- Multiple-paper synthesis may use all, some, or only one of the provided papers depending on evidence strength, relevance, and mechanism compatibility.
- The Skill should not force weakly related papers into the final argument or innovation framework.
- README now explicitly states: one paper → single-paper deep analysis; multiple papers → literature synthesis, strong argument construction, innovation framework recommendation.

## v0.5.1-beta — 2026-05-28

### Fixed

- Removed local Claude settings, Git metadata, caches, bytecode, and stale build artifacts from release packages.
- Added release-mode validation (`--release`) for clean package checks.
- Corrected and expanded GB/T 7714-2015 formatting examples: fixed [J]/[C] mismatch, added Chinese journal/conference examples, added dataset online resource examples, added `Missing metadata` format, added disclaimer.
- Removed unaudited README tested-environment TODOs and claims.
- CI now compiles scripts, validates the Skill, runs pytest, packages release artifacts, and performs unpack-and-release-check.

### Added

- Versioned `.skill` and `.zip` package generation with `--version` and `--dist` flags.
- `--release` mode on `validate_skill.py` that rejects `.git/`, `.pytest_cache/`, `__pycache__/`, `*.pyc`, `.claude/settings.local.json`, `outputs/`, nested `.zip`/`.skill`, `.DS_Store`, `.env`, `.venv/`.
- OCR mode controls: `--ocr-mode auto|all|none` and `--ocr-text-threshold`.
- OCR confidence metadata (`ocr_confidence_mean`, `ocr_confidence_min`, `ocr_low_confidence`) where available.
- Native-text then OCR fallback for reference candidate extraction with `reference_source` manifest field.
- Stable manifest schema: `input_file`, `created_at`, `extractor_version`, `capabilities`, `warnings`, `pages`, `reference_source`, `outputs`.
- `tests/test_validator_release_mode.py` — release mode validation tests.
- `tests/test_packaging_cleanliness.py` — packaging output and archive cleanliness tests.
- `tests/test_extract_paper_assets_smoke.py` — extractor CLI and manifest schema smoke tests.

### Clarified

- `references/document-ingestion-pipeline.md` now has explicit "Implemented by current helper script" and "Not implemented directly" sections.
- Document extraction is best-effort and does not guarantee perfect parsing of complex PDFs, scanned pages, formulas, figures, charts, tables, multi-column order, or supplementary packages.

## v0.5.0-document-ingestion — 2026-05-27

### Added

- **Document ingestion pipeline**: `references/document-ingestion-pipeline.md` defines 8 evidence channels — PDF layout parsing, OCR for scanned papers, table structure extraction, mathematical formula recognition, image/figure/chart semantic analysis, automatic reference parsing, multi-column paper reconstruction, supplementary material parsing.
- **Paper asset extraction script**: `scripts/extract_paper_assets.py` provides best-effort extraction of native PDF text blocks, OCR text (via pytesseract/Tesseract), tables (via pdfplumber), images (via PyMuPDF), equation candidates, reference candidates, and per-page metadata. Gracefully degrades when optional dependencies are unavailable.
- **`requirements-optional.txt`**: Lists optional Python dependencies (pymupdf, pdfplumber, pillow, pytesseract) for the extraction script.
- **Evidence coverage tracking**: `templates/paper-analysis-template.md` now includes Section 1A (Evidence Coverage and Extraction Status) and Section 1B (Formula, Figure, and Table Evidence) with uncertainty labels.
- **SKILL.md Document Ingestion Scope**: Updated capability boundaries to reference the optional extraction pipeline and document-ingestion-pipeline.md. Phase 1 now mentions extracted assets. Phase 2 now includes formula/figure/table/reference/supplementary extraction fields.
- **Security rules updated**: Input Security Rules now treat extracted assets as untrusted research material.
- **Validator updated**: `scripts/validate_skill.py` now checks for document-ingestion-pipeline.md, extract_paper_assets.py, requirements-optional.txt, evidence coverage in paper-analysis template, and 8 evidence channels in the ingestion pipeline.

### Changed

- SKILL.md description expanded to mention evidence-aware analysis of formulas, tables, figures, references, scanned pages, and supplementary material.
- README.md updated with new repository layout, capability boundary, and extract_paper_assets.py usage instructions.

## v0.4.0-security-and-reproducibility-hardening — 2026-05-27

### Security

- **Input Security Rules added to SKILL.md**: All paper content, PDFs, supplementary material, code repositories treated as untrusted research material. Embedded instructions that attempt to change Claude's behavior are ignored. Prompt injection protection documented.
- **`.gitignore` added**: Excludes `.claude/settings.local.json`, `__pycache__`, `.env`, build artifacts.
- **Sensitive file check**: Validator rejects `.claude/settings.local.json` in repository.

### Changed

- **SKILL.md compressed**: Restructured from ~300 lines to ~110 lines. Detailed content migrated to reference files. Core workflow preserved with all 8 phases.
- **Dynamic output defaults (Phase 8)**: Default output now adapts to user intent — `brief` for summaries, `innovation_brief` for limitations/gaps, `experiment_plan` for implementation, `comparison_matrix` for multiple papers, `reviewer_report` for review requests.
- **Capability boundaries declared**: SKILL.md and README.md now explicitly state the Skill does not implement PDF parsing, OCR, table extraction, or formula recognition.
- **Innovation Quality Gate**: Every idea must satisfy 4/6 conditions (concrete limitation, affected module, measurable metric, minimal experiment, baseline, compute impact). Failed ideas are rejected or rewritten.
- **Anti-generic check strengthened**: Banned expressions like "add attention mechanism", "use transformer", "improve robustness" unless accompanied by layer-level specification, formulas, experiments, and deployment cost.
- **GB/T 7714-2015 example file created**: `references/gbt7714-2015-examples.md` with format examples for journal [J], conference [C], thesis [D], monograph [M], arXiv, web [EB/OL], GitHub, datasets, multi-author format, DOI/URL handling, and missing field rules.
- **CV detection addendum created**: `references/cv-detection-addendum.md` with YOLO-style detection checklist covering backbone, neck, head, assignment, loss, dataset-specific pain points, and deployment constraints.
- **Idea quality gates reference created**: `references/idea-quality-gates.md` with scoring examples and anti-generic rules.
- **experiment-plan-template.md enhanced**: Added Reproducibility and Experiment Logging section (git commit, config, seeds, environment, dataset checksum, training/eval commands, logging backend, checkpoint policy). Strengthened ablation matrix with Failure signal and Debug action columns. Expanded Failure Criteria to cover 12 failure modes with specific diagnosis plans and fallbacks.
- **multi-paper-comparison-template.md enhanced**: Added Related-work Positioning Map, Chronological Development, and Cross-paper Innovation Opportunities sections.
- **README.md updated**: Removed unverified "Tested with Claude 4.x" claim. Added capability boundaries section. Updated repository layout. Added test instructions.
- **validate_skill.py rewritten**: Added checks for security rules, capability boundaries, dynamic defaults, quality gate references, anti-fabrication in all templates, GB/T 7714-2015 in all templates, .gitignore content, sensitive file exclusion, README claim validation.

### Added

- `references/gbt7714-2015-examples.md` — GB/T 7714-2015 citation format examples
- `references/cv-detection-addendum.md` — CV/object detection analysis requirements
- `references/idea-quality-gates.md` — Innovation idea quality gates and scoring reference
- `.gitignore` — Git ignore rules
- `tests/test_validate_skill.py` — pytest test suite for validation
- `tests/fixtures/toy-cv-paper.md` — CV detection paper test fixture
- `tests/fixtures/toy-llm-paper.md` — LLM paper test fixture
- `tests/fixtures/prompt-injection-paper.md` — Security test fixture with embedded injection attempts
- `tests/expected/cv-analysis-checklist.md` — Expected CV analysis output checklist
- `tests/expected/security-behavior-checklist.md` — Expected security behavior checklist

## v0.3.0 — 2026-05-27

### Fixed

- **validate_skill.py dead code bug**: v0.2 hardening checks were placed after `raise SystemExit()` and never executed. Integrated into `validate_hardening()` function.

### Changed

- SKILL.md description tightened to exclude simple summaries.
- Scoring examples added for Feasibility/Novelty/Risk (1/3/5).
- Domain addenda framework added.
- paper-analysis-template.md: Added Quality Self-Check section.
- multi-paper-comparison-template.md: Added dynamic column support and hardware/deployment row.
- reviewer-report-template.md: Expanded to 6 technical concern sub-sections.

### Added

- `references/domain-addenda.md`: ML/CV, NLP/LLM, Systems, Robotics, HCI addenda.
- `CHANGELOG.md`

## v0.2.0

### Added

- Mandatory hardware/deployment limitation mining
- VRAM/RAM/FLOPs/MACs/latency/operator-support checks
- Layer-level and dataset-specific innovation requirements for CV/detection
- Ablation compute-cost estimates
- Direct fallbacks for loss divergence, NaN/Inf, training collapse, GPU OOM, export failure
- GB/T 7714-2015 citation and reference formatting requirement

## v0.1.0

### Added

- Initial SKILL.md with 8-phase workflow
- Templates: paper-analysis, innovation-brief, experiment-plan, multi-paper-comparison, reviewer-report
- Review rubric with 12 scoring dimensions
- Example prompts
- Validation script
- README with installation instructions
