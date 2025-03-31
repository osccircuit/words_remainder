from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QFile, QIODevice
from PySide6.QtUiTools import QUiLoader
from views.ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Теперь кнопка должна быть доступна как self.ui.buttonName
        if hasattr(self.ui, "buttonName"):
            self.ui.buttonName.setStyleSheet("background-color: green;")
        
    def load_ui(self):
        """Загрузка UI из .ui файла"""
        loader = QUiLoader()
        ui_file = QFile("views/main_window.ui")
        
        if not ui_file.open(QIODevice.ReadOnly):
            print(f"Cannot open {ui_file.fileName()}: {ui_file.errorString()}")
            return
            
        self.ui = loader.load(ui_file, self)
        ui_file.close()
        
        if not self.ui:
            print(loader.errorString())
            return
            
        self.setCentralWidget(self.ui)
        self.setWindowTitle("MVC Application")
        
    def connect_signals(self, controller):
        """Подключение сигналов к контроллеру"""
        # Пример: self.ui.some_button.clicked.connect(controller.handle_button_click)
        pass