from fastapi import APIRouter

from apis.v1 import routes as v1


router = APIRouter()

router.include_router(v1.router, prefix="/v1")


@router.get("/health", tags=["health"])
def health():
    return {"status": "OK"}
