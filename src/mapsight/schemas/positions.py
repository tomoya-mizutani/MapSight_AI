from __future__ import annotations
from pydantic import BaseModel
from pydantic import Field
from typing import Optional

class PlayerPosition(BaseModel):
    match_id: str
    map_name: str
    map_round: str
    frame_index: int = Field(ge=1)
    ts_ms: int = Field(ge=0)
    image_path: str
    team_id: str
    player_slot: str
    player_uid: str
    status: str = Field(pattern=r"^(alive|downed|eliminated|unknown)$")

    px_x: Optional[float] = None
    px_y: Optional[float] = None
    x_norm: Optional[float] = None
    y_norm: Optional[float] = None
    confidence: Optional[float] = None

    calib_id: Optional[str] = None
    notes: Optional[str] = None

    class Config:
        frozen = False
        validate_assignment = True