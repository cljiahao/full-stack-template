from sqlalchemy.orm import Session

from db.CRUD.example import create_example
from db.models.example import EXAMPLE
from utils.debug import time_print
from core.logging import logger
from utils.example.example import run_example


def component_example(example: str, db: Session) -> dict[str]:
    """
    Main function to run example.

    Parameters:
    - example: An string length 7 example

    Returns:
    - An example string that is of length 7
    """

    start, stdout = time_print(f"Start of Example")
    logger.info(stdout)

    example = run_example(example)

    lap, stdout = time_print("Processing Example", start)
    logger.info(stdout)

    example_dict = {"example": example}
    create_example(EXAMPLE, db, example_dict)

    lap, stdout = time_print("Add Example into DB", lap)
    logger.info(stdout)
    _, stdout = time_print(lap=start, end=True)
    logger.info(stdout)

    return example_dict
