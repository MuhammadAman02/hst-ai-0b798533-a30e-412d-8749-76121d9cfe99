from nicegui import ui

class HomePage:
    def __init__(self):
        @ui.page('/')
        def home():
            ui.label('Irish Credit Union Fraud Detection').classes('text-h3 text-weight-bold')
            ui.label('Welcome to the Fraud Detection Solution for Irish Credit Unions').classes('text-h5')
            
            with ui.row():
                ui.button('Upload Data', on_click=lambda: ui.open('/upload')).classes('text-white bg-primary')
                ui.button('View Results', on_click=lambda: ui.open('/results')).classes('text-white bg-secondary')

            ui.label('This application helps detect potential fraud in credit union transactions.')
            ui.label('To get started, upload your transaction data on the Upload page.')