from PySide6.QtCore import QObject, Signal


class MainModel(QObject):
    data_updated = Signal(str)  # Сигнал об обновлении данных
    
    def __init__(self):
        super().__init__()
        self._data = ""
        
    @property
    def data(self) -> str:
        return self._data
    
    def set_data(self, value: str):
        if self._data != value:
            self._data = value
            self.data_updated.emit(value)  # Уведомляем об изменении