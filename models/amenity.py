#!/usr/bin/python3
"""
Amenity Class

This file contains the Amenity class, which inherits from BaseModel.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class for representing amenities.

    Attributes:
        name (str): The name of the amenity.
    """
    name = ""
