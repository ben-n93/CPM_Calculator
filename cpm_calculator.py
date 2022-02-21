import re

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QMessageBox,
    QPushButton)


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('CPM Calculator')
        self.impressions_label = QLabel('Impressions:')
        self.CPM_label = QLabel('CPM:')
        self.budget_label = QLabel('Budget:')
        self.impressions_field = QLineEdit()
        self.CPM_field = QLineEdit('$')
        self.budget_field = QLineEdit('$')
        self.calculate_button = QPushButton("Calculate")
        self.reset_button = QPushButton("Reset")
        self.fields = [self.impressions_field, self.CPM_field,
                       self.budget_field]
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.impressions_label)
        self.layout.addWidget(self.impressions_field)
        self.layout.addWidget(self.CPM_label)
        self.layout.addWidget(self.CPM_field)
        self.layout.addWidget(self.budget_label)
        self.layout.addWidget(self.budget_field)
        self.layout.addWidget(self.calculate_button)
        self.layout.addWidget(self.reset_button)
        self.setLayout(self.layout)
        self.setMinimumHeight(250)
        self.setMinimumWidth(250)
        self.setMaximumHeight(250)
        self.setMaximumWidth(250)
        self.alert = QMessageBox()
        self.alert.setIcon(QMessageBox.Warning)
        self.calculate_button.clicked.connect(self.calculate_button_clicked)
        self.reset_button.clicked.connect(self.reset_button_clicked)

    def valid_input(self):
        """Check to make sure user's input is valid."""

        # Removes non-alphanumerical characters/symbols (excluding dot) from
        # field values and resets fields with formatted values.
        temp_impressions_field_value = re.sub(r'[^\w'+'.'+']', '',
                                              self.impressions_field.text())
        self.impressions_field.setText(temp_impressions_field_value)

        temp_budget_field_value = re.sub(r'[^\w'+'.'+']', '',
                                         self.budget_field.text())
        self.budget_field.setText(temp_budget_field_value)

        temp_cpm_field_value = re.sub(r'[^\w'+'.'+']', '',
                                      self.CPM_field.text())
        self.CPM_field.setText(temp_cpm_field_value)

        # Checks for text input.
        for field in self.fields:
            # If field has a value, attempts to create a float.
            if field.text():
                try:
                    value_check = float(field.text())
                # If unable to create a float (in which, user input is invalid)
                # returns False, so the calculate button does not execute
                # calculation formulas.
                except ValueError:
                    self.alert.setText("Error - please only enter numbers. ")
                    self.alert.exec()
                    # REMINDER - function ends when it returns a value, so, in
                    # the event of a field having valid input,
                    # False is returned and fct stops executing.
                    return False
                    # Loop doesn't continue if invalid user input detected -
                    # no point in checking other friends.
                    break
        # Assuming all entered fields have a valid value,
        # True is returned, so calculate button knows to execute calculation
        # formulas.
        return True

    def field_check_fct(self):
        """Check to make sure ONLY two fields have a value."""
        field_value_count = 0
        # For every field that has a value, field_value_count will increase.
        for field in self.fields:
            if field.text():
                field_value_count = field_value_count + 1
        # Returns True, so calculate button doesn't run.
        if field_value_count == 3:
            alert_text = "Error - all fields have a value.  Please ensure only"
            alert_text += " two fields have a value. "
            self.alert.setText(alert_text)
            self.alert.exec()
            self.field_value_format()
            return True
        else:
            return False

    def field_value_format(self):
        """Format the values in the QLineEdit fields and return a readable
        value."""

        # Field format count, implemented for the dollar symbol formatting
        # (see below for more details).
        field_format_count = 0
        for field in self.fields:
            field_format_count += 1
            # If the field has text, formatting commences.
            if field.text():
                # Captures fractional points/numbers.
                formatted_value = float(field.text())
                fractional_part = formatted_value % 1
                # Checks to see if fractional part is 0, in which case
                # calculated value is turned into an integer (to remove
                # unnecessary decimal point).
                if fractional_part == 0:
                    formatted_value = int(formatted_value)
                else:
                    # If the calculated value has a fractional part higher
                    # than 0, then value is rounded down to 2 decimal points,
                    # for a more readable value.
                    formatted_value = round(formatted_value, 2)
                # Adds comma for every thousand digits
                formatted_value = "{:,}".format(formatted_value)
                field.setText(formatted_value)
                # First field in this loop is impressions field, so no dollar
                # symbol is added (impressions_field is first element in fields
                # list).
                if field_format_count == 1:
                    pass
                else:
                    # If there is already a dollar symbol in budget or CPM
                    # field nothing happens.
                    if '$' in field.text():
                        pass
                    # If no dollar symbol present in budget or CPM field,
                    # one is added to start of string.
                    else:
                        temp_value = field.text()
                        field.setText('$' + temp_value)
            else:
                pass

    def calculate_button_clicked(self):
        """Calculate CPM, budget or impressions."""

        # Call to check that valid text has been input, in which case True is
        # returned.
        if self.valid_input():
            # Call to the field_check_fct to check only two fields have a
            # value.
            if self.field_check_fct() is not True:
                # Budget calculation.
                if self.impressions_field.text() and self.CPM_field.text():
                    calculation = str((float(self.impressions_field.text()) /
                                       1000) * float(self.CPM_field.text()))
                    self.budget_field.setText(calculation)
                    # Formats the value of all fields.
                    self.field_value_format()
                # Impressions calculation.
                elif self.budget_field.text() and self.CPM_field.text():
                    calculation = str((float(self.budget_field.text()) /
                                       float(self.CPM_field.text())) * 1000)
                    self.impressions_field.setText(calculation)
                    # Formats the value of all fields.
                    self.field_value_format()

                # CPM calculation
                elif self.budget_field.text() and self.impressions_field.text():
                    calculation = str(float(self.budget_field.text()) /
                                      float(self.impressions_field.text())
                                      * 1000)
                    self.CPM_field.setText(calculation)
                    # Formats the value of all fields.
                    self.field_value_format()
                # If only one field has a value or NO fields have a value,
                # nothing happens other than a dollar symbol added to budget
                # and CPM fields.
                else:
                    self.CPM_field.setText('$' + self.CPM_field.text())
                    self.budget_field.setText('$' + self.budget_field.text())
        # If user has input invalid value/s, nothing happens.
        else:
            pass

    def reset_button_clicked(self):
        """Reset calculator fields."""
        self.impressions_field.setText('')
        self.CPM_field.setText('$')
        self.budget_field.setText('$')


if __name__ == "__main__":
    app = QApplication([])
    calculator = Calculator()
    calculator.show()
    app.exec()
