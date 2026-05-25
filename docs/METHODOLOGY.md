# Methodology

## Objective

Evaluate whether optical measurements can support confidence-scored telemetry inference.

The workflow treats each optical measurement as a signal candidate. A candidate becomes useful only when its input-target pairing, calibration artifacts, integrity checks, confidence behavior, and failure modes are visible.

## Pipeline

```text
dataset inventory -> calibration checks -> input-target pairing -> baseline inference -> confidence scoring -> abstention analysis
```

## Core checks

- Count and organize dataset artifacts.
- Validate image integrity and numeric arrays.
- Validate 3x3 homography matrices.
- Compare input and target identifiers.
- Compute confidence and abstention curves.
- Track normalized prediction error.
- Store small JSON and Markdown reports.

## Synthetic encoder demo

The synthetic demo maps a latent three-dimensional state into a 24-feature encoded measurement vector, trains a Ridge baseline, and reports error and abstention behavior. It is a fast path for verifying the software workflow before larger optical datasets are staged.

## Decision value

The project is useful when it can separate three states:

1. The signal is paired, calibrated, and informative.
2. The signal is present but confidence is low.
3. The signal is mismatched, corrupted, or outside the training distribution.
