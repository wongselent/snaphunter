#=========================================================
# Header File
#=========================================================
""" 
SNAPHUNTER TOOL
header file
"""

# define authorship information
__authors__     = ['David Wong']
__author__      = ','.join(__authors__)
__credits__     = []
__copyright__   = 'Copyright (c) 2018'
__license__     = 'GPL'

# maintanence information
__maintainer__  = 'David Wong'
__email__       = 'david.agung.satrio@gmail.com'

#=========================================================
# Configuration
#=========================================================
import sys
from PyQt5 import QtGui
from PyQt5 import QtWidgets

#=========================================================
# Main Script
#=========================================================
def main(argv = None):

    app = None

    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(argv)
        app.setStyle('plastique')

    #QtWidgets.QMessageBox.information(None, 'Stub', 'Create the Main Window!')
    # create the main window
    from gui.snaphunterwindow import SnaphunterWindow
    window = SnaphunterWindow()
    window.show()

    if app:
        return app.exec_()

    # return 0



if __name__ == '__main__':
    sys.exit(main(sys.argv))
