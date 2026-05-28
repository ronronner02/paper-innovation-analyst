# Claude Maintainer Instructions

When maintaining this repository, preserve the core promise: help users analyze academic papers and generate concrete, evidence-grounded innovation points.

## Improvement rules

- Keep `SKILL.md` focused and actionable (target 100-180 lines).
- Do not remove the evidence-vs-inference distinction.
- Do not remove anti-fabrication rules.
- Do not remove Input Security Rules (prompt injection protection).
- Do not remove the Innovation Quality Gate (4/6 condition minimum).
- Prefer compact templates over bloated documents.
- Add examples only if they improve skill invocation or output quality.
- Validate changes with `python scripts/validate_skill.py .` and `python -m pytest tests/`.

## Useful maintenance tasks

1. Tighten the skill description so Claude triggers it for academic-paper analysis but not for unrelated summarization.
2. Add domain-specific addenda for additional fields beyond ML/CV, NLP/LLM, Systems, Robotics, and HCI.
3. Add example outputs using public-domain or synthetic paper summaries.
4. Improve the review rubric with more precise novelty criteria.
5. Keep installation instructions current with Claude's latest Skills interface.
6. Improve `scripts/extract_paper_assets.py` extraction quality and add new evidence channels.
7. Expand test fixtures with more domain-specific paper examples.

## Maintenance emphasis

- Keep hardware and deployment constraints explicit, especially for CV, object detection, remote sensing, and embedded deployment.
- Reject generic innovation points unless they specify layer/module changes, dataset pain points, loss/objective changes, metrics, and compute/deployment impact.
- Preserve GB/T 7714-2015 formatting requirements for generated reports with references.
- Maintain document ingestion pipeline's uncertainty labeling discipline.
- Keep security rules synchronized across SKILL.md, document-ingestion-pipeline.md, and supplementary parsing rules.
