#!/usr/bin/python3
"""
State Class

This file contains the State class, which inherits from BaseModel.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    State class for representing states.

    Attributes:
        name (str): The name of the state.
    """
    name = ""
