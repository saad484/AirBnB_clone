#!/usr/bin/python3
"""
Defines the City class that inherit from BaseModel .
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent a city.

    Attributes:
        state_id (str): The state id.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""
