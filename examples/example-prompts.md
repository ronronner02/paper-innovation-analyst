# Example Prompts

## Quick Summary

```text
Use paper-innovation-analyst to summarize this paper. Focus on the problem, method, experiments, and main contributions.
```

## Innovation Mining

```text
Read this paper and generate 5 concrete innovation points. For each idea, include the technical route, experiments, baselines, metrics, feasibility, novelty, and risk.
```

## Deep Learning Project Direction

```text
I want to turn this paper into a deep learning internship project. Analyze its limitations and propose a 4-week implementation plan with milestones.
```

## Multi-paper Comparison

```text
Compare these three papers. Build a comparison matrix and propose one thesis-level research direction that synthesizes them.
```

## Reviewer-style Critique

```text
Act as a reviewer. Critique the novelty, technical soundness, baselines, evaluation protocol, and missing ablations of this paper.
```

## Reproduction Plan

```text
Turn this paper into a PyTorch reproduction plan. Identify required datasets, implementation modules, baselines, expected metrics, and ablation experiments.
```

## Literature Gap Search Preparation

```text
Based on this paper, list the exact related-work questions I should verify through literature search before claiming novelty.
```


## Hardware-aware CV / Detection Prompt

Analyze this YOLO-style small-object detection paper for VisDrone or remote-sensing data. Do not give generic ideas. For every innovation point, specify the affected backbone/neck/head layer, loss or assignment change, dataset-specific pain point, expected mAP/FPS/VRAM effect, and deployment feasibility on an embedded board.

## Deployment-constrained Experiment Prompt

Turn this paper into an experiment plan for a single 8GB or 12GB GPU and a target edge device. Include VRAM estimates, OOM fallbacks, loss-divergence debugging steps, ONNX/TensorRT export risks, and GB/T 7714-2015 references.

## Single Paper Deep Analysis

```text
Analyze this paper from its own technical perspective. Identify its method, formula design, framework diagram implications, limitations, and single-paper extension opportunities.
```

## Literature Synthesis (Multiple Papers)

```text
Analyze this batch of papers as a literature set. Do not generate separate full reports for each paper. Build a synthesis, identify strong arguments, and recommend innovation frameworks that may extend one paper, fuse multiple papers, or propose a new framework from shared gaps.
```

## Selective Paper Usage

```text
Use these papers as a corpus. You may use all papers or select only the most relevant ones. Explain which papers support the final argument, which provide mechanisms, and which are excluded.
```

## Framework Innovation from Literature

```text
Based on this literature set, recommend 2–3 research frameworks. Each framework can be a single-paper extension, a cross-paper fusion, or a new framework derived from shared unresolved gaps.
```
