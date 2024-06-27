import json

import aiofiles
from fastapi import APIRouter

from pizzas.schemas import PizzaSchema

pizzas_router = APIRouter(prefix="/pizzas", tags=["pizzas"])


@pizzas_router.get("/", response_model=list[PizzaSchema])
async def get_pizzas():
    async with aiofiles.open("pizzas/pizzas.json", "r") as f:
        body = await f.read()
        body_list = json.loads(body)
        return [PizzaSchema.model_validate(item) for item in body_list]
