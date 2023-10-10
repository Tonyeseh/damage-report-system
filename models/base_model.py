#!/usr/bin/env python3
"""Base model"""
import datetime
import uuid

class BaseModel:
    """BaseModel from which all other models inherit"""
    def __init__(self) -> None:
        self.id = str(uuid.uuid4())
        