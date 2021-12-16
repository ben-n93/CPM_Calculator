# CPM-Calculator
Digital advertising cost per mille (CPM) calculator, created using the PyQt5 library and re module.

<img width="274" alt="CPM_Calculator_Screenshot1" src="https://user-images.githubusercontent.com/84557025/146355127-3fa0dea7-5249-4eb0-8655-5e6c92faf0c5.png">

You can calculate an impression goal, CPM or budget, depending on which two fields have been entered:

![CPM_Calculator_GIF_1](https://user-images.githubusercontent.com/84557025/146358191-fe2e406d-1afb-4a2e-ac52-b858547d7ae4.gif)

The dollar symbol is a default value in the CPM and budget fields - I thought this was a nice visual reminder of the value type that goes in these fields. Even if you hit the reset button the dollar symbol reappears.

If all 3 fields have a value, an error message pops up:

![CPM_Calculator_Error_GIF](https://user-images.githubusercontent.com/84557025/146360694-d69dd2bf-7057-45ec-be97-f5df800ac99a.gif)

For a future update I'd like to ensure that the output value is formatted in a more readable format, e.g. 50000.0 impressions becomes '50,000' impressions.
