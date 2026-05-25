# Dataset Readiness

## Waller lensless imaging path

Role: primary real-optical benchmark for lensless measurement-to-target validation.

Local readiness summary:

- 25,000 GT2DC registered target images identified.
- 25,000 GT2RML registered target images identified.
- 25,000 shared image IDs matched between GT2DC and GT2RML.
- 199 PSF TIFF files present in the local dataset stack.
- 8 homography matrices converted to finite 3x3 NumPy matrices.

Interpretation: the registered target stack, PSF inventory, and homography support files are ready for paired optical experiments.

Next benchmark step:

1. Ingest Diffuser lensless input images.
2. Pair Diffuser inputs to GT2DC registered targets by image ID.
3. Run leakage-controlled train/test splits.
4. Report reconstruction or feature-prediction baselines.
5. Add corruption, mismatch, OOD, and confidence-calibration tests.

## IDToolkit nanophotonic proxy path

Role: CSV/table adapter benchmark and response-generalization stress case.

Local readiness summary:

- 3,882 CSV files identified across color filter, multilayer, and TPV folders.
- Schema probing confirmed a common parameter and response structure across sampled files.

Interpretation: IDToolkit is useful for ingestion, schema validation, adapter development, and response-generalization tests.
