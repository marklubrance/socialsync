import unittest
import pandas as pd
from socialsync.machine_len_utils import MachineLearningUtils

class TestMachineLearningUtils(unittest.TestCase):
    def test_preprocess_data(self):
        data = [{"day": 1, "popularity": 100}, {"day": 2, "popularity": None}]
        df = MachineLearningUtils.preprocess_data(data)
        self.assertEqual(df.iloc[1]["popularity"], 0)

    def test_split_data(self):
        data = [{"day": 1, "popularity": 100}, {"day": 2, "popularity": 120}]
        df = pd.DataFrame(data)
        X_train, X_test, y_train, y_test = MachineLearningUtils.split_data(df, "popularity")
        self.assertEqual(len(X_train) + len(X_test), len(df))

if __name__ == "__main__":
    unittest.main()