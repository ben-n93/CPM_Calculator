#Created by ben-n93 on 16.12.21
#github.com/ben-n93

#Import re module and PyQt5 QtWidgets
import re
from PyQt5.QtWidgets import QApplication, QWidget,QLabel,QLineEdit, QVBoxLayout, QMessageBox, QPushButton

#Instance of QApplication
app = QApplication([])

#Window and layout
window = QWidget()
layout = QVBoxLayout()

#Buttons
calculate_button = QPushButton("Calculate")
reset_button = QPushButton("Reset")

#Alert message box
alert = QMessageBox()
alert.setIcon(QMessageBox.Warning)
alert.setText("Error - all fields have a value.  Please ensure only two fields have a value. ")

#Text labels/QLabels
impressions_label = QLabel('Impressions:')
CPM_label = QLabel('CPM:')
budget_label = QLabel('Budget:')

#Text fields/QLineEdits
impressions_field = QLineEdit()
CPM_field = QLineEdit('$')
budget_field = QLineEdit('$')

#List of field labels/QLabels
fields = [impressions_field,CPM_field,budget_field]

#List of text labels/QLabels and fields/QLineEdits
labels_fields = [impressions_label, impressions_field,CPM_label, CPM_field,budget_label,budget_field]

#Sets the window layout
window.setLayout(layout)

#Fixes the height and width of the window/QWidget
window.setMinimumHeight(250)
window.setMinimumWidth(250)
window.setMaximumHeight(250)
window.setMaximumWidth(250)

#Sets the window/QWidget title
window.setWindowTitle('CPM Calculator')

#Adds fields/QLineEdits and field labels/QLabels to layout/window
for label_field in labels_fields:
    layout.addWidget(label_field)

#Adds buttons to window/QWidget
layout.addWidget(calculate_button)
layout.addWidget(reset_button)

#Displays the window/QWidget
window.show()

#Functions

def field_check_fct():
    """Checks to see if all fields have a value, in which case error message appears and True is returned"""

    #Resets field value count
    field_value_count = 0

    #Removes non-alphanumerical characters/symbols (excluding dot) from field values, using sub fct from re module, and resets fields with formatted values
    temp_impressions_field_value = re.sub(r'[^\w'+'.'+']', '',impressions_field.text())
    impressions_field.setText(temp_impressions_field_value)

    temp_budget_field_value = re.sub(r'[^\w'+'.'+']', '', budget_field.text())
    budget_field.setText(temp_budget_field_value)

    temp_cpm_field_value = re.sub(r'[^\w'+'.'+']', '', CPM_field.text())
    CPM_field.setText(temp_cpm_field_value)

    #For every field that has a value, field_value_count will increase. 
    for field in fields:
        if field.text():
            field_value_count = field_value_count + 1
    #If all fields have a value, in which case field_value_count is 3, then an error message/window appears,
    #asking the user to ensure only 2 fields have a value. Also returns True, so calculate button doesn't run.
    if field_value_count == 3:
        alert.exec()
        return True
    else:
        return False

def field_value_format(calculation):
    """Formats the values in the QLineEdit fields and returns a readable value."""
    global calculation_formatted
    calculation_formatted = float(calculation)
    #Captures fractional points/numbers
    fractional_part = calculation_formatted % 1
    #Checks to see if fractional part is 0, in which case calculated value is turned into an integer (to remove unnecessary decimal point)
    if fractional_part == 0:
        calculation_formatted = int(calculation_formatted)
    else:
        #If the calculated value has a fractional part higher than 0, then value is rounded down to 2 decimal points, for a more readable value.
        calculation_formatted = round(calculation_formatted,2)
    #Adds comma for every thousand digits
    calculation_formatted = "{:,}".format(calculation_formatted)
    return calculation_formatted
    
def calculate_button_clicked():
    """Calculates CPM, budget or impressions, depending on which fields have a value."""

    #Call to the field_check_fct to double check if all fields have a value - in which case, an error message appears and no calculation is performed (due to the return of True value)
    if field_check_fct() == False:
        #Budget calculation    
        if impressions_field.text() and CPM_field.text():
            calculation = (float(impressions_field.text()) / 1000) * float(CPM_field.text())
            field_value_format(calculation)
            budget_field.setText("$" + calculation_formatted)
            #Add dollar symbol to CPM field
            temp_value = '$' + CPM_field.text()
            CPM_field.setText(temp_value)

        #Impressions calculation
        elif budget_field.text() and CPM_field.text():
            calculation = (float(budget_field.text()) / float(CPM_field.text())) * 1000
            field_value_format(calculation)
            impressions_field.setText(calculation_formatted)
            #Add dollar symbol to budget field
            temp_value = '$' + budget_field.text()
            budget_field.setText(temp_value)
            #Add dollar symbol to CPM field
            temp_value = '$' + CPM_field.text()
            CPM_field.setText(temp_value)

        #CPM calculation
        elif budget_field.text() and impressions_field.text():
            calculation = 1000 * (float(budget_field.text()) / float(impressions_field.text()))
            field_value_format(calculation)
            CPM_field.setText("$" + calculation_formatted)
            #Add dollar symbol to budget field
            temp_value = '$' + budget_field.text()
            budget_field.setText(temp_value)

        #If only one field has a value or NO fields have a value, nothing happens other than a dollar symbol added to budget and CPM fields.
        else:
            CPM_field.setText('$' + CPM_field.text())
            budget_field.setText('$' + budget_field.text())
    else:
        #If all 3 fields have a value, the following code ensures a dollar symbol is added to budget and CPM field
        temp_value = '$' + budget_field.text()
        budget_field.setText(temp_value)
        temp_value = '$' + CPM_field.text()
        CPM_field.setText(temp_value)

def reset_button_clicked():
    """Replaces impressions field with empty text and replaces CPM and budget fields with a dollar symbol"""
    impressions_field.setText('')
    CPM_field.setText('$')
    budget_field.setText('$')

#Calculate button signal/slot
calculate_button.clicked.connect(calculate_button_clicked)

#Reset button signal/slot
reset_button.clicked.connect(reset_button_clicked)

#Exit app when user quits
app.exec()
