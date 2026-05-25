# Lensless Encoder Telemetry

Validation-first optical ML utilities for turning lensless measurements and physical encoder patterns into confidence-scored telemetry candidates.

The project asks a practical question: when can a complex optical pattern be treated as a measured signal for downstream decision systems? The workflow focuses on dataset integrity, calibration artifacts, input-target pairing, confidence scoring, abstention behavior, and failure detection.

## Current focus

The benchmark path uses lensless imaging data and nanophotonic proxy tables to exercise the validation workflow. The longer research direction is physical optical encoders: structured phase masks, 3D scattering media, micro/nano void networks, and state-sensitive material surfaces that produce measurable optical signatures.

## What is included

```text
src/optical_telemetry_assurance/   Validation utilities
scripts/                           Dataset inventory and synthetic demo runners
tests/                             Lightweight unit tests
docs/                              Methodology, dataset readiness, and validation roadmap
examples/                          Small synthetic example configuration
artifacts/                         Validation summaries and demo outputs
data/                              Local manifest placeholder
```

## Validation status

| Benchmark path | Current status | Next step |
|---|---|---|
| Waller lensless imaging | Registered target images, PSFs, and homographies are organized for paired experiments. | Ingest Diffuser lensless inputs and pair them with registered GT2DC targets. |
| IDToolkit nanophotonic proxy data | CSV ingestion and schema checks are available for adapter testing. | Use as a response-generalization stress case and schema benchmark. |
| Synthetic physical encoder demo | Included as a lightweight runnable workflow. | Replace synthetic examples with benchmark experiments as local datasets are staged. |

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python scripts/run_synthetic_demo.py --out artifacts/synthetic_demo
pytest -q
```

## Example local inventory

```bash
python scripts/inventory_dataset_stack.py \
  --waller-root /path/to/waller_lensless \
  --idtoolkit-root /path/to/idtoolkit \
  --out artifacts/dataset_inventory.json
```

The inventory script records counts and artifact types while leaving dataset storage outside the repository.

## Research direction

The first publication path is a validation framework for lensless optical inference and physical encoder telemetry. The core contribution is a reproducible method for checking whether optical measurements are paired correctly, calibrated, robust to corruption, and suitable for confidence-scored inference.

A concise paper direction:

**Validation-First Lensless Optical Inference for Physical Encoder Telemetry**
