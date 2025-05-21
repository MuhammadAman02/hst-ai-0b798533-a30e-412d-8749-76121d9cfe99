from nicegui import ui
import pandas as pd

class UploadPage:
    def __init__(self, data_processor):
        self.data_processor = data_processor

        @ui.page('/upload')
        def upload():
            ui.label('Upload Transaction Data').classes('text-h4 text-weight-bold')

            file = ui.upload(label='Upload CSV file', auto_upload=True).classes('max-w-full')

            async def process_upload(file):
                if file:
                    content = await file.read()
                    df = pd.read_csv(pd.compat.StringIO(content.decode('utf-8')))
                    X, y = self.data_processor.process_data(df)
                    ui.notify(f'Data processed successfully. Shape: {X.shape}')
                    ui.open('/results')

            ui.button('Process Data', on_click=lambda: process_upload(file.value)).classes('text-white bg-primary')