from sklearn.linear_model import LinearRegression
import numpy as np
from typing import List, Dict, Any

class TrendAnalyzer:
    def __init__(self, data_source):
        self.data_source = data_source

    def analyze_trends(self) -> List[Dict[str, Any]]:
        trends = self.data_source.fetch_trends()
        return sorted(trends, key=lambda x: x.get("popularity", 0), reverse=True)

    def generate_report(self, trends: List[Dict[str, Any]]) -> str:
        report = "Top Trends:\n"
        for trend in trends[:5]:
            name = trend.get("name", "Unknown")
            popularity = trend.get("popularity", 0)
            report += f"- {name} (Popularity: {popularity})\n"
        return report

    def recommend_content(self, trends: List[Dict[str, Any]]) -> List[str]:
        recommendations = []
        for trend in trends[:3]:
            name = trend.get("name", "Unknown")
            recommendations.append(f"Create content related to '{name}'")
        return recommendations

    def forecast_trends(self, trends: List[Dict[str, Any]], days: int = 7) -> List[Dict[str, Any]]:
        forecasted_trends = []
        for trend in trends:
            popularity = trend.get("popularity", 0)
            forecasted_popularity = popularity * (1 + 0.1 * days)  # Simple growth model
            forecasted_trends.append({**trend, "forecasted_popularity": forecasted_popularity})
        return forecasted_trends

    def train_trend_forecast_model(self, historical_data: List[Dict[str, Any]]) -> LinearRegression:
        X = np.array([data["day"] for data in historical_data]).reshape(-1, 1)
        y = np.array([data["popularity"] for data in historical_data])
        model = LinearRegression()
        model.fit(X, y)
        return model

    def predict_future_trends(self, model: LinearRegression, future_days: List[int]) -> List[float]:
        X_future = np.array(future_days).reshape(-1, 1)
        predictions = model.predict(X_future)
        return predictions.tolist()