class BodyNullException(Exception):
    def __init__(self):
        self._message = "A entrada dessa lambda deve ser um JSON com a propriedade `samples` sendo um array de números!"
        super().__init__(self._message)
    def getMessage(self):
        return self._message