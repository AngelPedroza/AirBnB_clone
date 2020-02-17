#!/usr/bin/python3
"""Review Module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """The class to save the reviews"""
    place_id = ""  # Place.id format
    user_id = ""  # User.id format
    text = ""
