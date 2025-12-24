from services.distribuition_process_service import DistruibuitionProcessService
from typing import List, Any

class Controller:
    def __init__(self):
        self._distribuitionProcessService = None

    def get(self, dados: List[int]) ->  List[dict[str, Any]]:
        # dados = [2,2,3,3,3,5,5,7,8]
        self._distribuitionProcessService = DistruibuitionProcessService(dados)
        table = self._distribuitionProcessService.calculate()
        return table