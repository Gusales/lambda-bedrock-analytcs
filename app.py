import logging
import json

from http import HTTPStatus
from typing import Dict, Any
from errors.body_null_exception import BodyNullException
from errors.input_validation_exception import InputValidationException
from validators.validate_input_pipe import ValidateInputPipe

from controllers.lambda_controller import Controller

logger = logging.getLogger("[Lambda Bedrock Analytcs]")
logger.setLevel(logging.INFO)

def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    logger.info(f"Evento recebido:\n{event}")

    try:
        samples_dto = ValidateInputPipe(
            event=event,
            logger=logger
        )
        samples = samples_dto.validate()

        controller = Controller()
        results = controller.get(samples)

        return {
            "statusCode": HTTPStatus.OK,
            "body": json.dumps({
                "data": results
            })
        }
    except (BodyNullException, InputValidationException) as e:
        return {
            "statusCode": HTTPStatus.BAD_REQUEST,
            "body": json.dumps({
                "message": e.getMessage()
            })
        }