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
from PySide6.QtWidgets import (QApplication, QComboBox, QGraphicsView, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTableWidget, QTableWidgetItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 850)
        MainWindow.setMinimumSize(QSize(1200, 850))
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"	background-color: #EEEEEE;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
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
"    /* Ulepszenie: \u015arednio ciemny, profesjonalny b\u0142\u0119kit - idealna r\u00f3wnowaga */\n"
"    background-color: #4A89C9; \n"
"    /* Subtelna linia dla wydzielenia Navbara */\n"
"    border-right: 1px solid #3c72b0;\n"
"}\n"
"\n"
"/* Tytu\u0142 aplikacji */\n"
"QLabel#lbl_app_title {\n"
"    /* Bia\u0142y tekst dla maksymalnej czytelno\u015bci */\n"
"    color: #FFFFFF; \n"
"    font-size: 17px;\n"
"    font-weight: 700;\n"
"    padding: 16px 10px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"/* Przyciski w nawigacji */\n"
"QPushButton {\n"
"    /* Ulepszenie: Stonowany b\u0142\u0119kit (#75aadb) jako przycisk normalny */\n"
"    background-color: #75aadb;\n"
"    /* Bia\u0142y tekst na niebieskim przycisku */\n"
"    color: #FFFFFF;\n"
"    border: 2px solid #3c72b0;\n"
"    border-radius: 6px;\n"
"	margin-bottom: 6px;\n"
"    /*padding: 10px 12px;\n"
"    margin: 6px 12px;*/\n"
"    text-align: center; \n"
"    font-size: 13px;\n"
"    font-weight: 500;\n"
"    min-height: 40px;\n"
""
                        "    min-width: 200px;\n"
"}\n"
"\n"
"/* Hover - subtelne przyciemnienie */\n"
"QPushButton:hover {\n"
"    /* Lekkie przyciemnienie przycisku */\n"
"    background-color: #619bd1;\n"
"    border: none;\n"
"}\n"
"\n"
"/* Klikni\u0119ty / aktywny */\n"
"QPushButton:pressed {\n"
"    /* Efekt wci\u015bni\u0119cia */\n"
"    background-color: #538cc4;\n"
"    border: none;\n"
"}\n"
"\n"
"/* Zaznaczony przycisk (np. aktualna strona) */\n"
"QPushButton:checked {\n"
"    /* Ulepszenie: Czysty, wyrazisty b\u0142\u0119kit (#5B9ADF) dla aktywnej strony */\n"
"    background-color: #5B9ADF; \n"
"    /* Dajemy ciemniejsz\u0105 ramk\u0119 dla odr\u00f3\u017cnienia */\n"
"    border: 1px solid #3c72b0; \n"
"    color: #FFFFFF;\n"
"    font-weight: 700;\n"
"}\n"
"\n"
"/* Dodatkowe wyr\u00f3wnanie i przestrze\u0144 */\n"
"QVBoxLayout, QHBoxLayout {\n"
"    spacing: 8px;\n"
"    margin: 0;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.nav)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_app_title = QLabel(self.nav)
        self.lbl_app_title.setObjectName(u"lbl_app_title")
        self.lbl_app_title.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.lbl_app_title)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.btn_data_page = QPushButton(self.nav)
        self.btn_data_page.setObjectName(u"btn_data_page")
        self.btn_data_page.setMinimumSize(QSize(204, 50))
        self.btn_data_page.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout.addWidget(self.btn_data_page)

        self.btn_stfn_page = QPushButton(self.nav)
        self.btn_stfn_page.setObjectName(u"btn_stfn_page")
        self.btn_stfn_page.setMinimumSize(QSize(204, 50))
        self.btn_stfn_page.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout.addWidget(self.btn_stfn_page)

        self.btn_mcda_page = QPushButton(self.nav)
        self.btn_mcda_page.setObjectName(u"btn_mcda_page")
        self.btn_mcda_page.setMinimumSize(QSize(204, 50))
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
        self.data_page.setStyleSheet(u"/* --- OG\u00d3LNE STYLI DLA T\u0141A --- */\n"
"\n"
"/* T\u0142o centralnej sekcji powinno by\u0107 jasne i neutralne */\n"
"QWidget#centralwidget {\n"
"    background-color: #F8F9FA; /* Bardzo jasny szary/bia\u0142y */\n"
"}\n"
"\n"
"/* --- NAG\u0141\u00d3WKI I TEKST --- */\n"
"\n"
"/* Og\u00f3lny styl dla etykiet (Label) */\n"
"QLabel {\n"
"    color: #1b2735; /* Ciemny, czytelny tekst */\n"
"}\n"
"\n"
"/* Styl dla g\u0142\u00f3wnego nag\u0142\u00f3wka strony (np. lbl_data_management) */\n"
"QLabel#lbl_data_management {\n"
"    /*color: #1b2735;*/\n"
"    font-size: 24px; \n"
"    font-weight: bold;\n"
"    padding: 10px 0;\n"
"}\n"
"\n"
"/* --- KONTENERY GRUPUJ\u0104CE (QGroupBox) --- */\n"
"\n"
"QGroupBox {\n"
"    /* U\u017cycie koloru Navbara (#4A89C9) dla tytu\u0142u grupy, aby zachowa\u0107 sp\u00f3jno\u015b\u0107 */\n"
"    color: #4A89C9; \n"
"    font-weight: bold;\n"
"    border: 1px solid #c3cedb; /* Subtelna, jasnoszara ramka */\n"
"    border-radius: 4px;\n"
"    margin-top: 10px; \n"
"    padd"
                        "ing: 10px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    /* Stylizacja tytu\u0142u grupy */\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 0 5px;\n"
"    color: #4A89C9; \n"
"    font-size: 12px;\n"
"}\n"
"\n"
"QTextEdit {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #c3cedb;\n"
"    border-radius: 4px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"/* KOREKTA: Ograniczenie wysoko\u015bci pola tekstowego do wy\u015bwietlania \u015bcie\u017cki pliku */\n"
"QTextEdit#txt_data_input {\n"
"    min-height: 25px; \n"
"    max-height: 35px; /* Nadaje sta\u0142\u0105, ma\u0142\u0105 wysoko\u015b\u0107 */\n"
"}\n"
"\n"
"/* --- WID\u017bET TABELI (QTableWidget) --- */\n"
"\n"
"QTableWidget {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #c3cedb;\n"
"    border-radius: 4px;\n"
"    gridline-color: #e5e5e5; /* Bardzo jasne linie siatki */\n"
"    /* KLUCZOWA POPRAWKA: Ustawienie koloru tekstu dla ca\u0142ej tabeli */\n"
"    color: #1b2735; \n"
"}\n"
"\n"
"/* Na"
                        "g\u0142\u00f3wki kolumn w tabeli */\n"
"\n"
"QHeaderView {\n"
"    /* Ustaw t\u0142o ca\u0142ego nag\u0142\u00f3wka na jasne, takie jak t\u0142o sekcji lub kontenera */\n"
"    background-color: #EFEFEF; \n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #EFEFEF; /* Jasnoszare t\u0142o nag\u0142\u00f3wk\u00f3w */\n"
"    color: #1b2735;\n"
"    padding: 4px;\n"
"    border: 1px solid #c3cedb;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"/* --- OG\u00d3LNE PRZYCISKI (Przycisk w grupie danych, np. btn_load_data) --- */\n"
"/* Uwaga: Te style b\u0119d\u0105 nadpisywa\u0107 style przycisk\u00f3w w navbarze, je\u015bli zostan\u0105 zastosowane globalnie. */\n"
"/* Je\u015bli chcesz, by tylko przyciski w sekcji g\u0142\u00f3wnej mia\u0142y te style, musisz u\u017cy\u0107 specyfikator\u00f3w: QWidget#data_page QPushButton */\n"
"\n"
"QPushButton#btn_load_data, QPushButton#btn_generate_bounds, QPushButton#btn_calculate_stfn, QPushButton#btn_calculate_ranking {\n"
"    background-color: #4A89C9; /* U\u017cyci"
                        "e koloru Navbara jako koloru g\u0142\u00f3wnej akcji */\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    border-radius: 4px;\n"
"    padding: 8px 15px;\n"
"    font-weight: 600;\n"
"    min-height: 25px;\n"
"}\n"
"\n"
"QPushButton#btn_load_data:hover, QPushButton:hover {\n"
"    background-color: #3c72b0;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.data_page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_data_management = QLabel(self.data_page)
        self.lbl_data_management.setObjectName(u"lbl_data_management")
        self.lbl_data_management.setStyleSheet(u"/*font-size: 24px; font-weight: bold;*/")

        self.verticalLayout_2.addWidget(self.lbl_data_management)

        self.data_input_container = QGroupBox(self.data_page)
        self.data_input_container.setObjectName(u"data_input_container")
        self.horizontalLayout_3 = QHBoxLayout(self.data_input_container)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.txt_data_input = QTextEdit(self.data_input_container)
        self.txt_data_input.setObjectName(u"txt_data_input")
        self.txt_data_input.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.txt_data_input.sizePolicy().hasHeightForWidth())
        self.txt_data_input.setSizePolicy(sizePolicy2)
        self.txt_data_input.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.txt_data_input)

        self.btn_load_data = QPushButton(self.data_input_container)
        self.btn_load_data.setObjectName(u"btn_load_data")

        self.horizontalLayout_3.addWidget(self.btn_load_data)


        self.verticalLayout_2.addWidget(self.data_input_container)

        self.data_table_container = QGroupBox(self.data_page)
        self.data_table_container.setObjectName(u"data_table_container")
        self.verticalLayout_5 = QVBoxLayout(self.data_table_container)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tbl_data_view = QTableWidget(self.data_table_container)
        self.tbl_data_view.setObjectName(u"tbl_data_view")

        self.verticalLayout_5.addWidget(self.tbl_data_view)


        self.verticalLayout_2.addWidget(self.data_table_container)

        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 6)
        self.pages.addWidget(self.data_page)
        self.stfn_page = QWidget()
        self.stfn_page.setObjectName(u"stfn_page")
        self.stfn_page.setStyleSheet(u"/* --- BLOK CSS SKOPIOWANY Z GLOBALNEGO --- */\n"
"\n"
"/* T\u0142o centralnej sekcji powinno by\u0107 jasne i neutralne */\n"
"/*\n"
"QWidget {\n"
"    background-color: #F8F9FA;\n"
"}\n"
"*/\n"
"\n"
"/* Og\u00f3lny styl dla etykiet (Label) */\n"
"QLabel {\n"
"    color: #1b2735; /* Ciemny, czytelny tekst */\n"
"}\n"
"\n"
"/* Styl dla g\u0142\u00f3wnego nag\u0142\u00f3wka strony (np. lbl_data_management) */\n"
"QLabel#lbl_stfn_analysis {\n"
"    font-size: 24px; \n"
"    font-weight: bold;\n"
"    padding: 10px 0;\n"
"}\n"
"\n"
"/* KONTENERY GRUPUJ\u0104CE (QGroupBox) */\n"
"\n"
"QGroupBox {\n"
"    color: #4A89C9; \n"
"    font-weight: bold;\n"
"    border: 1px solid #c3cedb;\n"
"    border-radius: 4px;\n"
"    margin-top: 10px; \n"
"    padding: 10px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 0 5px;\n"
"    color: #4A89C9; \n"
"    font-size: 12px;\n"
"}\n"
"\n"
"/* POLA WEJ\u015aCIA DANYCH (QTextEdit, QPlainTextEdit) */\n"
""
                        "\n"
"QTextEdit, QPlainTextEdit {\n"
"    background-color: #FFFFFF;\n"
"	color: #1b2735;\n"
"    border: 1px solid #c3cedb;\n"
"    border-radius: 4px;\n"
"    padding: 5px;\n"
"    /* Ograniczenie wysoko\u015bci dla sp\u00f3jno\u015bci z przyciskami (domy\u015blny dla Input\u00f3w) */\n"
"    max-height: 35px;\n"
"}\n"
"QTextEdit#txt_bounds, QPlainTextEdit#txt_bounds_data {\n"
"    /* Dla pola na Bounds potrzebujemy wi\u0119cej miejsca */\n"
"    max-height: 70px;\n"
"	color: #1b2735;\n"
"}\n"
"\n"
"/* PRZYCISKI AKCJI (Primary Buttons) */\n"
"\n"
"QPushButton#btn_generate_bounds, QPushButton#btn_calculate_stfn {\n"
"    background-color: #4A89C9;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    border-radius: 4px;\n"
"    padding: 8px 15px;\n"
"    font-weight: 600;\n"
"    min-height: 25px;\n"
"}\n"
"\n"
"QPushButton#btn_generate_bounds:hover, QPushButton#btn_calculate_stfn:hover {\n"
"    background-color: #3c72b0;\n"
"}\n"
"\n"
"/* PRZYCISKI NAWIGACYJNE WIZUALIZACJI (Secondary Buttons) */\n"
"QGroupBo"
                        "x#stfn_visualization_container QPushButton {\n"
"    background-color: #75aadb; /* \u0141agodniejszy b\u0142\u0119kit */\n"
"    color: #FFFFFF;\n"
"    border: 1px solid #3c72b0;\n"
"    border-radius: 4px;\n"
"    padding: 4px 8px;\n"
"    font-weight: 500;\n"
"    min-height: 20px;\n"
"}\n"
"QGroupBox#stfn_visualization_container QPushButton:hover {\n"
"    background-color: #619bd1;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.stfn_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lbl_stfn_analysis = QLabel(self.stfn_page)
        self.lbl_stfn_analysis.setObjectName(u"lbl_stfn_analysis")
        self.lbl_stfn_analysis.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.lbl_stfn_analysis)

        self.stfn_main_container = QWidget(self.stfn_page)
        self.stfn_main_container.setObjectName(u"stfn_main_container")
        self.horizontalLayout_4 = QHBoxLayout(self.stfn_main_container)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.stfn_parameters_container = QGroupBox(self.stfn_main_container)
        self.stfn_parameters_container.setObjectName(u"stfn_parameters_container")
        self.verticalLayout_6 = QVBoxLayout(self.stfn_parameters_container)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lbl_bounds = QLabel(self.stfn_parameters_container)
        self.lbl_bounds.setObjectName(u"lbl_bounds")

        self.verticalLayout_6.addWidget(self.lbl_bounds)

        self.txt_bounds_data = QPlainTextEdit(self.stfn_parameters_container)
        self.txt_bounds_data.setObjectName(u"txt_bounds_data")

        self.verticalLayout_6.addWidget(self.txt_bounds_data)

        self.btn_generate_bounds = QPushButton(self.stfn_parameters_container)
        self.btn_generate_bounds.setObjectName(u"btn_generate_bounds")

        self.verticalLayout_6.addWidget(self.btn_generate_bounds)

        self.lbl_alternatives_ranking = QLabel(self.stfn_parameters_container)
        self.lbl_alternatives_ranking.setObjectName(u"lbl_alternatives_ranking")

        self.verticalLayout_6.addWidget(self.lbl_alternatives_ranking)

        self.txt_alternatives_ranking = QTextEdit(self.stfn_parameters_container)
        self.txt_alternatives_ranking.setObjectName(u"txt_alternatives_ranking")

        self.verticalLayout_6.addWidget(self.txt_alternatives_ranking)

        self.lbl_criteria_weights = QLabel(self.stfn_parameters_container)
        self.lbl_criteria_weights.setObjectName(u"lbl_criteria_weights")

        self.verticalLayout_6.addWidget(self.lbl_criteria_weights)

        self.txt_criteria_weights = QTextEdit(self.stfn_parameters_container)
        self.txt_criteria_weights.setObjectName(u"txt_criteria_weights")

        self.verticalLayout_6.addWidget(self.txt_criteria_weights)

        self.lbl_population_size = QLabel(self.stfn_parameters_container)
        self.lbl_population_size.setObjectName(u"lbl_population_size")

        self.verticalLayout_6.addWidget(self.lbl_population_size)

        self.txt_population_size = QTextEdit(self.stfn_parameters_container)
        self.txt_population_size.setObjectName(u"txt_population_size")

        self.verticalLayout_6.addWidget(self.txt_population_size)

        self.lbl_epoch_size = QLabel(self.stfn_parameters_container)
        self.lbl_epoch_size.setObjectName(u"lbl_epoch_size")

        self.verticalLayout_6.addWidget(self.lbl_epoch_size)

        self.txt_epoch_size = QTextEdit(self.stfn_parameters_container)
        self.txt_epoch_size.setObjectName(u"txt_epoch_size")

        self.verticalLayout_6.addWidget(self.txt_epoch_size)

        self.lbl_c1_size = QLabel(self.stfn_parameters_container)
        self.lbl_c1_size.setObjectName(u"lbl_c1_size")

        self.verticalLayout_6.addWidget(self.lbl_c1_size)

        self.txt_c1_size = QTextEdit(self.stfn_parameters_container)
        self.txt_c1_size.setObjectName(u"txt_c1_size")

        self.verticalLayout_6.addWidget(self.txt_c1_size)

        self.lbl_c2_size = QLabel(self.stfn_parameters_container)
        self.lbl_c2_size.setObjectName(u"lbl_c2_size")

        self.verticalLayout_6.addWidget(self.lbl_c2_size)

        self.txt_c2_size = QTextEdit(self.stfn_parameters_container)
        self.txt_c2_size.setObjectName(u"txt_c2_size")

        self.verticalLayout_6.addWidget(self.txt_c2_size)

        self.lbl_w_size = QLabel(self.stfn_parameters_container)
        self.lbl_w_size.setObjectName(u"lbl_w_size")

        self.verticalLayout_6.addWidget(self.lbl_w_size)

        self.txt_w_size = QTextEdit(self.stfn_parameters_container)
        self.txt_w_size.setObjectName(u"txt_w_size")

        self.verticalLayout_6.addWidget(self.txt_w_size)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)

        self.btn_calculate_stfn = QPushButton(self.stfn_parameters_container)
        self.btn_calculate_stfn.setObjectName(u"btn_calculate_stfn")

        self.verticalLayout_6.addWidget(self.btn_calculate_stfn)


        self.horizontalLayout_4.addWidget(self.stfn_parameters_container)

        self.stfn_results_and_vis_wrapper = QWidget(self.stfn_main_container)
        self.stfn_results_and_vis_wrapper.setObjectName(u"stfn_results_and_vis_wrapper")
        self.verticalLayout_7 = QVBoxLayout(self.stfn_results_and_vis_wrapper)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.stfn_results_container = QGroupBox(self.stfn_results_and_vis_wrapper)
        self.stfn_results_container.setObjectName(u"stfn_results_container")
        self.horizontalLayout_5 = QHBoxLayout(self.stfn_results_container)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.txt_stfn_results = QTextEdit(self.stfn_results_container)
        self.txt_stfn_results.setObjectName(u"txt_stfn_results")
        self.txt_stfn_results.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.txt_stfn_results)


        self.verticalLayout_7.addWidget(self.stfn_results_container)

        self.stfn_visualization_container = QGroupBox(self.stfn_results_and_vis_wrapper)
        self.stfn_visualization_container.setObjectName(u"stfn_visualization_container")
        self.verticalLayout_8 = QVBoxLayout(self.stfn_visualization_container)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_3_left = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3_left)

        self.btn_previous_visualization = QPushButton(self.stfn_visualization_container)
        self.btn_previous_visualization.setObjectName(u"btn_previous_visualization")
        self.btn_previous_visualization.setMinimumSize(QSize(100, 30))
        self.btn_previous_visualization.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_6.addWidget(self.btn_previous_visualization)

        self.btn_next_visualization = QPushButton(self.stfn_visualization_container)
        self.btn_next_visualization.setObjectName(u"btn_next_visualization")
        self.btn_next_visualization.setMinimumSize(QSize(100, 30))
        self.btn_next_visualization.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_6.addWidget(self.btn_next_visualization)

        self.horizontalSpacer_3_right = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3_right)


        self.verticalLayout_8.addLayout(self.horizontalLayout_6)

        self.gv_stfn_visualization = QGraphicsView(self.stfn_visualization_container)
        self.gv_stfn_visualization.setObjectName(u"gv_stfn_visualization")

        self.verticalLayout_8.addWidget(self.gv_stfn_visualization)


        self.verticalLayout_7.addWidget(self.stfn_visualization_container)

        self.verticalLayout_7.setStretch(1, 1)

        self.horizontalLayout_4.addWidget(self.stfn_results_and_vis_wrapper)

        self.horizontalLayout_4.setStretch(0, 2)
        self.horizontalLayout_4.setStretch(1, 3)

        self.verticalLayout_3.addWidget(self.stfn_main_container)

        self.verticalLayout_3.setStretch(1, 1)
        self.pages.addWidget(self.stfn_page)
        self.mcda_page = QWidget()
        self.mcda_page.setObjectName(u"mcda_page")
        self.mcda_page.setStyleSheet(u"/* --- OG\u00d3LNY KONTEKST DLA STRONY MCDA --- */\n"
"\n"
"/* Og\u00f3lny styl dla etykiet (Label) */\n"
"QWidget#mcda_page QLabel {\n"
"    color: #1b2735; /* Ciemny, czytelny tekst */\n"
"}\n"
"\n"
"/* Styl dla g\u0142\u00f3wnego nag\u0142\u00f3wka strony */\n"
"QLabel#lbl_mcda_title {\n"
"    font-size: 24px; \n"
"    font-weight: bold;\n"
"    padding: 10px 0;\n"
"}\n"
"\n"
"/* --- KONTENERY GRUPUJ\u0104CE (QGroupBox) --- */\n"
"\n"
"QWidget#mcda_page QGroupBox {\n"
"    color: #4A89C9; \n"
"    font-weight: bold;\n"
"    border: 1px solid #c3cedb;\n"
"    border-radius: 4px;\n"
"    margin-top: 10px; \n"
"    padding: 10px;\n"
"}\n"
"\n"
"QWidget#mcda_page QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 0 5px;\n"
"    color: #4A89C9; \n"
"    font-size: 12px;\n"
"}\n"
"\n"
"/* --- POLA WEJ\u015aCIA DANYCH (QTextEdit i QComboBox) --- */\n"
"\n"
"QWidget#mcda_page QTextEdit {\n"
"    background-color: #FFFFFF;\n"
"	color: #1b2735;\n"
"    border"
                        ": 1px solid #c3cedb;\n"
"    border-radius: 4px;\n"
"    padding: 5px;\n"
"    /* Ograniczenie wysoko\u015bci dla sp\u00f3jno\u015bci */\n"
"    max-height: 35px;\n"
"}\n"
"QWidget#mcda_page QComboBox {\n"
"    background-color: #FFFFFF;\n"
"	color: #1b2735;\n"
"    border: 1px solid #c3cedb;\n"
"    border-radius: 4px;\n"
"    padding: 5px;\n"
"    min-height: 25px;\n"
"}\n"
"\n"
"\n"
"/* --- PRZYCISKI AKCJI (Primary Buttons - np. Calculate Ranking) --- */\n"
"\n"
"QPushButton#btn_calculate_ranking {\n"
"    background-color: #4A89C9;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    border-radius: 4px;\n"
"    padding: 8px 15px;\n"
"    font-weight: 600;\n"
"    min-height: 25px;\n"
"}\n"
"\n"
"QPushButton#btn_calculate_ranking:hover {\n"
"    background-color: #3c72b0;\n"
"}\n"
"\n"
"/* --- PRZYCISKI WIZUALIZACJI (Secondary Buttons - np. Rank Comaprison) --- */\n"
"QGroupBox#mcda_visualization_container QPushButton {\n"
"    background-color: #75aadb; /* \u0141agodniejszy b\u0142\u0119kit */\n"
"    col"
                        "or: #FFFFFF;\n"
"    /* Usuni\u0119to 1px solid #3c72b0 na rzecz bardziej p\u0142askiego stylu */\n"
"    border: none; \n"
"    border-radius: 4px;\n"
"    padding: 4px 8px;\n"
"    font-weight: 500;\n"
"    min-height: 20px;\n"
"}\n"
"QGroupBox#mcda_visualization_container QPushButton:hover {\n"
"    background-color: #619bd1;\n"
"}\n"
"QGroupBox#mcda_visualization_container QPushButton:pressed {\n"
"    background-color: #538cc4;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.mcda_page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lbl_mcda_title = QLabel(self.mcda_page)
        self.lbl_mcda_title.setObjectName(u"lbl_mcda_title")
        self.lbl_mcda_title.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.lbl_mcda_title)

        self.mcda_main_container = QWidget(self.mcda_page)
        self.mcda_main_container.setObjectName(u"mcda_main_container")
        self.horizontalLayout_4_mcda = QHBoxLayout(self.mcda_main_container)
        self.horizontalLayout_4_mcda.setObjectName(u"horizontalLayout_4_mcda")
        self.mcda_config_container = QGroupBox(self.mcda_main_container)
        self.mcda_config_container.setObjectName(u"mcda_config_container")
        self.verticalLayout_9 = QVBoxLayout(self.mcda_config_container)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.lbl_mcda_methods = QLabel(self.mcda_config_container)
        self.lbl_mcda_methods.setObjectName(u"lbl_mcda_methods")

        self.verticalLayout_9.addWidget(self.lbl_mcda_methods)

        self.cb_mcda_method = QComboBox(self.mcda_config_container)
        self.cb_mcda_method.addItem("")
        self.cb_mcda_method.addItem("")
        self.cb_mcda_method.addItem("")
        self.cb_mcda_method.addItem("")
        self.cb_mcda_method.setObjectName(u"cb_mcda_method")

        self.verticalLayout_9.addWidget(self.cb_mcda_method)

        self.lbl_criteria_types = QLabel(self.mcda_config_container)
        self.lbl_criteria_types.setObjectName(u"lbl_criteria_types")

        self.verticalLayout_9.addWidget(self.lbl_criteria_types)

        self.txt_criteria_types = QTextEdit(self.mcda_config_container)
        self.txt_criteria_types.setObjectName(u"txt_criteria_types")

        self.verticalLayout_9.addWidget(self.txt_criteria_types)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_4)

        self.btn_calculate_ranking = QPushButton(self.mcda_config_container)
        self.btn_calculate_ranking.setObjectName(u"btn_calculate_ranking")

        self.verticalLayout_9.addWidget(self.btn_calculate_ranking)


        self.horizontalLayout_4_mcda.addWidget(self.mcda_config_container)

        self.mcda_results_and_vis_wrapper = QWidget(self.mcda_main_container)
        self.mcda_results_and_vis_wrapper.setObjectName(u"mcda_results_and_vis_wrapper")
        self.verticalLayout_10 = QVBoxLayout(self.mcda_results_and_vis_wrapper)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.mcda_new_ranking_container = QGroupBox(self.mcda_results_and_vis_wrapper)
        self.mcda_new_ranking_container.setObjectName(u"mcda_new_ranking_container")
        self.horizontalLayout_7 = QHBoxLayout(self.mcda_new_ranking_container)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.txt_new_ranking = QTextEdit(self.mcda_new_ranking_container)
        self.txt_new_ranking.setObjectName(u"txt_new_ranking")
        self.txt_new_ranking.setReadOnly(True)

        self.horizontalLayout_7.addWidget(self.txt_new_ranking)


        self.verticalLayout_10.addWidget(self.mcda_new_ranking_container)

        self.mcda_old_ranking_container = QGroupBox(self.mcda_results_and_vis_wrapper)
        self.mcda_old_ranking_container.setObjectName(u"mcda_old_ranking_container")
        self.horizontalLayout_8 = QHBoxLayout(self.mcda_old_ranking_container)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.txt_old_ranking = QTextEdit(self.mcda_old_ranking_container)
        self.txt_old_ranking.setObjectName(u"txt_old_ranking")
        self.txt_old_ranking.setReadOnly(True)

        self.horizontalLayout_8.addWidget(self.txt_old_ranking)


        self.verticalLayout_10.addWidget(self.mcda_old_ranking_container)

        self.mcda_visualization_container = QGroupBox(self.mcda_results_and_vis_wrapper)
        self.mcda_visualization_container.setObjectName(u"mcda_visualization_container")
        self.verticalLayout_11 = QVBoxLayout(self.mcda_visualization_container)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_4_left = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_4_left)

        self.btn_compare_ranks = QPushButton(self.mcda_visualization_container)
        self.btn_compare_ranks.setObjectName(u"btn_compare_ranks")
        self.btn_compare_ranks.setMinimumSize(QSize(120, 28))

        self.horizontalLayout_9.addWidget(self.btn_compare_ranks)

        self.btn_rank_correlation = QPushButton(self.mcda_visualization_container)
        self.btn_rank_correlation.setObjectName(u"btn_rank_correlation")
        self.btn_rank_correlation.setMinimumSize(QSize(120, 28))

        self.horizontalLayout_9.addWidget(self.btn_rank_correlation)

        self.horizontalSpacer_4_right = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_4_right)


        self.verticalLayout_11.addLayout(self.horizontalLayout_9)

        self.gv_mcda_visualization = QGraphicsView(self.mcda_visualization_container)
        self.gv_mcda_visualization.setObjectName(u"gv_mcda_visualization")

        self.verticalLayout_11.addWidget(self.gv_mcda_visualization)


        self.verticalLayout_10.addWidget(self.mcda_visualization_container)

        self.verticalLayout_10.setStretch(2, 1)

        self.horizontalLayout_4_mcda.addWidget(self.mcda_results_and_vis_wrapper)

        self.horizontalLayout_4_mcda.setStretch(0, 2)
        self.horizontalLayout_4_mcda.setStretch(1, 3)

        self.verticalLayout_4.addWidget(self.mcda_main_container)

        self.verticalLayout_4.setStretch(1, 1)
        self.pages.addWidget(self.mcda_page)

        self.horizontalLayout.addWidget(self.pages)

        self.horizontalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_app_title.setText(QCoreApplication.translate("MainWindow", u"pymcdm-reidentify", None))
        self.btn_data_page.setText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.btn_stfn_page.setText(QCoreApplication.translate("MainWindow", u"stfn", None))
        self.btn_mcda_page.setText(QCoreApplication.translate("MainWindow", u"mcda", None))
        self.lbl_data_management.setText(QCoreApplication.translate("MainWindow", u"Data Management", None))
        self.data_input_container.setTitle(QCoreApplication.translate("MainWindow", u"Data Import", None))
        self.btn_load_data.setText(QCoreApplication.translate("MainWindow", u"Load Data", None))
        self.data_table_container.setTitle(QCoreApplication.translate("MainWindow", u"Data Preview", None))
        self.lbl_stfn_analysis.setText(QCoreApplication.translate("MainWindow", u"STFN Analysis", None))
        self.stfn_parameters_container.setTitle(QCoreApplication.translate("MainWindow", u"Parameters", None))
        self.lbl_bounds.setText(QCoreApplication.translate("MainWindow", u"Bounds for Criteria", None))
        self.btn_generate_bounds.setText(QCoreApplication.translate("MainWindow", u"Generate Bounds", None))
        self.lbl_alternatives_ranking.setText(QCoreApplication.translate("MainWindow", u"Alternatives Ranking", None))
        self.lbl_criteria_weights.setText(QCoreApplication.translate("MainWindow", u"Criteria Weights", None))
        self.lbl_population_size.setText(QCoreApplication.translate("MainWindow", u"Population Size", None))
        self.lbl_epoch_size.setText(QCoreApplication.translate("MainWindow", u"Epoch Size", None))
        self.lbl_c1_size.setText(QCoreApplication.translate("MainWindow", u"C1 Size", None))
        self.lbl_c2_size.setText(QCoreApplication.translate("MainWindow", u"C2 Size", None))
        self.lbl_w_size.setText(QCoreApplication.translate("MainWindow", u"W Size", None))
        self.btn_calculate_stfn.setText(QCoreApplication.translate("MainWindow", u"Calculate STFN", None))
        self.stfn_results_container.setTitle(QCoreApplication.translate("MainWindow", u"Results", None))
        self.stfn_visualization_container.setTitle(QCoreApplication.translate("MainWindow", u"Visualization", None))
        self.btn_previous_visualization.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.btn_next_visualization.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.lbl_mcda_title.setText(QCoreApplication.translate("MainWindow", u"MCDA Methods", None))
        self.mcda_config_container.setTitle(QCoreApplication.translate("MainWindow", u"Method Configuration", None))
        self.lbl_mcda_methods.setText(QCoreApplication.translate("MainWindow", u"MCDA Method", None))
        self.cb_mcda_method.setItemText(0, QCoreApplication.translate("MainWindow", u"TOPSIS", None))
        self.cb_mcda_method.setItemText(1, QCoreApplication.translate("MainWindow", u"WAPAS", None))
        self.cb_mcda_method.setItemText(2, QCoreApplication.translate("MainWindow", u"VIKOR", None))
        self.cb_mcda_method.setItemText(3, QCoreApplication.translate("MainWindow", u"MABAC", None))

        self.lbl_criteria_types.setText(QCoreApplication.translate("MainWindow", u"Types of criteria", None))
        self.btn_calculate_ranking.setText(QCoreApplication.translate("MainWindow", u"Calculate Ranking", None))
        self.mcda_new_ranking_container.setTitle(QCoreApplication.translate("MainWindow", u"New Ranking", None))
        self.mcda_old_ranking_container.setTitle(QCoreApplication.translate("MainWindow", u"Old Ranking", None))
        self.mcda_visualization_container.setTitle(QCoreApplication.translate("MainWindow", u"Visualization", None))
        self.btn_compare_ranks.setText(QCoreApplication.translate("MainWindow", u"Rank Comparison", None))
        self.btn_rank_correlation.setText(QCoreApplication.translate("MainWindow", u"Rank Correlation", None))
    # retranslateUi

