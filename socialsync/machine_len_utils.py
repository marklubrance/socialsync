import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

class MachineLearningUtils:
    @staticmethod
    def preprocess_data(data: List[Dict[str, Any]]) -> pd.DataFrame:
        df = pd.DataFrame(data)
        df.fillna(0, inplace=True)
        return df

    @staticmethod
    def split_data(df: pd.DataFrame, target_column: str, test_size: float = 0.2):
        X = df.drop(columns=[target_column])
        y = df[target_column]
        return train_test_split(X, y, test_size=test_size, random_state=42)

    @staticmethod
    def evaluate_model(model, X_test, y_test):
        predictions = model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        return {"mean_squared_error": mse}