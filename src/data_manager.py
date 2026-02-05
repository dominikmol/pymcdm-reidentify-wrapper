import os
import pandas as pd
from helpers import createDataTable, showErrorMessage


def clearStates(app):
    app.stfn = None
    app.data = None
    app.data_matrix = None
    app.bounds = None
    app.weights = None
    app.types = None
    app.stfn_plot_data = []
    app.stfn_plot_index = 0
    app.expert_rank = None
    app.mcda_method = None
    app.new_rank = None


def load_data(app, file_loc):
    _, extension = os.path.splitext(file_loc)
    extension = extension.lower()

    try:
        if extension == '.csv' or extension == '.txt':
            data = pd.read_csv(file_loc)
        elif extension == '.xlsx' or extension == '.xls':
            data = pd.read_excel(file_loc)
        else:
            raise ValueError("Unsupported file format")

        if data.size == 0:
            raise ValueError("The selected file is empty")
        
        clearStates(app)

        app.data = data
        app.data_matrix = data.iloc[:, 1:].to_numpy()
        createDataTable(app, data)

    except Exception as e:
        showErrorMessage(
            "Error",
            f'Failed to load data: {str(e)}'
            )
        return