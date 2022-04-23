from typing import Dict

from fastapi import FastAPI, Path
from pydantic import BaseModel


class Food(BaseModel):
    """Model from Bite 02"""

    id: int
    name: str
    serving_size: str
    kcal_per_serving: int
    protein_grams: float
    fibre_grams: float = 0


app = FastAPI()
foods: Dict[int, Food] = {}


@app.post("/", status_code=201)
async def create_food(food: Food):
    """Endpoint from Bite 03"""
    foods[food.id] = food
    return food


# write the two Read endpoints
@app.get("/")
async def read_foods():
    return [v for k, v in foods.items()]

@app.get("/{food_id}")
async def read_foods(food_id: int):
    return foods[food_id]