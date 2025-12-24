class InputValidationException(Exception):
    def __init__(self):
        self._message = "A entrada de dados da lambda deve ser uma lista de números!"
        super().__init__(self._message)
    def getMessage(self):
        return self._message