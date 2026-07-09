# Result Writing Guide

## Purpose

Use this guide when drafting a Chinese biomedical Results section from experiment designs, partial results, actual results, assumed-positive findings, or explicitly requested simulated findings.

## Result Logic

For each experiment, extract:

1. The biological question.
2. The assay or dataset.
3. The sample or model.
4. The comparison.
5. The expected or observed direction.
6. The figure panel.
7. The claim strength.
8. The source mode: input, assumed, simulated, or requirements-only.

For each module, also extract:

1. Module relationship: standalone, parallel, progressive upstream, or progressive downstream.
2. Node-discovery layer: the omics, public-data, screen, high-throughput assay, or broad experiment that found the new node/readout.
3. Validation layer: the perturbation of the upstream/input side and the downstream/output readout.
4. Rescue layer when testing a mediator.
5. Layer status: real, partial, assumed, simulated with approval, requirements-only, or missing.

Write in the order of evidence, not in the order of experimental operations when the logic would read better otherwise. A common order is:

1. Rationale or model panel.
2. Node-discovery assay or analysis.
3. Quantification or candidate selection.
4. Perturbation validation with downstream readout.
5. Rescue or orthogonal validation when the claim requires it.
6. Integrative conclusion and boundary.

## Chinese Style

Use compact manuscript language:

- Prefer `结果显示`, `进一步`, `与此一致`, `提示`, `支持`, `说明`.
- Avoid grant-like language such as `我们拟`, `本课题将`, `具有重大意义`.
- Avoid Discussion-heavy interpretation in Results. Short mechanistic linking is allowed when needed to explain why panels are grouped.

## Panel Citation

Index each result with figure panels in the body:

- Single panel: `（Figure 1A）`
- Multiple panels: `（Figure 1A-D）`
- Cross-figure synthesis: `（Figure 1D, Figure 2C）`

Mention a panel the first time the evidence is described, not only at paragraph endings.

## Claim Strength

Use direct claim language only when the assay supports it:

| Evidence type | Appropriate claim | Avoid |
|---|---|---|
| Co-IP | `处于同一复合物或相邻蛋白复合体中` | `直接结合`, unless purified binding also shown |
| SPR/BLI/ITC with purified proteins | `发生直接亲和结合` | `证明体内机制`, unless paired with in vivo evidence |
| Representative Western blot | `可检测到`, `显示富集` | `显著`, unless quantified |
| Quantification with replicates | `显著升高/降低` | exact P if not available |
| Schematic | `模型示意`, `提出工作模型` | `证明` |
| Transcriptomics correlation | `相关`, `一致`, `候选轴` | `导致`, `驱动`, unless perturbation evidence exists |
| Omics or screen discovery only | `筛选得到`, `提示候选节点`, `优先验证对象` | `证明关键机制`, unless validation also shown |
| Upstream perturbation plus downstream readout | `支持该上游因素调控下游表型/通路` | `证明中介`, unless rescue is shown |
| Mediator perturbation plus rescue | `支持该节点作为中介环节` | `完全解释`, unless alternatives are ruled out |

## Missing Numeric Details

If the user did not provide sample size, exact P value, fold change, Kd, confidence interval, or software fit output:

- Write directionally in the Results.
- Use placeholders sparingly in notes, not in polished body text.
- Mark exact values as to be replaced after real data are available.

## Biological Boundary Note

When a family member is mentioned but not directly assayed, keep it as a candidate or related molecule. For example, if only SV2A is validated, write SV2B as `候选延伸对象` or `同家族相关分子`, not as a proven binding target.
