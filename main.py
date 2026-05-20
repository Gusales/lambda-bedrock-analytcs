import json
import logging
import sys

from http import HTTPStatus

from firebase_functions import https_fn
from flask import make_response

from errors.body_null_exception import BodyNullException
from errors.input_validation_exception import InputValidationException
from validators.validate_input_pipe import ValidateInputPipe

from controllers.lambda_controller import Controller

logging.basicConfig(
    level=logging.INFO,
    stream=sys.stdout,
    format="%(asctime)s [%(name)s] %(levelname)s - %(message)s"
)


logger = logging.getLogger("[Lambda Bedrock Analytcs]")
logger.setLevel(logging.INFO)

@https_fn.on_request()
def lambda_handler(request: https_fn.Request) -> https_fn.Response:
    logger.info(f"Request recebida:\n{request}")
    logger.info(f"Headers:\n{request.headers}")

    try:
        samples_dto = ValidateInputPipe(
            event=request.get_json(),
            logger=logger
        )
        samples = samples_dto.validate()

        controller = Controller()
        results = controller.get(samples)

        response = make_response(
            json.dumps({"data": results}),
            HTTPStatus.OK,
        )

    except (BodyNullException, InputValidationException) as e:
        response = make_response(
            json.dumps({"message": e.getMessage()}),
            HTTPStatus.BAD_REQUEST,
        )

    response.headers["Content-Type"] = "application/json"
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"

    return response