#!/usr/bin/python3
"""BaseModel Class"""
import uuid
from datetime import datetime

class BaseModel:
    id = str(uuid.uuid4())
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
