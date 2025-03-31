import sys
from PySide6.QtWidgets import QApplication
from models.main_model import MainModel
from controllers.main_controller import MainController
from views.main_window import MainWindow
# pyuic6 main_window.ui -o ui_main_window.py        

class App(QApplication):
    def __init__(self, sys_argv):
        super().__init__(sys_argv)
        
        # Инициализация MVC
        self.model = MainModel()
        self.controller = MainController(self.model)
        self.view = MainWindow()
        
        # Подключение сигналов
        self.view.connect_signals(self.controller)
        
        # Пример подписки на изменения модели
        self.model.data_updated.connect(self.on_data_updated)
        
        self.view.show()
        
    def on_data_updated(self, data):
        """Пример обработчика обновления данных"""
        print(f"Data updated: {data}")
        # self.view.ui.some_label.setText(data)


if __name__ == "__main__":
    app = App(sys.argv)
    sys.exit(app.exec())