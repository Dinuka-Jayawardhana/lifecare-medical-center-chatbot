from pydantic import BaseModel, field_validator
from typing import List, Dict, Any


class SQLResultModel(BaseModel):
    result: List[Dict[str, Any]]

    @field_validator("result")
    def validate_result(cls, res: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        if not isinstance(res, list):
            raise ValueError("Result must be a list")
        for row in res:
            if not isinstance(row, dict):
                raise ValueError("Each row must be a dictionary")
        return res