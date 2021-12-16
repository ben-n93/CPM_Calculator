#Created by ben-n93
#16.12.21

#Import re module and PyQt5 QtWidgets
import re
from PyQt5.QtWidgets import *

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

#Text labels/QLabels
impressions_label = QLabel('Impressions:')
CPM_label = QLabel('CPM:')
budget_label = QLabel('Budget:')

#List of text labels
labels = [impressions_label,CPM_label,budget_label]

#Text fields/QLineEdits
impressions_field = QLineEdit()
CPM_field = QLineEdit('$')
budget_field = QLineEdit('$')

#List of field labels
fields = [impressions_field,CPM_field,budget_field]

#List of text labels and fields
labels_fields = [impressions_label, impressions_field,CPM_label, CPM_field,budget_label,budget_field]

#Sets the window layout
window.setLayout(layout)

#Fixes the height and width of the window
window.setMinimumHeight(250)
window.setMinimumWidth(250)
window.setMaximumHeight(250)
window.setMaximumWidth(250)

#Sets the window title
window.setWindowTitle('CPM Calculator')

#Adds QLineEdits and QLabels to layout/window
for label_field in labels_fields:
    layout.addWidget(label_field)

#Adds buttons to window
layout.addWidget(calculate_button)
layout.addWidget(reset_button)

#Displays the window
window.show()

#Functions

def remove_symbols():
    """Removes non-alphanumerical characters/symbols (excluding dot) from user input using sub fct from re module"""
    dot = "."
    
    global temp_impressions_field_value
    temp_impressions_field_value = impressions_field.text()
    global temp_impressions_field_value_2
    temp_impressions_field_value_2 = re.sub(r'[^\w'+dot+']', '',temp_impressions_field_value)
    impressions_field.setText(temp_impressions_field_value_2)

    global temp_budget_field_value
    temp_budget_field_value = budget_field.text()
    global temp_budget_field_value_2
    temp_budget_field_value_2 = re.sub(r'[^\w'+dot+']', '', temp_budget_field_value)
    budget_field.setText(temp_budget_field_value_2)

    global temp_cpm_field_value
    temp_cpm_field_value = CPM_field.text()
    global temp_cpm_field_value_2
    temp_cpm_field_value_2 = re.sub(r'[^\w'+dot+']', '', temp_cpm_field_value)
    CPM_field.setText(temp_cpm_field_value_2)

def add_dollar_symbol():
    """Resets field values to original value before symbol removal"""
    impressions_field.setText(temp_impressions_field_value)
    budget_field.setText(temp_budget_field_value)    
    CPM_field.setText(temp_cpm_field_value)

def field_check_fct():
    """Checks to see if all fields have a value, in which case error window/message appears"""
    field_value_count = 0

    #Call the remove_symbols() fct in order to ensure dollar sign isn't seen as a value
    remove_symbols()

    #For every field that has a value, field_value_count will increase. 
    for field in fields:
        if field.text():
            field_value_count = field_value_count + 1
        else:
            pass

    #If all fields have a value, in which case field_value_count is 3, then an error message appears,
    #asking the user to ensure only 2 fields have a value.
    if field_value_count == 3:
        alert.setText("Error - all fields have a value.  Please ensure only two fields have a value. ")
        alert.exec()
    else:
        pass

    #Sets field values with original field values before dollar symbol removal.
    add_dollar_symbol()
    
def calculate_button_clicked():
    """Calculates CPM, budget or impressions, depending on which fields have a value."""

    #First calls the field_check_fct to double check if all fields have a value - in which case, an error msg appears.
    field_check_fct()

    #If field check has passed, removes non alphanumerical characters and converts entered fields into a floating-point number.
    remove_symbols()

    #Converts QLineEdit text values to float
    if impressions_field.text():
        impressions_calculation_value = float(impressions_field.text())
        
    if CPM_field.text():
        CPM_calculation_value = float(CPM_field.text())

    if budget_field.text():
        budget_calculation_value = float(budget_field.text())

    #If no fields have a value, nothing happens other than a dollar symbol added to budget and CPM fields.
    if not budget_field.text() and not CPM_field.text() and not impressions_field.text():
        CPM_field.setText('$')
        budget_field.setText('$')

    #Budget calculation    
    elif impressions_field.text() and CPM_field.text():
        calculation = (impressions_calculation_value / 1000) * CPM_calculation_value
        calculation = float(calculation)
        #Converts calculation to string, in order to pass to QLineEdit text property                  
        calculation = str(calculation)
        calculation = '$' + calculation
        budget_field.setText(calculation)
        #Add dollar symbol to CPM field
        temp_value = '$' + CPM_field.text()
        CPM_field.setText(temp_value)

    #Impressions calculation
    elif budget_field.text() and CPM_field.text():
        calculation = (budget_calculation_value / CPM_calculation_value) * 1000
        calculation = float(calculation)
        #Converts calculation to string, in order to pass to QLineEdit text property                  
        calculation = str(calculation)
        impressions_field.setText(calculation)

    #CPM calculation
    elif budget_field.text() and impressions_field.text():
        calculation = 1000 * (budget_calculation_value / impressions_calculation_value)
        calculation = float(calculation)
        #Converts calculation to string, in order to pass to QLineEdit text property
        calculation = str(calculation)
        #Adds dollar symbol to QLineEdit text field
        calculation = '$' + calculation
        CPM_field.setText(calculation)
        #Add dollar symbol to budget field
        temp_value = '$' + budget_field.text()
        budget_field.setText(temp_value)

    #If only one field has a value, nothing happens other than a dollar symbol added to budget and CPM fields.
    else:
        temp_value = '$' + CPM_field.text()
        CPM_field.setText(temp_value)
        temp_value = '$' + budget_field.text()
        budget_field.setText(temp_value)

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
