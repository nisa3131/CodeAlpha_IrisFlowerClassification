"""Tests for duplicate leakage and ambiguous labels, not numerical score snapshots."""

from pathlib import Path
import tempfile
import unittest

import pandas as pd
from sklearn.model_selection import StratifiedGroupKFold

import analysis


class EvaluationContractTests(unittest.TestCase):
    def test_identical_measurements_never_cross_held_out_or_cv_boundaries(self):
        data, groups, _ = analysis.load_and_audit(analysis.ROOT / "data" / "Iris.csv")
        train, test = analysis.split_indices(data, groups)
        self.assertEqual(len(set(train) | set(test)), len(data))
        self.assertFalse(set(train) & set(test))
        self.assertFalse(set(groups[train]) & set(groups[test]))
        # Compare feature tuples too, independently of the generated group labels.
        feature_sets = lambda rows: set(data.iloc[rows][analysis.FEATURES].itertuples(index=False, name=None))
        self.assertFalse(feature_sets(train) & feature_sets(test))
        train_data = data.iloc[train]
        cv = StratifiedGroupKFold(n_splits=5, shuffle=True, random_state=analysis.SEED)
        validation_positions = []
        for fit, validate in cv.split(train_data[analysis.FEATURES], train_data[analysis.TARGET], groups[train]):
            self.assertFalse(feature_sets(train[fit]) & feature_sets(train[validate]))
            self.assertEqual(set(train_data.iloc[fit][analysis.TARGET]), set(analysis.CLASSES))
            self.assertEqual(set(train_data.iloc[validate][analysis.TARGET]), set(analysis.CLASSES))
            validation_positions.extend(validate)
        self.assertEqual(sorted(validation_positions), list(range(len(train))))

    def test_conflicting_species_for_identical_measurements_are_rejected(self):
        data = pd.read_csv(analysis.ROOT / "data" / "Iris.csv")
        extra = data.iloc[[0]].copy()
        extra[analysis.TARGET] = "Iris-virginica"
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "conflicting.csv"
            pd.concat([data, extra], ignore_index=True).to_csv(path, index=False)
            with self.assertRaisesRegex(ValueError, "conflicting species"):
                analysis.load_and_audit(path)


if __name__ == "__main__":
    unittest.main()
