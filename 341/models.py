from datetime import datetime
from typing import Any

from passlib.context import CryptContext
from pydantic import BaseModel

# https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
# which we'll further explore in a later Bite
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return pwd_context.hash(password)


class Food(BaseModel):
    """Bite 02"""

    id: int
    name: str
    serving_size: str
    kcal_per_serving: int
    protein_grams: float
    fibre_grams: float = 0


class User(BaseModel):
    password: str
    def __init__(self, id: int, username: int, password: str):
        self.password = get_password_hash(password)


class FoodEntry(BaseModel):
    def __init__(self, id: int, user: User, food: Food, date_added: datetime, number_servings: float):
        self.id = id
        self.user = user
        self.food = food
        self.date_added = date_added
        self.number_servings = number_servings
        self.total_calories = property(self.number_servings * self.food.kcal_per_serving)

