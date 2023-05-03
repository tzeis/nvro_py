import sys
import time
import numpy as np

from PySide6 import QtWidgets as qtw

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
#Vereinfachte Einstellungen für Realtime-Plot
import matplotlib.style as mplstyle
mplstyle.use('fast')

class MplWidget(qtw.QWidget):
    def __init__(self,parent=None):
        super(MplWidget,self).__init__(parent)
        self.fig = plt.figure(figsize=(5,5))
        self.canvas = FigureCanvas(self.fig)
        self.toolbar = NavigationToolbar(self.canvas,self)
        
        layout = qtw.QVBoxLayout()


        self.ax = self.fig.add_subplot(111)
        #Initializes two lists of length xrange
        self.xrange = 10000
        self.x = list(range(0,self.xrange))
        self.y = list(np.repeat(0,self.xrange))
        #Initialize arbitrary units
        self.xunit = "arb.u."
        self.yunit = "arb.u"
        
        self.refresh()
        
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)

        self.setLayout(layout)

    #refesh canvas
    def refresh(self):
        #self.ax.clear()
        plt.cla()
        #self.ax.set_ylim([-1,3])
        self.ax.plot(self.x,self.y)
        self.change_units(self.xunit,self.yunit)
        self.canvas.draw()  

    #Remaps last dur values of x to y = val and refreshes canvas
    def push_new_value(self,val,dur):
        newy = list(np.repeat(val,dur))
        tmpy = self.y+newy
        self.y = tmpy[dur:self.xrange+dur]
        self.refresh()

    #Change axis units
    def change_units(self,xunit,yunit):
        #Stores inputs locally
        self.xunit = xunit
        self.yunit = yunit
        self.ax.set_xlabel("Time["+self.xunit+"]")
        self.ax.set_ylabel("Amplitude["+self.yunit+"]")

