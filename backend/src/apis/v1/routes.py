from enum import Enum
from fastapi import APIRouter

from apis.v1.example import routes as example

class APITag(str, Enum):
    """Enum to define API tags for better organization and documentation."""

    EXAMPLE = "example"


router = APIRouter()

router.include_router(example.router, tags=[APITag.EXAMPLE], prefix="/example")
