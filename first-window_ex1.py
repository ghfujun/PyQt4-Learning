from PyQt4 import QtGui 
import sys
# in the above steps we import the required
app_obj  = QtGui.QApplication(sys.argv)	# here we create a application object for our pgm
window = QtGui.QWidget()
# here we create a  empty window using QtGui.QWidget()
window.setWindowTitle("Sample window")
#here we set the window title
window.show()
# to display our window 
sys.exit(app_obj.exec_())
#here we 
