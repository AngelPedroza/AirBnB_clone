#!/usr/bin/python3
"""City Module"""
from models.base_model import BaseModel


class City(BaseModel):
    """The city of the place"""
    state_id = ""  # Could be state.id format
    name = ""
