import math
from typing import List, Any, Dict
class DistruibuitionProcessService:
    def __init__(self, samples: List[int]):
        print(f"[DistruibuitionProcessService.__init__]: Iniciando classe com amostra {samples}")
        samples.sort()
        self._samples = samples

    def _getNumbersOfClass(self, n: int) -> int:
        print(f"[DistruibuitionProcessService.getNumbersOfClass]: Obtendo números de classe da amostra")
        classes = 1 + 3.3 * math.log10(n)
        result = math.ceil(classes)
        print(f"[DistruibuitionProcessService.getNumbersOfClass]: Quantidade de classes da amostra: {result}")
        return result

    def _getAmplitude(self, num_of_classes: int) -> int:
        print(f"[DistruibuitionProcessService.getAmplitude]: Obtendo amplitude da amostra")
        min_value = self._samples[0]
        max_value = self._samples[len(self._samples) - 1]

        result = math.floor((max_value - min_value) / num_of_classes)
        print(f"[DistruibuitionProcessService.getAmplitude]: Esta é a amplitude da amostra: {result}")

        return result

    def calculate(self) -> List[Dict[str, Any]]:
        print(f"[DistruibuitionProcessService.calculate]: Realizando cálculo da tabela de distribuição")

        nums_set = list(set(self._samples))
        print(f"[DistruibuitionProcessService.calculate]: Esses são todos os números contidos na amostra: {nums_set}")

        length_of_samples = len(self._samples)
        print(f"[DistruibuitionProcessService.calculate]: Este é o tamanho da amostra: {length_of_samples}")


        classes = self._getNumbersOfClass(length_of_samples)
        ai = self._getAmplitude(num_of_classes=classes)
        table = []

        i, last_index = 0, 0
        last_num = nums_set[len(nums_set) - 1]
        interval = [nums_set[i], nums_set[i] + ai]
        print(f"[DistruibuitionProcessService.calculate]: Percorrendo as classes para ir gerando a tabela")
        while interval[0] <= last_num:
            body = {
                "i": i + 1,
                "class": f"{interval[0]} -> {interval[1]}"
            }
            print(f"[DistruibuitionProcessService.calculate]: i: {body['i']}")
            print(f"[DistruibuitionProcessService.calculate]: classe: {body['class']}")

            count = 0
            for index in range(last_index, len(self._samples)):
                if interval[0] <= self._samples[index] < interval[1]:
                    count += 1
                else:
                    last_index = index
                    break

            body["fi"] = count
            print(f"[DistruibuitionProcessService.calculate]: Total de itens dentro desse intervalo: {count}")

            if len(table) == 0:
                body["Fi"] = count
            else :
                body["Fi"] = table[i - 1]["Fi"] + count

            print(f"[DistruibuitionProcessService.calculate]: Frequência acumulada absoluta: {body['Fi']}")

            body["xi"] = (interval[0] + interval[1]) / 2
            print(f"[DistruibuitionProcessService.calculate]: Ponto médio: {body['xi']}")

            body["fri"] = round(body["fi"] / length_of_samples, 4)
            print(f"[DistruibuitionProcessService.calculate]: Frequência Relativa: {body['fri']}")

            body["pi"] = round(body["fri"] * 100, 4)
            print(f"[DistruibuitionProcessService.calculate]: Frequência Percentual: {body['pi']}%")

            table.append(body)
            i+=1

            interval = [interval[1], interval[1] + ai]

        return table