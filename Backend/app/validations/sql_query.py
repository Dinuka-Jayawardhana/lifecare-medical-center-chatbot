from pydantic import BaseModel, field_validator

class SQLQueryModel(BaseModel):
    query: str

    @field_validator("query")
    def validate_sql(cls, q: str) -> str:
        lowered = q.lower().strip()
        if not lowered.startswith("select"):
            raise ValueError("Only SELECT queries are allowed")
        banned_keywords = ["delete", "drop", "update", "insert", "alter", "truncate"]
        if any(bad in lowered for bad in banned_keywords):
            raise ValueError("Unsafe SQL detected")
        return q