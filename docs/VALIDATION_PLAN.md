# Validation Plan

## Current validation

The repository validates:

- homography shape, finiteness, and determinant checks
- image artifact probing
- input-target ID pairing
- normalized MAE
- expected calibration error
- confidence-abstention curves
- synthetic encoder demo execution

## Next validation gates

1. Stage Diffuser lensless inputs and pair them with GT2DC targets.
2. Add leakage-controlled train, validation, and test splits.
3. Train baseline reconstruction and feature-prediction models.
4. Add OOD, mismatch, corruption, and calibration experiments.
5. Report confidence-risk curves and abstention behavior.
6. Add result plots for reconstruction quality, confidence, and error distribution.
7. Add a compact release gate that records pass/fail status for each validation run.

## Acceptance logic

A validation run should report input-target pairing status, calibration-artifact status, model error, confidence behavior, and known failure modes. Outputs should be structured enough for repeated comparison across datasets and model variants.
