from typing import List, Optional

from pydantic import BaseModel


class Host(BaseModel):
    taxon_id: int
    common_name: str
    sci_name: str
    counts = int

    class Config:
        orm_mode = True



