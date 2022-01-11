# Created by ben-n93 on 16.12.21.
# github.com/ben-n93.

# Import re module and PyQt5 QtWidgets.
import re

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QMessageBox,
    QPushButton)

# Instance of QApplication.
app = QApplication([])

# Window and layout.
window = QWidget()
layout = QVBoxLayout()

# Buttons.
calculate_button = QPushButton("Calculate")
reset_button = QPushButton("Reset")

# Alert message box.
alert = QMessageBox()
alert.setIcon(QMessageBox.Warning)

# Text labels/QLabels.
impressions_label = QLabel('Impressions:')
CPM_label = QLabel('CPM:')
budget_label = QLabel('Budget:')

# Text fields/QLineEdits.
impressions_field = QLineEdit()
CPM_field = QLineEdit('$')
budget_field = QLineEdit('$')

# List of field labels/QLabels.
fields = [impressions_field, CPM_field, budget_field]

# List of text labels/QLabels and fields/QLineEdits.
labels_fields = [impressions_label, impressions_field, CPM_label,
                 CPM_field, budget_label, budget_field]

# Sets the window layout.
window.setLayout(layout)

# Fixes the height and width of the window/QWidget
window.setMinimumHeight(250)
window.setMinimumWidth(250)
window.setMaximumHeight(250)
window.setMaximumWidth(250)

# Sets the window/QWidget title.
window.setWindowTitle('CPM Calculator')

# Adds fields/QLineEdits and field labels/QLabels to layout/window
for label_field in labels_fields:
    layout.addWidget(label_field)

# Adds buttons to window/QWidget.
layout.addWidget(calculate_button)
layout.addWidget(reset_button)

# Displays the window/QWidget.
window.show()


def valid_input():
    """Checks to make sure user's input is valid."""

    # Removes non-alphanumerical characters/symbols (excluding dot) from field
    # values, using sub fct from re module, and resets fields with formatted
    # values.
    temp_impressions_field_value = re.sub(r'[^\w'+'.'+']', '',
                                          impressions_field.text())
    impressions_field.setText(temp_impressions_field_value)

    temp_budget_field_value = re.sub(r'[^\w'+'.'+']', '', budget_field.text())
    budget_field.setText(temp_budget_field_value)

    temp_cpm_field_value = re.sub(r'[^\w'+'.'+']', '', CPM_field.text())
    CPM_field.setText(temp_cpm_field_value)

    # Checks for text input.
    for field in fields:
        # If field has a value, attempts to create a float.
        if field.text():
            try:
                value_check = float(field.text())
            # If unable to create a float (in which, user input is invalid),
            # returns False, so the calculate button does not execute
            # calculation formulas.
            except ValueError:
                alert.setText("Error - please only enter numbers. ")
                alert.exec()
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


def field_check_fct():
    """Checks to make sure ONLY two fields have a value."""

    # Resets field value count.
    field_value_count = 0

    # For every field that has a value, field_value_count will increase.
    for field in fields:
        if field.text():
            field_value_count = field_value_count + 1
    # If all fields have a value, in which case field_value_count is 3, then
    # an error message/window appears, asking the user to ensure only 2 fields
    # have a value. Also returns True, so calculate button doesn't run.
    if field_value_count == 3:
        alert_text = "Error - all fields have a value.  Please ensure only"
        alert_text += "two fields have a value. "
        alert.setText(alert_text)
        alert.exec()
        field_value_format()
        return True
    else:
        return False


def field_value_format():
    """Formats the values in the QLineEdit fields and returns a readable
    value."""

    # Field format count, implemented for the dollar symbol formatting
    # (see below for more details).
    field_format_count = 0
    for field in fields:
        field_format_count += 1
        # If the field has text, formatting commences.
        if field.text():
            # Captures fractional points/numbers.
            formatted_value = float(field.text())
            fractional_part = formatted_value % 1
            # Checks to see if fractional part is 0, in which case calculated
            # value is turned into an integer (to remove unnecessary decimal
            # point).
            if fractional_part == 0:
                formatted_value = int(formatted_value)
            else:
                # If the calculated value has a fractional part higher than 0,
                # then value is rounded down to 2 decimal points, for a more
                # readable value.
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
                # If there is already a dollar symbol in budget or CPM field,
                # nothing happens.
                if '$' in field.text():
                    pass
                # If no dollar symbol present in budget or CPM field, one is
                # added to start of string.
                else:
                    temp_value = field.text()
                    field.setText('$' + temp_value)
        else:
            pass


def reset_button_clicked():
    """Replaces impressions field with empty text and replaces CPM and budget
    fields with a dollar symbol."""

    impressions_field.setText('')
    CPM_field.setText('$')
    budget_field.setText('$')


def calculate_button_clicked():
    """Calculates CPM, budget or impressions, depending on which fields have a
    value."""

    # Call to check that valid text has been input, in which case True is
    # returned.
    if valid_input():
        # Call to the field_check_fct to check only two fields have a value.
        if field_check_fct() is not True:
            # Budget calculation.
            if impressions_field.text() and CPM_field.text():
                calculation = str((float(impressions_field.text()) / 1000) *
                                  float(CPM_field.text()))
                budget_field.setText(calculation)
                # Formats the value of all fields.
                field_value_format()
            # Impressions calculation.
            elif budget_field.text() and CPM_field.text():
                calculation = str((float(budget_field.text()) /
                                   float(CPM_field.text())) * 1000)
                impressions_field.setText(calculation)
                # Formats the value of all fields.
                field_value_format()

            # CPM calculation
            elif budget_field.text() and impressions_field.text():
                calculation = str(float(budget_field.text()) /
                                  float(impressions_field.text()) * 1000)
                CPM_field.setText(calculation)
                # Formats the value of all fields.
                field_value_format()
            # If only one field has a value or NO fields have a value,
            # nothing happens other than a dollar symbol added to budget and
            # CPM fields.
            else:
                CPM_field.setText('$' + CPM_field.text())
                budget_field.setText('$' + budget_field.text())
    # If user has input invalid value/s, nothing happens.
    else:
        pass


# Calculate button signal/slot.
calculate_button.clicked.connect(calculate_button_clicked)


# Reset button signal/slot.
reset_button.clicked.connect(reset_button_clicked)

# Exit app when user quits.
app.exec()
