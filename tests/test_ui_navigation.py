import pytest
from PySide6.QtCore import Qt
from unittest.mock import patch
import numpy as np
from main import MainWindow

@pytest.fixture
def app(qtbot):
    test_window = MainWindow()
    qtbot.addWidget(test_window)

    test_window.ui.txt_c1_size.setPlainText("2.05")
    test_window.ui.txt_c2_size.setPlainText("2.05")
    test_window.ui.txt_w_size.setPlainText("0.4")
    test_window.ui.txt_population_size.setPlainText("50")
    test_window.ui.txt_epoch_size.setPlainText("250")
    return test_window

def test_stfn_calculation_flow_no_data(app, qtbot):
    qtbot.mouseClick(app.ui.btn_stfn_page, Qt.LeftButton)
    
    with patch("ui_helpers.showErrorMessage") as mock_error:
        qtbot.mouseClick(app.ui.btn_calculate_stfn, Qt.LeftButton)
        mock_error.assert_called_once_with("Error", "Please import data first.")

def test_stfn_calculation_missing_weights(app, qtbot):
    app.data_matrix = np.array([[10, 20]])
    
    with patch("ui_helpers.showErrorMessage") as mock_error:
        qtbot.mouseClick(app.ui.btn_calculate_stfn, Qt.LeftButton)
        mock_error.assert_called_once_with("Error", "Please enter criteria weights.")


def test_stfn_calculation_missing_expert_rank(app, qtbot):
    app.data_matrix = np.array([[10, 20]])
    app.ui.txt_criteria_weights.setPlainText("0.5, 0.5")
    
    with patch("ui_helpers.showErrorMessage") as mock_error:
        qtbot.mouseClick(app.ui.btn_calculate_stfn, Qt.LeftButton)
        mock_error.assert_called_once_with("Error", "Please enter expert ranking.")


def test_navigation_clear_stfn_results(app, qtbot):    
    app.ui.txt_criteria_weights.setPlainText("0.5, 0.5, ")
    app.ui.txt_alternatives_ranking.setPlainText("1, 2, ")
    app.data_matrix = np.array([[10, 20], [15, 25]]) 
    
    with patch("ui_helpers.showErrorMessage"), \
        patch("validation.checkIfSTFNReady", return_value=False), \
        patch("computation.set_stfn_to_background") as mock_background:
        
        qtbot.mouseClick(app.ui.btn_calculate_stfn, Qt.LeftButton)
        
        assert app.ui.txt_stfn_results.toPlainText() == ""
        assert np.array_equal(app.expert_rank, np.array([1, 2]))
        assert np.array_equal(app.weights, np.array([0.5, 0.5]))
        mock_background.assert_not_called()


def test_make_bounds_handle(app, qtbot):
    app.data_matrix = np.array([[10, 100], [20, 200]])
    qtbot.mouseClick(app.ui.btn_generate_bounds, Qt.LeftButton)
    
    expected_text = "(10, 20), (100, 200)"
    assert app.ui.txt_bounds_data.toPlainText() == expected_text


def test_page_switching(app, qtbot):
    qtbot.mouseClick(app.ui.btn_mcda_page, Qt.LeftButton)
    assert app.ui.pages.currentWidget() == app.ui.mcda_page
    
    qtbot.mouseClick(app.ui.btn_reversal_page, Qt.LeftButton)
    assert app.ui.pages.currentWidget() == app.ui.reversal_page