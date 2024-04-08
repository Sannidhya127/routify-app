from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
import sys

class TableWidget(QWidget):
    def __init__(self, table_data, parent=None):
        super(TableWidget, self).__init__(parent)
        self.table_data = table_data
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.table = QTableWidget()
        self.table.setRowCount(len(self.table_data))
        self.table.setColumnCount(len(self.table_data[0]))

        for i, row in enumerate(self.table_data):
            for j, cell in enumerate(row):
                self.table.setItem(i, j, QTableWidgetItem(str(cell)))

        self.layout.addWidget(self.table)
        self.setLayout(self.layout)

table_data = [["Sun",696000,1989100000],["Earth",6371,5973.6],["Moon",1737,73.5],["Mars",3390,641.85]]
app = QApplication(sys.argv)
table_widget = TableWidget(table_data)
table_widget.show()
sys.exit(app.exec_())