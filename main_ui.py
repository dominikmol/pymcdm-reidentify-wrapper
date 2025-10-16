# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGraphicsView, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableView, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1037, 818)
        MainWindow.setMinimumSize(QSize(900, 650))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget {\n"
"    background-color: #f5f7f9;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.nav = QWidget(self.centralwidget)
        self.nav.setObjectName(u"nav")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nav.sizePolicy().hasHeightForWidth())
        self.nav.setSizePolicy(sizePolicy)
        self.nav.setMinimumSize(QSize(250, 0))
        self.nav.setMaximumSize(QSize(250, 16777215))
        self.nav.setStyleSheet(u"QWidget#nav {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #0078D7, stop:1 #005A9E\n"
"    );\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0.1);\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 10px;\n"
"    text-align: left;\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.25);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 255, 255, 0.15);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.nav)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_app_title = QLabel(self.nav)
        self.lbl_app_title.setObjectName(u"lbl_app_title")
        self.lbl_app_title.setStyleSheet(u"QLabel#lbl_app_title {\n"
"    color: white;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    text-align: center;\n"
"    padding: 10px;\n"
"}")

        self.verticalLayout.addWidget(self.lbl_app_title)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.btn_data_page = QPushButton(self.nav)
        self.btn_data_page.setObjectName(u"btn_data_page")
        self.btn_data_page.setMinimumSize(QSize(220, 40))
        self.btn_data_page.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout.addWidget(self.btn_data_page)

        self.btn_stfn_page = QPushButton(self.nav)
        self.btn_stfn_page.setObjectName(u"btn_stfn_page")
        self.btn_stfn_page.setMinimumSize(QSize(220, 40))
        self.btn_stfn_page.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout.addWidget(self.btn_stfn_page)

        self.btn_mcda_page = QPushButton(self.nav)
        self.btn_mcda_page.setObjectName(u"btn_mcda_page")
        self.btn_mcda_page.setMinimumSize(QSize(220, 40))
        self.btn_mcda_page.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout.addWidget(self.btn_mcda_page)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.nav)

        self.pages = QStackedWidget(self.centralwidget)
        self.pages.setObjectName(u"pages")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pages.sizePolicy().hasHeightForWidth())
        self.pages.setSizePolicy(sizePolicy1)
        self.pages.setStyleSheet(u"")
        self.data_page = QWidget()
        self.data_page.setObjectName(u"data_page")
        self.verticalLayout_2 = QVBoxLayout(self.data_page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.data_input_container = QWidget(self.data_page)
        self.data_input_container.setObjectName(u"data_input_container")
        self.lbl_data_management = QLabel(self.data_input_container)
        self.lbl_data_management.setObjectName(u"lbl_data_management")
        self.lbl_data_management.setGeometry(QRect(60, 30, 191, 31))
        self.txt_data_input = QTextEdit(self.data_input_container)
        self.txt_data_input.setObjectName(u"txt_data_input")
        self.txt_data_input.setGeometry(QRect(20, 90, 551, 71))
        self.btn_load_data = QPushButton(self.data_input_container)
        self.btn_load_data.setObjectName(u"btn_load_data")
        self.btn_load_data.setGeometry(QRect(580, 90, 171, 71))

        self.verticalLayout_2.addWidget(self.data_input_container)

        self.data_table_container = QWidget(self.data_page)
        self.data_table_container.setObjectName(u"data_table_container")
        self.lbl_data_view = QLabel(self.data_table_container)
        self.lbl_data_view.setObjectName(u"lbl_data_view")
        self.lbl_data_view.setGeometry(QRect(40, 20, 47, 13))
        self.tbl_data_view = QTableView(self.data_table_container)
        self.tbl_data_view.setObjectName(u"tbl_data_view")
        self.tbl_data_view.setGeometry(QRect(10, 50, 751, 341))

        self.verticalLayout_2.addWidget(self.data_table_container)

        self.pages.addWidget(self.data_page)
        self.stfn_page = QWidget()
        self.stfn_page.setObjectName(u"stfn_page")
        self.verticalLayout_3 = QVBoxLayout(self.stfn_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.stfn_title_container = QWidget(self.stfn_page)
        self.stfn_title_container.setObjectName(u"stfn_title_container")
        self.lbl_stfn_analysis = QLabel(self.stfn_title_container)
        self.lbl_stfn_analysis.setObjectName(u"lbl_stfn_analysis")
        self.lbl_stfn_analysis.setGeometry(QRect(40, 30, 241, 51))

        self.verticalLayout_3.addWidget(self.stfn_title_container)

        self.stfn_main_container = QWidget(self.stfn_page)
        self.stfn_main_container.setObjectName(u"stfn_main_container")
        self.stfn_parameters_container = QWidget(self.stfn_main_container)
        self.stfn_parameters_container.setObjectName(u"stfn_parameters_container")
        self.stfn_parameters_container.setGeometry(QRect(10, 10, 251, 381))
        self.lbl_parameters = QLabel(self.stfn_parameters_container)
        self.lbl_parameters.setObjectName(u"lbl_parameters")
        self.lbl_parameters.setGeometry(QRect(10, 10, 71, 16))
        self.plainTextEdit = QPlainTextEdit(self.stfn_parameters_container)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(10, 70, 231, 71))
        self.lbl_bounds = QLabel(self.stfn_parameters_container)
        self.lbl_bounds.setObjectName(u"lbl_bounds")
        self.lbl_bounds.setGeometry(QRect(10, 50, 131, 16))
        self.btn_generate_bounds = QPushButton(self.stfn_parameters_container)
        self.btn_generate_bounds.setObjectName(u"btn_generate_bounds")
        self.btn_generate_bounds.setGeometry(QRect(10, 150, 231, 23))
        self.lbl_alternatives_ranking = QLabel(self.stfn_parameters_container)
        self.lbl_alternatives_ranking.setObjectName(u"lbl_alternatives_ranking")
        self.lbl_alternatives_ranking.setGeometry(QRect(10, 180, 161, 16))
        self.lbl_population_size = QLabel(self.stfn_parameters_container)
        self.lbl_population_size.setObjectName(u"lbl_population_size")
        self.lbl_population_size.setGeometry(QRect(10, 280, 161, 16))
        self.lbl_criteria_weights = QLabel(self.stfn_parameters_container)
        self.lbl_criteria_weights.setObjectName(u"lbl_criteria_weights")
        self.lbl_criteria_weights.setGeometry(QRect(10, 230, 161, 16))
        self.txt_alternatives_ranking = QTextEdit(self.stfn_parameters_container)
        self.txt_alternatives_ranking.setObjectName(u"txt_alternatives_ranking")
        self.txt_alternatives_ranking.setGeometry(QRect(10, 200, 221, 21))
        self.txt_criteria_weights = QTextEdit(self.stfn_parameters_container)
        self.txt_criteria_weights.setObjectName(u"txt_criteria_weights")
        self.txt_criteria_weights.setGeometry(QRect(10, 250, 221, 21))
        self.txt_population_size = QTextEdit(self.stfn_parameters_container)
        self.txt_population_size.setObjectName(u"txt_population_size")
        self.txt_population_size.setGeometry(QRect(10, 300, 221, 21))
        self.btn_calculate_stfn = QPushButton(self.stfn_parameters_container)
        self.btn_calculate_stfn.setObjectName(u"btn_calculate_stfn")
        self.btn_calculate_stfn.setGeometry(QRect(10, 350, 231, 23))
        self.stfn_results_container = QWidget(self.stfn_main_container)
        self.stfn_results_container.setObjectName(u"stfn_results_container")
        self.stfn_results_container.setGeometry(QRect(270, 10, 491, 80))
        self.lbl_stfn_results = QLabel(self.stfn_results_container)
        self.lbl_stfn_results.setObjectName(u"lbl_stfn_results")
        self.lbl_stfn_results.setGeometry(QRect(20, 10, 71, 16))
        self.txt_stfn_results = QTextEdit(self.stfn_results_container)
        self.txt_stfn_results.setObjectName(u"txt_stfn_results")
        self.txt_stfn_results.setGeometry(QRect(20, 30, 451, 41))
        self.stfn_visualization_container = QWidget(self.stfn_main_container)
        self.stfn_visualization_container.setObjectName(u"stfn_visualization_container")
        self.stfn_visualization_container.setGeometry(QRect(270, 100, 491, 291))
        self.gv_stfn_visualization = QGraphicsView(self.stfn_visualization_container)
        self.gv_stfn_visualization.setObjectName(u"gv_stfn_visualization")
        self.gv_stfn_visualization.setGeometry(QRect(0, 40, 491, 251))
        self.lbl_stfn_visualization = QLabel(self.stfn_visualization_container)
        self.lbl_stfn_visualization.setObjectName(u"lbl_stfn_visualization")
        self.lbl_stfn_visualization.setGeometry(QRect(20, 10, 71, 16))
        self.btn_previous_visualization = QPushButton(self.stfn_visualization_container)
        self.btn_previous_visualization.setObjectName(u"btn_previous_visualization")
        self.btn_previous_visualization.setGeometry(QRect(310, 10, 75, 23))
        self.btn_next_visualization = QPushButton(self.stfn_visualization_container)
        self.btn_next_visualization.setObjectName(u"btn_next_visualization")
        self.btn_next_visualization.setGeometry(QRect(400, 10, 75, 23))

        self.verticalLayout_3.addWidget(self.stfn_main_container)

        self.pages.addWidget(self.stfn_page)
        self.mcda_page = QWidget()
        self.mcda_page.setObjectName(u"mcda_page")
        self.verticalLayout_4 = QVBoxLayout(self.mcda_page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.mcda_title_container = QWidget(self.mcda_page)
        self.mcda_title_container.setObjectName(u"mcda_title_container")
        self.lbl_mcda_title = QLabel(self.mcda_title_container)
        self.lbl_mcda_title.setObjectName(u"lbl_mcda_title")
        self.lbl_mcda_title.setGeometry(QRect(30, 30, 141, 21))

        self.verticalLayout_4.addWidget(self.mcda_title_container)

        self.mcda_main_container = QWidget(self.mcda_page)
        self.mcda_main_container.setObjectName(u"mcda_main_container")
        self.mcda_config_container = QWidget(self.mcda_main_container)
        self.mcda_config_container.setObjectName(u"mcda_config_container")
        self.mcda_config_container.setGeometry(QRect(10, 10, 181, 381))
        self.lbl_mcda_config = QLabel(self.mcda_config_container)
        self.lbl_mcda_config.setObjectName(u"lbl_mcda_config")
        self.lbl_mcda_config.setGeometry(QRect(20, 10, 131, 31))
        self.lbl_mcda_methods = QLabel(self.mcda_config_container)
        self.lbl_mcda_methods.setObjectName(u"lbl_mcda_methods")
        self.lbl_mcda_methods.setGeometry(QRect(10, 35, 101, 31))
        self.cb_mcda_method = QComboBox(self.mcda_config_container)
        self.cb_mcda_method.setObjectName(u"cb_mcda_method")
        self.cb_mcda_method.setGeometry(QRect(10, 80, 161, 22))
        self.lbl_criteria_types = QLabel(self.mcda_config_container)
        self.lbl_criteria_types.setObjectName(u"lbl_criteria_types")
        self.lbl_criteria_types.setGeometry(QRect(10, 120, 151, 16))
        self.txt_criteria_types = QTextEdit(self.mcda_config_container)
        self.txt_criteria_types.setObjectName(u"txt_criteria_types")
        self.txt_criteria_types.setGeometry(QRect(10, 150, 161, 21))
        self.btn_calculate_ranking = QPushButton(self.mcda_config_container)
        self.btn_calculate_ranking.setObjectName(u"btn_calculate_ranking")
        self.btn_calculate_ranking.setGeometry(QRect(10, 350, 161, 23))
        self.mcda_new_ranking_container = QWidget(self.mcda_main_container)
        self.mcda_new_ranking_container.setObjectName(u"mcda_new_ranking_container")
        self.mcda_new_ranking_container.setGeometry(QRect(210, 10, 551, 51))
        self.lbl_new_ranking = QLabel(self.mcda_new_ranking_container)
        self.lbl_new_ranking.setObjectName(u"lbl_new_ranking")
        self.lbl_new_ranking.setGeometry(QRect(10, 0, 71, 16))
        self.txt_new_ranking = QTextEdit(self.mcda_new_ranking_container)
        self.txt_new_ranking.setObjectName(u"txt_new_ranking")
        self.txt_new_ranking.setGeometry(QRect(10, 25, 531, 21))
        self.mcda_old_ranking_container = QWidget(self.mcda_main_container)
        self.mcda_old_ranking_container.setObjectName(u"mcda_old_ranking_container")
        self.mcda_old_ranking_container.setGeometry(QRect(210, 80, 551, 51))
        self.lbl_old_ranking = QLabel(self.mcda_old_ranking_container)
        self.lbl_old_ranking.setObjectName(u"lbl_old_ranking")
        self.lbl_old_ranking.setGeometry(QRect(10, 0, 81, 16))
        self.txt_old_ranking = QTextEdit(self.mcda_old_ranking_container)
        self.txt_old_ranking.setObjectName(u"txt_old_ranking")
        self.txt_old_ranking.setGeometry(QRect(10, 20, 531, 21))
        self.mcda_visualization_container = QWidget(self.mcda_main_container)
        self.mcda_visualization_container.setObjectName(u"mcda_visualization_container")
        self.mcda_visualization_container.setGeometry(QRect(210, 140, 551, 251))
        self.btn_compare_ranks = QPushButton(self.mcda_visualization_container)
        self.btn_compare_ranks.setObjectName(u"btn_compare_ranks")
        self.btn_compare_ranks.setGeometry(QRect(320, 10, 101, 23))
        self.btn_rank_correlation = QPushButton(self.mcda_visualization_container)
        self.btn_rank_correlation.setObjectName(u"btn_rank_correlation")
        self.btn_rank_correlation.setGeometry(QRect(430, 10, 111, 23))
        self.lbl_mcda_visualization = QLabel(self.mcda_visualization_container)
        self.lbl_mcda_visualization.setObjectName(u"lbl_mcda_visualization")
        self.lbl_mcda_visualization.setGeometry(QRect(10, 10, 81, 16))
        self.gv_mcda_visualization = QGraphicsView(self.mcda_visualization_container)
        self.gv_mcda_visualization.setObjectName(u"gv_mcda_visualization")
        self.gv_mcda_visualization.setGeometry(QRect(10, 40, 531, 201))

        self.verticalLayout_4.addWidget(self.mcda_main_container)

        self.pages.addWidget(self.mcda_page)

        self.horizontalLayout.addWidget(self.pages)

        self.horizontalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pages.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_app_title.setText(QCoreApplication.translate("MainWindow", u"pymcdm-reidentify", None))
        self.btn_data_page.setText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.btn_stfn_page.setText(QCoreApplication.translate("MainWindow", u"stfn", None))
        self.btn_mcda_page.setText(QCoreApplication.translate("MainWindow", u"mcda", None))
        self.lbl_data_management.setText(QCoreApplication.translate("MainWindow", u"Data Management", None))
        self.btn_load_data.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.lbl_data_view.setText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.lbl_stfn_analysis.setText(QCoreApplication.translate("MainWindow", u"STFN Analysis\n"
"", None))
        self.lbl_parameters.setText(QCoreApplication.translate("MainWindow", u"Parameters", None))
        self.lbl_bounds.setText(QCoreApplication.translate("MainWindow", u"Bounds for Criteria", None))
        self.btn_generate_bounds.setText(QCoreApplication.translate("MainWindow", u"Generate Bounds", None))
        self.lbl_alternatives_ranking.setText(QCoreApplication.translate("MainWindow", u"Alternatives Ranking", None))
        self.lbl_population_size.setText(QCoreApplication.translate("MainWindow", u"Population Size", None))
        self.lbl_criteria_weights.setText(QCoreApplication.translate("MainWindow", u"Criteria Weights", None))
        self.btn_calculate_stfn.setText(QCoreApplication.translate("MainWindow", u"Calculate STFN", None))
        self.lbl_stfn_results.setText(QCoreApplication.translate("MainWindow", u"Results", None))
        self.lbl_stfn_visualization.setText(QCoreApplication.translate("MainWindow", u"Visualization", None))
        self.btn_previous_visualization.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.btn_next_visualization.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.lbl_mcda_title.setText(QCoreApplication.translate("MainWindow", u"MCDA Methods", None))
        self.lbl_mcda_config.setText(QCoreApplication.translate("MainWindow", u"Method Configuration\n"
"", None))
        self.lbl_mcda_methods.setText(QCoreApplication.translate("MainWindow", u"MCDA Method", None))
        self.lbl_criteria_types.setText(QCoreApplication.translate("MainWindow", u"Types of criteria", None))
        self.btn_calculate_ranking.setText(QCoreApplication.translate("MainWindow", u"Calculate Ranking", None))
        self.lbl_new_ranking.setText(QCoreApplication.translate("MainWindow", u"New Ranking", None))
        self.lbl_old_ranking.setText(QCoreApplication.translate("MainWindow", u"Old Ranking", None))
        self.btn_compare_ranks.setText(QCoreApplication.translate("MainWindow", u"Rank Comaprison", None))
        self.btn_rank_correlation.setText(QCoreApplication.translate("MainWindow", u"Rank Corelation", None))
        self.lbl_mcda_visualization.setText(QCoreApplication.translate("MainWindow", u"Visualization", None))
    # retranslateUi

