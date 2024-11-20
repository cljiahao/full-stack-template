from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import Depends, Path
from fastapi import APIRouter

from apis.v1.components.example import component_example
from apis.v1.helpers.HTTPExceptions import handle_exceptions
from db.session import get_db
from apis.v1.schemas.base import Example

router = APIRouter()


@router.get(
    "/{example}",
    response_model=Example,
    summary="Return Example based on example provided",
)
def get_example(
    example: Annotated[str, Path(description="Example", pattern="[a-zA-Z0-9]{7}")],
    db: Annotated[Session, Depends(get_db)],
):
    try:
        return_example = component_example(example, db)
        return return_example
    except Exception as e:
        handle_exceptions(e)
