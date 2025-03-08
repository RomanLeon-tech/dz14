class LoggerMixin:
    """
    Миксин для логирования создания объектов.
    """
    def __init__(self, *args, **kwargs):
        print(f"Создан объект {self.__class__.__name__}"
              f" с параметрами: {args}, {kwargs}")
        super().__init__(*args, **kwargs)
