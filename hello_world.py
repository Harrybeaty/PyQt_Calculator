#hello.py

"""Simple Hello, World GUI"""

import sys                              # Allows us to use exit() function to terminate the application.

# 1. import QApplication and all the required widgets.
from PyQt6.QtWidgets import QApplication, QLabel, QWidget

# 2. Create an instance of QApplication class
app = QApplication([])                  # QApplication class deals with command-line arguments which are lists.

# 3. Create your application's GUI
window = QWidget()                      # Creates an instance of the QWidget class.
window.setWindowTitle("PyQT App")
window.setGeometry(100, 100, 280, 80)   # Position on the screen and size (x, y, w, h).
helloMsg = QLabel("<h1>Hello, World!</h1>", parent=window) # Creates a widget, uses HTML format. Set as parent as main window.
helloMsg.move(60, 15)                   # Places the widget at those coordinates.    

# 4. Show your application's GUI
window.show()

# 5. Run the application's event loop
sys.exit(app.exec())