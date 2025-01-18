from typing import List
from pydantic.v1 import BaseModel


class Directory(BaseModel):
    name: str
    files: List[str]
    directories: List["Directory"]
