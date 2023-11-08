from typing import Optional

from pydantic import BaseModel, validator


class MeetingRoomCreate(BaseModel):
    name: str
    description: Optional[str]

    @validator('name')
    def name_cant_be_empty_and_longer_then_100_characters(cls, value: str):
        if len(value) == 0 or len(value) > 100:
            raise ValueError(
                'Строка не должна быть пустой или превышать 100 символов.')
        return value
