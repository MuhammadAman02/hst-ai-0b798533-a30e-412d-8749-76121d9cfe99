from nicegui import ui
import pandas as pd
import plotly.express as px

class ResultsPage:
    def __init__(self, model, data_processor):
        self.model = model
        self.data_processor = data_processor

        @ui.page('/results')
        def results():
            ui.label('Fraud Detection Results').classes('text-h4 text-weight-bold')

            try:
                X, y = self.data_processor.get_processed_data()
            except ValueError:
                ui.label('No data has been processed yet. Please upload and process data first.')
                return

            if not self.model.is_trained:
                metrics = self.model.train(X, y)
                ui.label('Model trained successfully!').classes('text-h5')
                ui.label(f'Accuracy: {metrics["accuracy"]:.2f}')
                ui.label(f'Precision: {metrics["precision"]:.2f}')
                ui.label(f'Recall: {metrics["recall"]:.2f}')
                ui.label(f'F1 Score: {metrics["f1_score"]:.2f}')

            predictions = self.model.predict(X)
            probabilities = self.model.predict_proba(X)

            df_results = pd.DataFrame({
                'Actual': y,
                'Predicted': predictions,
                'Fraud Probability': probabilities[:, 1]
            })

            ui.label('Prediction Results').classes('text-h5')
            ui.table.from_pandas(df_results)

            # Feature importance plot
            feature_importance = self.model.get_feature_importance()
            fig = px.bar(x=X.columns, y=feature_importance, labels={'x': 'Features', 'y': 'Importance'})
            fig.update_layout(title='Feature Importance')
            ui.plotly(fig)

            # Fraud probability distribution
            fig_hist = px.histogram(df_results, x='Fraud Probability', nbins=50, title='Distribution of Fraud Probabilities')
            ui.plotly(fig_hist)