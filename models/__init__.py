#!/usr/bin/python3
"""
Initialize Storage for Console

This script initializes the storage variable for the console.
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
