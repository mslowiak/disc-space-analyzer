from PyQt5 import uic
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QWidget, QLabel

from controller.advanced_search_async import AdvancedSearchThread


class AdvancedSearchWidget(QWidget):
    """
    Widget class with advanced search view.
    """

    sig = pyqtSignal(str)

    def __init__(self, parent=None):
        """"
        Init method.
        Loads view defined in ui/advanced_search_component.ui
        """
        super(AdvancedSearchWidget, self).__init__(parent)
        uic.loadUi('ui/advanced_search_component.ui', self)
        self.parent = parent
        self.search_thread = None
        self.handle_buttons(parent)
        self.handle_checkboxes()

    def handle_buttons(self, parent):
        """
        Handle all buttons action events.
        :param parent: - parent window
        """
        self.homeButton.clicked.connect(parent.start_scan_view)
        self.scanButton.clicked.connect(self.handle_scan_click)

    def handle_scan_click(self):
        label = QLabel(self)
        label.setText("SEARCHING")
        self.setDisabled(True)

        label_width = 500
        label_height = 100
        label_x_pos = self.size().width() // 2 - label_width // 2
        label_y_pos = self.size().height() // 2 - label_height // 2

        movie = QMovie("ajax-loader.gif")
        label.setGeometry(label_x_pos, label_y_pos, label_width, label_height)
        label.setFrameStyle(Qt.FramelessWindowHint)
        label.setMovie(movie)
        label.show()
        movie.setScaledSize(label.size())
        movie.start()

        self.extract_data_from_fields()

    def extract_data_from_fields(self):
        """
        Extract data from elements in component
        """
        creation_date_from = self.createdFromDate.dateTime() \
            .toString(self.createdFromDate.displayFormat())
        creation_date_to = self.createdToDate.dateTime() \
            .toString(self.createdToDate.displayFormat())
        file_size_from = self.fileSizeFromSpinBox.value()
        file_size_to = self.fileSizeToSpinBox.value()
        parent_path = self.parentPathTextInput.toPlainText()
        extensions = self.extensionsTextInput.toPlainText()

        if not self.creationDateCheckbox.isChecked():
            size_range = [file_size_from, file_size_to]
            if file_size_from > file_size_to:
                raise ValueError('Incorrect file size range')
        else:
            size_range = None

        if not self.creationDateCheckbox.isChecked():
            date_range = [creation_date_from, creation_date_to]
            if creation_date_from > creation_date_to:
                raise ValueError('Incorrect data range')
        else:
            date_range = None

        if self.parentPathCheckbox.isChecked():
            parent_path = None

        if self.extensionsCheckbox.isChecked():
            extensions = None

        self.search_thread = AdvancedSearchThread(
            parent=self.parent,
            path=parent_path,
            date_range=date_range,
            size_range=size_range,
            extensions=extensions
        )
        self.sig.connect(self.search_thread.on_event)
        self.sig.emit("search")
        self.search_thread.start()
        self.search_thread.sig1.connect(self.handle_processed_paths)

    def handle_processed_paths(self):
        self.search_thread.exit(1)
        self.parent.start_results_advanced_search_view()

    def handle_checkboxes(self):
        """
        Handle all checkboxes state change.
        """
        self.parentPathCheckbox.stateChanged.connect(
            lambda: self.state_changed(
                self.parentPathCheckbox,
                self.parentPathTextInput)
        )
        self.extensionsCheckbox.stateChanged.connect(
            lambda: self.state_changed(
                self.extensionsCheckbox,
                self.extensionsTextInput)
        )
        self.fileSizeCheckbox.stateChanged.connect(
            lambda: self.state_changed(
                self.fileSizeCheckbox,
                self.fileSizeFromSpinBox,
                self.fileSizeToSpinBox
            )
        )
        self.creationDateCheckbox.stateChanged.connect(
            lambda: self.state_changed(
                self.creationDateCheckbox,
                self.createdFromDate,
                self.createdToDate
            )
        )

        self.parentPathCheckbox.setChecked(1)
        self.extensionsCheckbox.setChecked(1)
        self.fileSizeCheckbox.setChecked(1)
        self.creationDateCheckbox.setChecked(1)

    @staticmethod
    def state_changed(checkbox, *elements):
        """
        Handle checkbox tick connected with fields given in :param elements:.
        :param checkbox: - checkbox for which state is checked
        :param elements: - elements managed by checkbox
        """
        status = checkbox.isChecked()
        for elem in list(elements):
            elem.setDisabled(status)
