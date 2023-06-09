# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QMainWindow, QProgressBar, QPushButton, QRadioButton,
    QSizePolicy, QTextEdit, QWidget)

from mplwidget import MplWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 762)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.readout_grid = QGridLayout()
        self.readout_grid.setObjectName(u"readout_grid")
        self.readout_grid.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.readout_connect_line = QLineEdit(self.centralwidget)
        self.readout_connect_line.setObjectName(u"readout_connect_line")

        self.readout_grid.addWidget(self.readout_connect_line, 2, 0, 1, 1)

        self.readout_voltage_line = QLineEdit(self.centralwidget)
        self.readout_voltage_line.setObjectName(u"readout_voltage_line")
        font = QFont()
        font.setPointSize(14)
        self.readout_voltage_line.setFont(font)

        self.readout_grid.addWidget(self.readout_voltage_line, 3, 1, 1, 1)

        self.readout_label = QLabel(self.centralwidget)
        self.readout_label.setObjectName(u"readout_label")
        font1 = QFont()
        font1.setPointSize(20)
        self.readout_label.setFont(font1)
        self.readout_label.setAlignment(Qt.AlignCenter)

        self.readout_grid.addWidget(self.readout_label, 0, 0, 1, 2)

        self.readout_voltage_label = QLabel(self.centralwidget)
        self.readout_voltage_label.setObjectName(u"readout_voltage_label")
        self.readout_voltage_label.setFont(font)

        self.readout_grid.addWidget(self.readout_voltage_label, 3, 0, 1, 1)

        self.readout_connect_pushbutton = QPushButton(self.centralwidget)
        self.readout_connect_pushbutton.setObjectName(u"readout_connect_pushbutton")

        self.readout_grid.addWidget(self.readout_connect_pushbutton, 2, 1, 1, 1)

        self.readout_plot = MplWidget(self.centralwidget)
        self.readout_plot.setObjectName(u"readout_plot")
        self.readout_plot.setMinimumSize(QSize(640, 480))

        self.readout_grid.addWidget(self.readout_plot, 1, 0, 1, 2)

        self.laser_label = QLabel(self.centralwidget)
        self.laser_label.setObjectName(u"laser_label")
        self.laser_label.setFont(font1)
        self.laser_label.setAlignment(Qt.AlignCenter)

        self.readout_grid.addWidget(self.laser_label, 4, 0, 1, 2)

        self.recording_layout = QHBoxLayout()
        self.recording_layout.setObjectName(u"recording_layout")
        self.recordin_status_text = QTextEdit(self.centralwidget)
        self.recordin_status_text.setObjectName(u"recordin_status_text")
#if QT_CONFIG(tooltip)
        self.recordin_status_text.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.recordin_status_text.setFrameShape(QFrame.StyledPanel)
        self.recordin_status_text.setReadOnly(True)

        self.recording_layout.addWidget(self.recordin_status_text)

        self.record_target_line = QLineEdit(self.centralwidget)
        self.record_target_line.setObjectName(u"record_target_line")

        self.recording_layout.addWidget(self.record_target_line)

        self.toggle_recording_pushbutton = QPushButton(self.centralwidget)
        self.toggle_recording_pushbutton.setObjectName(u"toggle_recording_pushbutton")

        self.recording_layout.addWidget(self.toggle_recording_pushbutton)

        self.tag_text_line = QLineEdit(self.centralwidget)
        self.tag_text_line.setObjectName(u"tag_text_line")

        self.recording_layout.addWidget(self.tag_text_line)

        self.tag_event_pushbutton = QPushButton(self.centralwidget)
        self.tag_event_pushbutton.setObjectName(u"tag_event_pushbutton")

        self.recording_layout.addWidget(self.tag_event_pushbutton)


        self.readout_grid.addLayout(self.recording_layout, 5, 0, 1, 2)


        self.horizontalLayout.addLayout(self.readout_grid)

        self.signal_grid = QGridLayout()
        self.signal_grid.setObjectName(u"signal_grid")
        self.signal_grid.setHorizontalSpacing(0)
        self.output_label = QLabel(self.centralwidget)
        self.output_label.setObjectName(u"output_label")
        self.output_label.setFont(font1)
        self.output_label.setAlignment(Qt.AlignCenter)

        self.signal_grid.addWidget(self.output_label, 19, 0, 1, 5)

        self.sampler_progress = QProgressBar(self.centralwidget)
        self.sampler_progress.setObjectName(u"sampler_progress")
        self.sampler_progress.setValue(0)

        self.signal_grid.addWidget(self.sampler_progress, 7, 0, 1, 4)

        self.pulse_function_combobox = QComboBox(self.centralwidget)
        self.pulse_function_combobox.setObjectName(u"pulse_function_combobox")

        self.signal_grid.addWidget(self.pulse_function_combobox, 11, 0, 1, 1)

        self.stepsize_frequency_line = QLineEdit(self.centralwidget)
        self.stepsize_frequency_line.setObjectName(u"stepsize_frequency_line")

        self.signal_grid.addWidget(self.stepsize_frequency_line, 6, 3, 1, 1)

        self.signal_quickedit_label = QLabel(self.centralwidget)
        self.signal_quickedit_label.setObjectName(u"signal_quickedit_label")
        self.signal_quickedit_label.setFont(font)
        self.signal_quickedit_label.setAlignment(Qt.AlignCenter)

        self.signal_grid.addWidget(self.signal_quickedit_label, 8, 0, 1, 5)

        self.try_ip_pushbutton = QPushButton(self.centralwidget)
        self.try_ip_pushbutton.setObjectName(u"try_ip_pushbutton")

        self.signal_grid.addWidget(self.try_ip_pushbutton, 2, 4, 1, 1)

        self.pulse_settings_layout = QHBoxLayout()
        self.pulse_settings_layout.setObjectName(u"pulse_settings_layout")
        self.pulse_period_line = QLineEdit(self.centralwidget)
        self.pulse_period_line.setObjectName(u"pulse_period_line")

        self.pulse_settings_layout.addWidget(self.pulse_period_line)

        self.pulse_width_line = QLineEdit(self.centralwidget)
        self.pulse_width_line.setObjectName(u"pulse_width_line")

        self.pulse_settings_layout.addWidget(self.pulse_width_line)

        self.pulse_timeunits_combobox = QComboBox(self.centralwidget)
        self.pulse_timeunits_combobox.setObjectName(u"pulse_timeunits_combobox")

        self.pulse_settings_layout.addWidget(self.pulse_timeunits_combobox)


        self.signal_grid.addLayout(self.pulse_settings_layout, 11, 1, 1, 3)

        self.signal_generator_label = QLabel(self.centralwidget)
        self.signal_generator_label.setObjectName(u"signal_generator_label")
        font2 = QFont()
        font2.setPointSize(20)
        font2.setUnderline(False)
        font2.setKerning(True)
        self.signal_generator_label.setFont(font2)
        self.signal_generator_label.setText(u"Signal Generator Settings")
        self.signal_generator_label.setAlignment(Qt.AlignCenter)

        self.signal_grid.addWidget(self.signal_generator_label, 0, 0, 1, 5)

        self.external_start_pushbutton = QPushButton(self.centralwidget)
        self.external_start_pushbutton.setObjectName(u"external_start_pushbutton")

        self.signal_grid.addWidget(self.external_start_pushbutton, 17, 3, 1, 1)

        self.signal_setting_pushbutton = QPushButton(self.centralwidget)
        self.signal_setting_pushbutton.setObjectName(u"signal_setting_pushbutton")

        self.signal_grid.addWidget(self.signal_setting_pushbutton, 9, 4, 1, 1)

        self.external_modulation_label = QLabel(self.centralwidget)
        self.external_modulation_label.setObjectName(u"external_modulation_label")
        self.external_modulation_label.setFont(font)
        self.external_modulation_label.setAlignment(Qt.AlignCenter)

        self.signal_grid.addWidget(self.external_modulation_label, 15, 0, 1, 5)

        self.sample_frequency_pushbutton = QPushButton(self.centralwidget)
        self.sample_frequency_pushbutton.setObjectName(u"sample_frequency_pushbutton")

        self.signal_grid.addWidget(self.sample_frequency_pushbutton, 7, 4, 1, 1)

        self.signal_frequency_layout = QHBoxLayout()
        self.signal_frequency_layout.setObjectName(u"signal_frequency_layout")
        self.signal_frequency_line = QLineEdit(self.centralwidget)
        self.signal_frequency_line.setObjectName(u"signal_frequency_line")

        self.signal_frequency_layout.addWidget(self.signal_frequency_line)

        self.frequency_units_combobox = QComboBox(self.centralwidget)
        self.frequency_units_combobox.setObjectName(u"frequency_units_combobox")

        self.signal_frequency_layout.addWidget(self.frequency_units_combobox)


        self.signal_grid.addLayout(self.signal_frequency_layout, 9, 1, 1, 1)

        self.signal_amplitude_layout = QHBoxLayout()
        self.signal_amplitude_layout.setObjectName(u"signal_amplitude_layout")
        self.signal_amplitude_line = QLineEdit(self.centralwidget)
        self.signal_amplitude_line.setObjectName(u"signal_amplitude_line")

        self.signal_amplitude_layout.addWidget(self.signal_amplitude_line)

        self.amplitude_units_combobox = QComboBox(self.centralwidget)
        self.amplitude_units_combobox.setObjectName(u"amplitude_units_combobox")

        self.signal_amplitude_layout.addWidget(self.amplitude_units_combobox)


        self.signal_grid.addLayout(self.signal_amplitude_layout, 9, 0, 1, 1)

        self.pulse_toggle_pushbutton = QPushButton(self.centralwidget)
        self.pulse_toggle_pushbutton.setObjectName(u"pulse_toggle_pushbutton")

        self.signal_grid.addWidget(self.pulse_toggle_pushbutton, 11, 4, 1, 1)

        self.frequency_sampler_label = QLabel(self.centralwidget)
        self.frequency_sampler_label.setObjectName(u"frequency_sampler_label")
        self.frequency_sampler_label.setFont(font)
        self.frequency_sampler_label.setAlignment(Qt.AlignCenter)

        self.signal_grid.addWidget(self.frequency_sampler_label, 4, 0, 1, 5)

        self.target_ip_line = QLineEdit(self.centralwidget)
        self.target_ip_line.setObjectName(u"target_ip_line")
#if QT_CONFIG(tooltip)
        self.target_ip_line.setToolTip(u"")
#endif // QT_CONFIG(tooltip)

        self.signal_grid.addWidget(self.target_ip_line, 2, 0, 1, 4)

        self.dump_pulse_info_pushbutton = QPushButton(self.centralwidget)
        self.dump_pulse_info_pushbutton.setObjectName(u"dump_pulse_info_pushbutton")

        self.signal_grid.addWidget(self.dump_pulse_info_pushbutton, 14, 4, 1, 1)

        self.from_frequency_line = QLineEdit(self.centralwidget)
        self.from_frequency_line.setObjectName(u"from_frequency_line")
        self.from_frequency_line.setPlaceholderText(u"From")

        self.signal_grid.addWidget(self.from_frequency_line, 6, 0, 1, 1)

        self.dump_err_pushbutton = QPushButton(self.centralwidget)
        self.dump_err_pushbutton.setObjectName(u"dump_err_pushbutton")

        self.signal_grid.addWidget(self.dump_err_pushbutton, 14, 1, 1, 1)

        self.output_textedit = QTextEdit(self.centralwidget)
        self.output_textedit.setObjectName(u"output_textedit")

        self.signal_grid.addWidget(self.output_textedit, 20, 0, 1, 5)

        self.sample_units_combobox = QComboBox(self.centralwidget)
        self.sample_units_combobox.setObjectName(u"sample_units_combobox")

        self.signal_grid.addWidget(self.sample_units_combobox, 6, 4, 1, 1)

        self.dump_signal_setting_pushbutton = QPushButton(self.centralwidget)
        self.dump_signal_setting_pushbutton.setObjectName(u"dump_signal_setting_pushbutton")

        self.signal_grid.addWidget(self.dump_signal_setting_pushbutton, 14, 0, 1, 1)

        self.external_stop_pushbutton = QPushButton(self.centralwidget)
        self.external_stop_pushbutton.setObjectName(u"external_stop_pushbutton")

        self.signal_grid.addWidget(self.external_stop_pushbutton, 17, 4, 1, 1)

        self.pulse_label = QLabel(self.centralwidget)
        self.pulse_label.setObjectName(u"pulse_label")
        self.pulse_label.setFont(font)
        self.pulse_label.setAlignment(Qt.AlignCenter)

        self.signal_grid.addWidget(self.pulse_label, 10, 0, 1, 5)

        self.to_frequency_line = QLineEdit(self.centralwidget)
        self.to_frequency_line.setObjectName(u"to_frequency_line")

        self.signal_grid.addWidget(self.to_frequency_line, 6, 1, 1, 1)

        self.external_pulse_radiobutton = QRadioButton(self.centralwidget)
        self.external_pulse_radiobutton.setObjectName(u"external_pulse_radiobutton")

        self.signal_grid.addWidget(self.external_pulse_radiobutton, 17, 0, 1, 1)

        self.external_modulation_combobox = QComboBox(self.centralwidget)
        self.external_modulation_combobox.setObjectName(u"external_modulation_combobox")

        self.signal_grid.addWidget(self.external_modulation_combobox, 17, 1, 1, 1)


        self.horizontalLayout.addLayout(self.signal_grid)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.sample_units_combobox.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.readout_connect_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Target GPIB Adress", None))
        self.readout_voltage_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Not Connected", None))
        self.readout_label.setText(QCoreApplication.translate("MainWindow", u"Intensity Readout", None))
        self.readout_voltage_label.setText(QCoreApplication.translate("MainWindow", u"Current Value:", None))
        self.readout_connect_pushbutton.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.laser_label.setText(QCoreApplication.translate("MainWindow", u"Recording", None))
        self.record_target_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Filename", None))
        self.toggle_recording_pushbutton.setText(QCoreApplication.translate("MainWindow", u"Toggle Recording", None))
        self.tag_text_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Tag Text", None))
        self.tag_event_pushbutton.setText(QCoreApplication.translate("MainWindow", u"Tag Event", None))
        self.output_label.setText(QCoreApplication.translate("MainWindow", u"Output Console", None))
        self.pulse_function_combobox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pulse Function", None))
        self.stepsize_frequency_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Step Size", None))
        self.signal_quickedit_label.setText(QCoreApplication.translate("MainWindow", u"Quick Settings", None))
        self.try_ip_pushbutton.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.pulse_period_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pulse Period", None))
        self.pulse_width_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pulse Width", None))
        self.external_start_pushbutton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.signal_setting_pushbutton.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.external_modulation_label.setText(QCoreApplication.translate("MainWindow", u"External Pulse Modulation Settings", None))
        self.sample_frequency_pushbutton.setText(QCoreApplication.translate("MainWindow", u"Sample", None))
        self.signal_frequency_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Frequency", None))
        self.frequency_units_combobox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Units", None))
        self.signal_amplitude_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Amplitude", None))
        self.amplitude_units_combobox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Units", None))
        self.pulse_toggle_pushbutton.setText(QCoreApplication.translate("MainWindow", u"Toggle Pulse", None))
        self.frequency_sampler_label.setText(QCoreApplication.translate("MainWindow", u"Frequency Sampler", None))
        self.target_ip_line.setText("")
        self.target_ip_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Target Adress", None))
        self.dump_pulse_info_pushbutton.setText(QCoreApplication.translate("MainWindow", u"Dump Pulse Info", None))
        self.dump_err_pushbutton.setText(QCoreApplication.translate("MainWindow", u"Dump Device Errors", None))
        self.sample_units_combobox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Units", None))
        self.dump_signal_setting_pushbutton.setText(QCoreApplication.translate("MainWindow", u"Dump device Settings", None))
        self.external_stop_pushbutton.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.pulse_label.setText(QCoreApplication.translate("MainWindow", u"Internal Pulse Modulation Settings", None))
        self.to_frequency_line.setText("")
        self.to_frequency_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"To", None))
        self.external_pulse_radiobutton.setText(QCoreApplication.translate("MainWindow", u"Toggle PulseBlaster", None))
        self.external_modulation_combobox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"External Modulation Program", None))
    # retranslateUi

