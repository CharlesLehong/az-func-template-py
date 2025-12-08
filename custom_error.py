class CustomError(Exception):
    def __init__(self, title, message):
        super().__init__(f"{title}: {message}")
        self.title = title
        self.message = message