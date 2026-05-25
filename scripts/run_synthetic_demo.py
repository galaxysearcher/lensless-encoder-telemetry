from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

from optical_telemetry_assurance.evidence import write_json_report, write_markdown_report
from optical_telemetry_assurance.metrics import abstention_curve, normalized_mae


def make_synthetic_encoder_data(n: int = 512, seed: int = 7):
    """Create a simple latent-state to encoded-feature regression problem."""
    rng = np.random.default_rng(seed)
    state = rng.normal(size=(n, 3))
    encoder = rng.normal(size=(3, 24))
    features = np.tanh(state @ encoder + 0.05 * rng.normal(size=(n, 24)))
    target = 0.7 * state[:, 0] - 0.25 * state[:, 1] + 0.1 * state[:, 2]
    target += 0.03 * rng.normal(size=n)
    return features, target


def main():
    parser = argparse.ArgumentParser(description="Run a lightweight synthetic optical encoder demo.")
    parser.add_argument("--out", default="artifacts/synthetic_demo")
    args = parser.parse_args()

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    x, y = make_synthetic_encoder_data()
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=42)

    model = Ridge(alpha=1.0)
    model.fit(x_train, y_train)
    pred = model.predict(x_test)

    residual = np.abs(y_test - pred)
    confidence = 1.0 / (1.0 + residual / (np.std(y_train) + 1e-12))

    summary = {
        "title": "Synthetic Physical Encoder Demo",
        "status": "PASS_SYNTHETIC_DEMO",
        "headline": {
            "n_samples": int(len(y)),
            "n_features": int(x.shape[1]),
            "r2": round(float(r2_score(y_test, pred)), 4),
            "mae": round(float(mean_absolute_error(y_test, pred)), 4),
            "normalized_mae": round(float(normalized_mae(y_test, pred)), 4),
        },
        "abstention_curve": abstention_curve(confidence, residual),
        "scope_notes": [
            "Synthetic data exercises the software path.",
            "Physical encoder validation requires optical measurements and experimental controls.",
        ],
    }

    write_json_report(summary, out / "synthetic_demo_summary.json")
    write_markdown_report(summary, out / "synthetic_demo_summary.md")
    print(summary)


if __name__ == "__main__":
    main()
