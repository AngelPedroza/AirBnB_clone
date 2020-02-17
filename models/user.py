#!/usr/bin/python3
"""User Module"""
from models.base_model import BaseModel


class User(BaseModel):
    """Save me the information about the user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
