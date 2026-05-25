import numpy as np

from optical_telemetry_assurance.metrics import expected_calibration_error
from optical_telemetry_assurance.validators import paired_ids, validate_homography


def test_validate_homography_passes_for_identity():
    result = validate_homography(np.eye(3))
    assert result["status"] == "PASS"
    assert result["is_3x3"] is True


def test_paired_ids_detects_mismatch():
    result = paired_ids([1, 2, 3], [2, 3, 4])
    assert result["status"] == "CHECK"
    assert result["shared_count"] == 2


def test_ece_is_nonnegative():
    ece = expected_calibration_error([0.2, 0.8, 0.9], [0, 1, 1], n_bins=3)
    assert ece >= 0.0
