import pytest
from unittest.mock import MagicMock, patch
import numpy as np
import computation


@pytest.fixture
def mock_app():
    app = MagicMock()
    app.data_matrix = np.array([
        [10, 20, 21, 5],
        [15, 25, 30, 10],
        [5, 10, 15, 3]
    ])

    app.ui.txt_criteria_weights.toPlainText.return_value = "0.20, 0.30, 0.15, 0.35"
    app.ui.txt_bounds_data.toPlainText.return_value = "(5, 15), (10, 25), (15, 30), (3, 10)"

    app.ui.txt_epoch_size.toPlainText.return_value = "100"
    app.ui.txt_population_size.toPlainText.return_value = "25"
    app.ui.txt_c1_size.toPlainText.return_value = "2.05"
    app.ui.txt_c2_size.toPlainText.return_value = "2.05"
    app.ui.txt_w_size.toPlainText.return_value = "0.4"
    app.ui.txt_alternatives_ranking.toPlainText.return_value = "1, 2, 3"
    app.ui.cb_mcda_method.currentText.return_value = "TOPSIS"
    return app


def test_calculate_STFN_no_data(mock_app):
    mock_app.data_matrix = None
    
    with patch("ui_helpers.showErrorMessage") as mock_error, \
        patch("computation.set_stfn_to_background") as mock_background:

        computation.calculate_STFN(mock_app)
        mock_error.assert_called_once_with("Error", "Please import data first.")
        mock_background.assert_not_called()


def test_calculate_STFN_not_ready(mock_app):
    with patch("ui_helpers.showErrorMessage") as mock_error, \
        patch("validation.checkIfSTFNReady", return_value=False), \
        patch("computation.set_stfn_to_background") as mock_background:
        
        computation.calculate_STFN(mock_app)
        mock_error.assert_called_once_with(
            "Error", "Make sure data, bounds, weights, and expert rank are set."
        )
        mock_background.assert_not_called()


def test_calculate_STFN_pso_not_valid(mock_app):
    with patch("ui_helpers.showErrorMessage") as mock_error, \
        patch("validation.checkIfSTFNReady", return_value=True), \
        patch("validation.checkIfPSOReady", return_value=False), \
        patch("computation.set_stfn_to_background") as mock_background:
        
        computation.calculate_STFN(mock_app)
        mock_error.assert_called_once_with("Error", "Make sure PSO parameters are valid.")
        mock_background.assert_not_called()


def test_calculate_STFN_invalid_method(mock_app):
    mock_app.ui.cb_mcda_method.currentText.return_value = "WASPAS"
    
    with patch("ui_helpers.showErrorMessage") as mock_error, \
        patch("validation.checkIfSTFNReady", return_value=True), \
        patch("validation.checkIfPSOReady", return_value=True), \
        patch("ui_helpers.enable_all_buttons") as mock_enable, \
        patch("computation.set_stfn_to_background") as mock_background:
        
        computation.calculate_STFN(mock_app)
        
        mock_error.assert_called_once_with("Error", "Make sure valid MCDA method is selected.")
        mock_enable.assert_called_once()
        mock_background.assert_not_called()
        

def test_calculate_STFN_success(mock_app):
    with patch("ui_helpers.showErrorMessage") as mock_error, \
        patch("validation.checkIfSTFNReady", return_value=True), \
        patch("validation.checkIfPSOReady", return_value=True), \
        patch("ui_helpers.disable_all_buttons"), \
        patch("ui_helpers.clear_or_set_scene"), \
        patch("computation.set_stfn_to_background") as mock_background:
        
        computation.calculate_STFN(mock_app)
        
        mock_error.assert_not_called()
        assert mock_app.weights is not None
        assert mock_app.weights.shape == (4,)
        assert mock_app.weights[0] == 0.20
        assert isinstance(mock_app.weights, np.ndarray)
        mock_background.assert_called_once()