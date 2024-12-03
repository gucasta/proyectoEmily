from PySide6.QtWidgets import QApplication
from frontPage import MenuBarraLateral
import sys

app = QApplication(sys.argv)

window = MenuBarraLateral()

window.show()
app.exec()