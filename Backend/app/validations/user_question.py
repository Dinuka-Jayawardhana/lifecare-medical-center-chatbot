from pydantic import BaseModel, field_validator

class UserQuestionModel(BaseModel):
    question: str

    @field_validator("question")
    def clean_question(cls, q: str) -> str:
        q = q.strip()
        if not q:
            raise ValueError("Question cannot be empty")
        if len(q) < 2:
            raise ValueError("Question is too short")
        return q