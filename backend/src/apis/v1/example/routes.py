from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import Depends, Path
from fastapi import APIRouter

from apis.v1.helpers.HTTPExceptions import handle_exceptions
from apis.v1.schemas import Module
from db.repository.example import ExampleRepository
from db.repository.parent_example import ParentExampleRepository
from db.session import get_db
from core.logging import logger
from core.directory import directory

router = APIRouter()


@router.get(
    "/{example}",
    response_model="",
    summary="Return example stored in database.",
)
def get_processed_count(
    example: Annotated[
        str, Path(description="Example Text", pattern="[a-zA-Z0-9]{10}")
    ],
    db: Annotated[Session, Depends(get_db)],
):

    try:
        example_repository = ExampleRepository(db)
        parent_example_repository = ParentExampleRepository(db)
        return ""
    except Exception as e:
        handle_exceptions(e)


# @router.post(
#     "/example",
#     response_model="",
#     summary="Return example stored in database.",
# )
# def get_processed_count(
#     example: Annotated[
#         list[str], Path(description="Example Text", pattern="[a-zA-Z0-9]{10}")
#     ],
#     db: Annotated[Session, Depends(get_db)],
# ):

#     try:
#         example_repository = ExampleRepository(db)
#         parent_example_repository = ParentExampleRepository(db)
#         return ""
#     except Exception as e:
#         handle_exceptions(e)
