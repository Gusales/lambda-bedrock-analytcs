import logging
import urllib.parse
import json
from logging import Logger

from typing import List, Dict, Any
from errors.input_validation_exception import InputValidationException

class ValidateInputPipe:
    def __init__(self, logger: Logger, event: Dict[str, Any]):
        self._event = event
        if logger is None:
            self._logger = logging.getLogger("[Lambda Bedrock Analytcs]")
            self._logger.setLevel(logging.INFO)
        else:
            self._logger = logger

    def validate(self):
        self._logger.info("[ValidateInputPipe.validate] - Validando entradas da lambda")
        samples_encoded = self._event.get('queryStringParameters', {}).get('samples')
        self._logger.info(f"[ValidateInputPipe.validate] - event.queryStringParameters {samples_encoded}")
        if isinstance(samples_encoded, List):
            self._validateIsNumbers(samples_encoded)
            return samples_encoded

        elif not samples_encoded:
            raise InputValidationException()

        else:
            self._logger.info(f"[ValidateInputPipe.validate] - Decodificando a amostra vindo do evento")
            samples_decoded = urllib.parse.unquote(samples_encoded)

            dados = json.loads(samples_decoded)
            self._logger.info(f"[ValidateInputPipe.validate] - Dados decodificados:\n{dados}")
            self._validateIsNumbers(dados)
            return dados

    @staticmethod
    def  _validateIsNumbers(dados: List[int]) -> None:
        if not isinstance(dados, List):
            raise InputValidationException()
        else:
            for num in dados:
                if not isinstance(num, int):
                    raise InputValidationException()