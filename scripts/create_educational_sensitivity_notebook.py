#!/usr/bin/env python3
"""Create the educational sensitivity-analysis notebook."""

from pathlib import Path

import nbformat as nbf


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "notebooks" / "01_educational_sensitivity_analysis.ipynb"

nb = nbf.v4.new_notebook()
nb["metadata"]["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
nb["metadata"]["language_info"] = {"name": "python", "version": "3.10"}

cells = []
cells.append(nbf.v4.new_markdown_cell("""# From qualitative appearance to quantitative measurement

This notebook uses 12 **deterministic synthetic panels** to show how a visual observation becomes a computational variable—and how preprocessing and segmentation choices change derived measurements.

It does **not** estimate treatment effects, segmentation accuracy, biological abundance, viability, or mechanism. Each panel is an illustrative measurement case, not a biological replicate.
"""))
cells.append(nbf.v4.new_markdown_cell("""## Learning goals

1. Translate a qualitative observation into an operational measurement.
2. Compare reasonable analysis configurations.
3. Measure mask agreement without calling any mask “ground truth.”
4. Visualize how object count, area fraction, and object size depend on analysis choices.
5. Identify the manifest, controls, experimental units, and validation needed for a scientific study.
"""))
cells.append(nbf.v4.new_code_cell("""from pathlib import Path
import os, sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

PROJECT_ROOT = Path.cwd()
if not (PROJECT_ROOT / 'src').exists():
    PROJECT_ROOT = PROJECT_ROOT.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.segmentation import load_image, extract_channel
from src.sensitivity import default_educational_configs, mask_iou, segment_with_config, summarize_configuration
from src.synthetic import generate_synthetic_dataset

default_data = PROJECT_ROOT / 'data' / 'synthetic_panels'
DATA_DIR = Path(os.environ.get('JMM_DATA_DIR', default_data))
OUTPUT_DIR = Path(os.environ.get('JMM_EDU_OUTPUT_DIR', PROJECT_ROOT / 'results' / 'educational_sensitivity'))
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

metadata_path = DATA_DIR / 'metadata_fig34.csv'
if not metadata_path.exists():
    if DATA_DIR == default_data:
        generate_synthetic_dataset(DATA_DIR)
    else:
        raise FileNotFoundError('JMM_DATA_DIR must contain metadata_fig34.csv and matching PNG files.')
metadata = pd.read_csv(metadata_path)
configs = default_educational_configs()
print(f'{len(metadata)} illustrative panels; {len(configs)} analysis configurations')
"""))
cells.append(nbf.v4.new_markdown_cell("""## Run the configuration sweep

The output contains one row per **panel × configuration**. The default images are deterministic synthetic teaching cases and have no biological meaning. Authorized legacy panels may be supplied through `JMM_DATA_DIR` for private provenance work.
"""))
cells.append(nbf.v4.new_code_cell("""rows = []
masks = {}
channels = {}
for _, record in metadata.iterrows():
    image = load_image(DATA_DIR / record['file_name'])
    green = extract_channel(image, 'green')
    channels[record['image_id']] = green
    for config in configs:
        row = summarize_configuration(green, config)
        row.update({column: record[column] for column in metadata.columns})
        _, mask, _, _ = segment_with_config(green, config)
        masks[(record['image_id'], config.name)] = mask
        rows.append(row)

results = pd.DataFrame(rows)
results.to_csv(OUTPUT_DIR / 'panel_configuration_metrics.csv', index=False)
results[['image_id','panel','name','n_objects','positive_area_fraction','mean_object_area','max_object_area']].head(12)
"""))
cells.append(nbf.v4.new_markdown_cell("""## Agreement with a reference configuration

Intersection-over-union (IoU) quantifies how similar two masks are. The historically recovered configuration is used only as a computational reference. IoU measures **agreement, not accuracy**, because no expert ground truth is available.
"""))
cells.append(nbf.v4.new_code_cell("""agreement_rows = []
for image_id in metadata['image_id']:
    reference = masks[(image_id, 'submitted_branch')]
    for config in configs:
        agreement_rows.append({
            'image_id': image_id,
            'configuration': config.name,
            'iou_with_submitted_branch': mask_iou(reference, masks[(image_id, config.name)]),
        })
agreement = pd.DataFrame(agreement_rows)
agreement.to_csv(OUTPUT_DIR / 'mask_agreement.csv', index=False)

order = [c.name for c in configs]
plt.figure(figsize=(10, 4.8))
sns.boxplot(data=agreement, x='configuration', y='iou_with_submitted_branch', order=order, color='#8FB9DF')
sns.stripplot(data=agreement, x='configuration', y='iou_with_submitted_branch', order=order, color='#183B56', size=3, alpha=.65)
plt.xticks(rotation=40, ha='right')
plt.ylim(0, 1.03)
plt.ylabel('Mask IoU with submitted branch (agreement, not accuracy)')
plt.xlabel('Analysis configuration')
plt.tight_layout()
plt.savefig(OUTPUT_DIR / 'mask_agreement.png', dpi=200, bbox_inches='tight')
plt.show()
"""))
cells.append(nbf.v4.new_markdown_cell("""## Derived measurements are configuration-dependent

Lines connect measurements from the same panel. They show analytical sensitivity; they must not be interpreted as biological trajectories.
"""))
cells.append(nbf.v4.new_code_cell("""metrics = [
    ('n_objects', 'Segmented regions (count)'),
    ('positive_area_fraction', 'Foreground area fraction'),
    ('max_object_area', 'Largest segmented region (pixels)'),
]
fig, axes = plt.subplots(1, 3, figsize=(15, 4.8))
for ax, (metric, ylabel) in zip(axes, metrics):
    for image_id, subset in results.groupby('image_id'):
        subset = subset.set_index('name').reindex(order)
        ax.plot(order, subset[metric], marker='o', linewidth=.8, alpha=.55)
    ax.set_ylabel(ylabel)
    ax.set_xlabel('Configuration')
    ax.tick_params(axis='x', rotation=70)
fig.suptitle('Each line is one synthetic measurement case', y=1.02)
fig.tight_layout()
fig.savefig(OUTPUT_DIR / 'metric_sensitivity.png', dpi=200, bbox_inches='tight')
plt.show()
"""))
cells.append(nbf.v4.new_markdown_cell("""## Visual QC for one illustrative panel

Change `example_id` to inspect another panel. Differences between masks reveal method dependence, not which method is biologically correct.
"""))
cells.append(nbf.v4.new_code_cell("""example_id = metadata.iloc[0]['image_id']
green = channels[example_id]
fig, axes = plt.subplots(3, 3, figsize=(11, 11))
for ax, config in zip(axes.flat, configs):
    _, mask, labels, _ = segment_with_config(green, config)
    ax.imshow(green, cmap='gray')
    ax.contour(mask, levels=[.5], colors='magenta', linewidths=.5)
    ax.set_title(f'{config.name}\\nregions={labels.max()}, area={mask.mean():.3f}', fontsize=9)
    ax.axis('off')
fig.suptitle(f'Illustrative panel {example_id}: overlay comparison', y=.92)
fig.tight_layout()
fig.savefig(OUTPUT_DIR / f'{example_id}_configuration_overlays.png', dpi=200, bbox_inches='tight')
plt.show()
"""))
cells.append(nbf.v4.new_markdown_cell("""## Observation-to-measurement prompts

- Write one qualitative observation about a panel without proposing a cause.
- Which construct could represent that observation: coverage, intensity, size, shape, or spatial dispersion?
- Give one operational definition and one alternative definition for that construct.
- Which measurements are most stable across configurations?
- Which panels are most sensitive to threshold choice or object splitting?
- Why does agreement with the submitted branch not establish accuracy?
- Draw the intended hierarchy: experiment → sample/well → field → segmented object.
- Which metadata and controls would make the measurement interpretable?
- What would have to be validated before the construct could be used in a group comparison?

## Stop rule

Do not calculate group p-values or train a classifier from these panels. The endpoint is a defensible measurement specification and a design for collecting analysis-ready experimental data.
"""))

nb["cells"] = cells
OUT.parent.mkdir(parents=True, exist_ok=True)
nbf.write(nb, OUT)
print(OUT)
