#Structure of Qt5 GUIs

#Imports
import sys
from PyQt5.QtWidgets import QApplication, QWidget

#Create Application
app = QApplication(sys.argv)


#Create Window
win = QWidget()

#Add widgets and change properties
win.setWindowTitle('PyQt5 GUI')

#show the constructed Qt window
win.show()

# execute the application
sys.exit(app.exec_())
