from services.distribuition_process_service import DistruibuitionProcessService

class Controller:
    def __init__(self):
        self._distribuitionProcessService = None

    def get(self):
        dados = [
            39, 39, 39, 39, 39, 39, 39, 40, 40, 40, 40, 40, 40,
            30, 30, 30, 31, 32, 32, 32, 32, 33, 33, 34, 34, 35,
            4, 11, 12, 15, 15, 16, 20, 21, 22, 22, 23, 24, 24,
            35, 35, 36, 36, 37, 37, 37, 37, 37, 37, 37, 38, 38,
            25, 26, 26, 26, 26, 27, 27, 28, 28, 29, 29, 29, 30
        ]
        # dados = [2,2,3,3,3,5,5,7,8]
        self._distribuitionProcessService = DistruibuitionProcessService(dados)
        table = self._distribuitionProcessService.calculate()
        return table