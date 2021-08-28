# router for all endpoints that are triggered via webhooks
# see webhook-router for more details
from fastapi import APIRouter

router = APIRouter(
    prefix='/listeners',
    tags=['listeners'],
    dependencies=[],
)