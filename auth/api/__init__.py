from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["Authentication"])


from . import routes