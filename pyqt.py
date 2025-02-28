import sys
import random
from PyQt6 import QtWidgets, uic, QtGui, QtCore

class CircleWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.circles = []  

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)
        painter.setBrush(QtGui.QBrush(QtGui.QColor("yellow")))
        for circle in self.circles:
            x, y, diameter = circle
            painter.drawEllipse(x, y, diameter, diameter)

    def add_circle(self, x, y, diameter):
        self.circles.append((x, y, diameter))
        self.update() 

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        
        self.circle_widget = CircleWidget(self.centralWidget())
        self.circle_widget.setGeometry(0, 0, self.centralWidget().width(), self.centralWidget().height())
        self.circle_widget.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self.pushButton.clicked.connect(self.on_button_click)

    def on_button_click(self):
        diameter = random.randint(10, 100)
        max_x = self.circle_widget.width() - diameter
        max_y = self.circle_widget.height() - diameter
        if max_x < 0 or max_y < 0:
            return
        x = random.randint(0, max_x)
        y = random.randint(0, max_y)
        self.circle_widget.add_circle(x, y, diameter)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
