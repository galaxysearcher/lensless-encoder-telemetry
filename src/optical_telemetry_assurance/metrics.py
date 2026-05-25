from __future__ import annotations

import numpy as np


def normalized_mae(y_true, y_pred, eps: float = 1e-12) -> float:
    """Mean absolute error normalized by the observed target range."""
    truth = np.asarray(y_true, dtype=float)
    pred = np.asarray(y_pred, dtype=float)
    scale = np.nanmax(truth) - np.nanmin(truth)
    return float(np.nanmean(np.abs(truth - pred)) / max(scale, eps))


def expected_calibration_error(confidence, correct, n_bins: int = 10) -> float:
    """Binary expected calibration error for confidence-gated experiments."""
    conf = np.asarray(confidence, dtype=float)
    corr = np.asarray(correct, dtype=float)
    if conf.shape != corr.shape:
        raise ValueError("confidence and correct arrays must have the same shape")

    edges = np.linspace(0.0, 1.0, n_bins + 1)
    ece = 0.0
    for low, high in zip(edges[:-1], edges[1:]):
        if high < 1.0:
            mask = (conf >= low) & (conf < high)
        else:
            mask = (conf >= low) & (conf <= high)
        if not np.any(mask):
            continue
        bin_conf = float(np.mean(conf[mask]))
        bin_acc = float(np.mean(corr[mask]))
        ece += float(np.mean(mask) * abs(bin_acc - bin_conf))
    return ece


def abstention_curve(confidence, loss, thresholds=None) -> list[dict]:
    """Compute coverage and retained loss across confidence thresholds."""
    conf = np.asarray(confidence, dtype=float)
    losses = np.asarray(loss, dtype=float)
    if thresholds is None:
        thresholds = np.linspace(0.0, 1.0, 11)

    rows = []
    for threshold in thresholds:
        keep = conf >= threshold
        rows.append({
            "threshold": float(threshold),
            "coverage": float(np.mean(keep)),
            "mean_loss_when_kept": float(np.mean(losses[keep])) if np.any(keep) else None,
        })
    return rows
