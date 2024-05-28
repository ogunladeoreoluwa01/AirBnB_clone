#!/usr/bin/python3
"""
BaseModel Class

This file contains the BaseModel class, which serves as the base class
for all other classes in the project.
"""

from datetime import datetime
import uuid


class BaseModel:
    """
    BaseModel class for representing base model functionality.

    Attributes:
        id (str): The ID of the model.
        created_at (datetime): The creation datetime of the model.
        updated_at (datetime): The update datetime of the model.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the BaseModel class.

        If no kwargs are provided, it creates a new instance with a new ID,
        creation datetime, and update datetime. If kwargs are provided, it
        initializes the instance with the provided data.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            formats = "%Y-%m-%dT%H:%M:%S.%f"
            kwargs['created_at'] = datetime.strptime(
                kwargs['created_at'], formats)
            kwargs['updated_at'] = datetime.strptime(
                kwargs['updated_at'], formats)
            if '__class__' in kwargs.keys():
                del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """
        Override the __str__ method to print a string representation of the class.

        Returns:
            str: A string representation of the class.
        """
        st = f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        return st

    def to_dict(self):
        """
        Convert the object into a dictionary representation.

        Returns:
            dict: A dictionary representation of the object.
        """
        my_obj_dict = {}
        my_obj_dict.update(self.__dict__)
        my_obj_dict.update({"__class__": self.__class__.__name__})
        my_obj_dict['created_at'] = self.created_at.isoformat()
        my_obj_dict['updated_at'] = self.updated_at.isoformat()
        return my_obj_dict

    def save(self):
        """
        Save the instance to the storage file.
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()
