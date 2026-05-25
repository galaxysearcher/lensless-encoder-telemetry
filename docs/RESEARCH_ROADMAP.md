# Research Roadmap

## Phase 1: Optical dataset validation

Establish a reproducible pipeline for dataset inventory, input-target pairing, image integrity checks, PSF and homography handling, and baseline optical inference.

Near-term tasks:

1. Complete Diffuser input ingestion.
2. Pair Diffuser measurements with GT2DC registered targets.
3. Train baseline reconstruction or feature-prediction models.
4. Add corruption, mismatch, and OOD tests.
5. Report confidence-risk and abstention curves.

## Phase 2: Synthetic physical encoder simulation

Simulate physical encoders that transform latent material state into optical patterns.

Candidate simulations:

- random scattering encoders
- structured phase masks
- low-resolution diffractive encoders
- state-dependent intensity or speckle patterns

## Phase 3: Macro or micro optical encoder surrogate

Build a low-cost physical surrogate before moving to smaller structures.

Candidate demonstrators:

- printed transparency phase or amplitude masks
- diffuser-based optical encoders
- 3D printed scattering coupons
- microstructured polymer films

## Phase 4: Shrink-fabricated coupon

Evaluate whether shrink-fabricated structures can create reproducible optical signatures suitable for ML inference.

Candidate artifacts:

- 3D scattering structures
- structured phase masks
- porous optical diffusers
- micro/nano void networks

## Phase 5: State-sensitive material encoder

Embed optical encoder behavior in a material system whose optical response changes with environment or state.

Candidate responses:

- humidity
- temperature
- swelling
- solvent exposure
- ion concentration
- mechanical strain
- aging or degradation

## Publication path

The first paper path is a framework and validation paper using lensless data. A later paper can focus on fabricated physical encoders after a physical coupon produces repeatable optical data.
