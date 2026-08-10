# Published-image case-study feasibility audit

This directory plans transfer exercises for the educational workflow. It does
not claim to reproduce, validate, or reinterpret the source publications.

The cases vary image dimensionality, channel structure, experimental hierarchy,
file format, and availability of reference masks. Source images are not
redistributed here. Learners should retrieve a small, cited subset from the
authoritative repository and comply with its license.

## Recommended teaching sequence

1. **BBBC039:** begin with 2D, single-channel, 16-bit fluorescence images and
   compare sensitivity configurations with reference masks.
2. **BBBC022:** examine how channel choice and plate/well/site hierarchy change
   the measurement design. Use only a small, documented subset.
3. **CELLULAR:** distinguish cell segmentation from downstream biological
   classification in a three-channel, time-resolved experiment.
4. **BBBC050:** make z-plane selection or projection an explicit analytical
   decision before attempting 3D measurement.
5. **BBBC038:** test whether a measurement rule transfers across heterogeneous
   nuclei images acquired from fluorescence and histology preparations. This is
   an extension about domain shift, not a claim that one configuration is
   universally valid.

## Boundaries

- Agreement with a supplied mask is not biological validation.
- Treatment labels do not justify treatment-effect inference from a few
  teaching images.
- Images, fields, wells, embryos, and experiments are different observational
  levels and must not be treated as interchangeable replicates.
- Threshold, background subtraction, projection, channel selection, and object
  splitting remain sensitivity choices rather than facts about the specimen.
- The current code directly supports only 2D single-channel PNG/TIFF inputs.
  It intentionally rejects multichannel arrays instead of silently collapsing
  them.

See `case_study_manifest.csv` for access, license, size, and adaptation details.

## First case: BBBC039

Retrieve the CC0 images, masks, and official train/validation/test metadata only
when needed:

```bash
python scripts/download_bbbc039.py
```

The ignored destination is `data/external/BBBC039/`. The loader preserves the
16-bit TIFF intensities, and `decode_color_instance_mask()` follows the dataset
author's published example by labelling connected foreground components. The
teaching notebook samples from the official splits and reports mask agreement
as agreement, not as proof of biological correctness.

Generate and run the case notebook with:

```bash
python scripts/create_bbbc039_case_study_notebook.py
jupyter nbconvert --to notebook --execute --inplace \
  notebooks/02_bbbc039_published_image_transfer.ipynb
```

## Second case: BBBC050

Retrieve and run the CC BY 3.0 three-dimensional case with:

```bash
python scripts/download_bbbc050.py
python scripts/create_bbbc050_case_study_notebook.py
jupyter nbconvert --to notebook --execute --inplace \
  notebooks/03_bbbc050_3d_projection_transfer.ipynb
```

The notebook compares central-plane, mean-projection, and maximum-projection
operationalizations. It uses three files from one training embryo as repeated
teaching observations, not as independent biological replicates.
