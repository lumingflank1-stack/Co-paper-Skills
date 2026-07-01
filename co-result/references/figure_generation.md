# Figure Generation Guide

## When to Use

Use this guide when the user asks to call ChatGPT image generation, when `$co-result` is producing a full Results package, when virtual or assumed results are being prepared for manuscript drafting, when `$co-paper` is assembling a full manuscript, or when prompts for figure images are needed.

用户要求调用图片生成、`$co-result` 生成完整 Results 包、虚拟或假设结果进入论文撰写、`$co-paper` 组装全文，或需要图片 prompt 时，都使用本指南。

## Execution

Use the available ChatGPT image generation path by default (`imagegen` / GPT Image 2 when available). First parse the Results text and figure legends to enumerate every independent manuscript figure. Then generate one complete multi-panel bitmap per independent figure:

- `figures/Figure_1_<short_topic>.png`
- `figures/Figure_2_<short_topic>.png`
- `figures/Figure_3_<short_topic>.png`

Do not replace a full manuscript's figure set with a single global montage when the manuscript contains multiple independent figures. If the manuscript has Figure 1 through Figure 6, produce six independent image files. Do not leave project-referenced images only in the default generated-images directory. Copy final selected images into the project workspace.

After generation:

1. Update the manuscript Markdown so each `Figure N` has a local image link.
2. Save `figure_asset_manifest.md` with one row per figure: figure id, short topic, prompt source, saved path, linked in manuscript yes/no, inspection note.
3. If an image contains inaccurate long labels but the structure is useful, keep it only as a planning figure and state that final production figures must be redrawn with real data.

全文含多个独立 Figure 时，不要用一张总拼图代替。若全文包含 Figure 1 到 Figure 6，就生成 6 个独立图片文件，并写入全文链接和 `figure_asset_manifest.md`。

When the image generation path is unavailable, blocked, or the user requests text-only output, save both:

- `figure_generation_prompts.md`
- `figure_generation_blockers.md`

Do not silently downgrade full manuscript or virtual-result packages to prompt-only output.

## Prompt Structure

Use a structured prompt:

```text
Use case: scientific-educational
Asset type: biomedical manuscript Figure <N> complete multi-panel figure montage
Primary request: <one sentence summary>
Panel A: <schematic/result>
Panel B: <representative image/blot/flow/cell image>
Panel C: <quantification/plot>
Panel D: <orthogonal assay/integrative model>
Composition/framing: landscape figure, panel labels A-D, aligned grid, white background
Style/medium: clean biomedical vector-like illustration rendered as bitmap
Color palette: restrained, colorblind-aware, white background
Text constraints: short exact labels only
Avoid: clutter, invented logos, excessive text, exact unsupported statistics, dark background
```

## Panel Design

Use panel types that match evidence:

- Mechanism or workflow: schematic.
- Western blot or gel: representative schematic blot with lane labels.
- Quantification: bar, dot, box, violin, line, forest, or dose-response plot.
- Binding assay: sensorgram and equilibrium fit.
- Single-cell or omics: UMAP, heatmap, dot plot, volcano, pathway map, cell-cell axis.
- Animal/clinical endpoint: timeline, representative image, quantitative plot, survival or score plot.

## Text Accuracy

Keep in-image labels short. Generated image models may misspell long text. Put detailed explanation in the legend, not inside the figure.

Do not include exact p values, sample sizes, Kd, fold changes, or clinical numbers unless the user provided them or the prompt explicitly requested virtual numeric values. Use visual placeholders when planning:

- `Kd in nanomolar range`
- `normalized signal`
- `relative expression`
- `response (RU)`

## Inspection

After generation, inspect the image:

1. The image is nonblank.
2. All panels are present.
3. Panel labels match the manuscript.
4. Key labels are legible and not badly misspelled.
5. The visual claim does not exceed the text claim.

If text is inaccurate but structure is useful, keep the raw image as a planning figure and note that final production figures should be redrawn with real data.
