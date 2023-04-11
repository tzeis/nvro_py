import sys

from PySide6 import QtWidgets as qtw

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

class MplWidget(qtw.QWidget):
    def __init__(self,parent=None):
        super(MplWidget,self).__init__(parent)
        self.fig = plt.figure(figsize=(5,5))
        self.canvas = FigureCanvas(self.fig)
        self.toolbar = NavigationToolbar(self.canvas,self)
        
        layout = qtw.QVBoxLayout()
        
        self.plot()
        
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)

        self.setLayout(layout)

    def plot(self):
        x = range(0,10)
        y = range(0,20,2)
        ax = self.fig.add_subplot(111)
        ax.plot(x, y)
        self.canvas.draw()
        

