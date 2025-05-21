import os
from dotenv import load_dotenv
from nicegui import ui, app
from app.fraud_detection.model import FraudDetectionModel
from app.fraud_detection.data_processor import DataProcessor
from app.ui.pages.home import HomePage
from app.ui.pages.upload import UploadPage
from app.ui.pages.results import ResultsPage

# Load environment variables
load_dotenv()

# Initialize fraud detection model and data processor
model = FraudDetectionModel()
data_processor = DataProcessor()

# Create pages
HomePage()
UploadPage(data_processor)
ResultsPage(model, data_processor)

# Run the app
if __name__ in {"__main__", "__mp_main__"}:
    ui.run(
        title="Irish Credit Union Fraud Detection",
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8000)),
    )