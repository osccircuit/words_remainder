from PySide6.QtCore import QObject, Signal
from models.main_model import MainModel


class MainController(QObject):
    data_changed = Signal(str)  # Пример сигнала для передачи данных
    
    def __init__(self, model: MainModel):
        super().__init__()
        self._model = model
        
    def process_data(self, data: str):
        """Пример метода обработки данных"""
        # Обработка данных
        processed_data = data.upper()
        
        # Обновление модели
        self._model.set_data(processed_data)
        
        # Отправка сигнала (если нужно)
        self.data_changed.emit(processed_data)