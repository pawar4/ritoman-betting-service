# router for all endpoints that are triggered via webhooks
# see webhook-router for more details
from ritoman_betting_service.internal.database import register_bet
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(
    prefix='/listeners',
    tags=['listeners'],
    dependencies=[],
)

class Bet(BaseModel):
    game_id : int
    better_id : str
    bettee_id : str
    bet_condition : str
    bet_amount : int


@router.post('/')
async def create_bet(bet : Bet):
    #add to database
    result = register_bet(**bet.dict())
    #handle database response
    if not result:
        raise HTTPException(400)
    #send response message
    return True
