from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class AdvancedSearchWidget(QWidget):
    """
    Widget class with advanced search view.
    """

    def __init__(self, parent=None):
        """"
        Init method.
        Loads view defined in ui/advanced_search_component.ui
        """
        super(AdvancedSearchWidget, self).__init__(parent)
        uic.loadUi('ui/advanced_search_component.ui', self)
        self.handle_buttons(parent)
        self.handle_checkboxes()

    def handle_buttons(self, parent):
        """
        Handle all buttons action events.
        :param parent: - parent window
        """
        self.homeButton.clicked.connect(parent.start_scan_view)
        self.scanButton.clicked.connect(parent.start_results_advanced_search_view)

    def extract_data_from_fields(self):
        """
        Extract data from elements in component
        """
        creation_date_from = self.createdFromDate.dateTime()\
            .toString(self.createdFromDate.displayFormat())
        creation_date_to = self.createdToDate.dateTime()\
            .toString(self.createdToDate.displayFormat())
        file_size_from = self.fileSizeFromSpinBox.value()
        file_size_to = self.fileSizeToSpinBox.value()
        parent_path = self.parentPathTextInput.toPlainText()
        extensions = self.extensionsTextInput.toPlainText()

        print("date from: " + str(creation_date_from))
        print("date to: " + str(creation_date_to))
        print("file size from: " + str(file_size_from))
        print("file size to: " + str(file_size_to))
        print("parent path: " + str(parent_path))
        print("extensions: " + str(extensions))

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
