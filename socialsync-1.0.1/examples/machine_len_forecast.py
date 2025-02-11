from socialsync.analytics import TrendAnalyzer
from socialsync.machine_len_utils import MachineLearningUtils

historical_data = [
    {"day": 1, "popularity": 100},
    {"day": 2, "popularity": 120},
    {"day": 3, "popularity": 150},
    {"day": 4, "popularity": 180},
    {"day": 5, "popularity": 200}
]

analyzer = TrendAnalyzer(data_source=None)
model = analyzer.train_trend_forecast_model(historical_data)

future_days = [6, 7, 8]
predictions = analyzer.predict_future_trends(model, future_days)
print("Predicted trends:", predictions)