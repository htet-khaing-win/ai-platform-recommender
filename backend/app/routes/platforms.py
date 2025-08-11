from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

class AIPlatform(BaseModel):
    id: int
    name: str
    category: str
    description: str
    pricing: str
    website: str

platforms_db = [
    AIPlatform(
        id=1,
        name="ChatGPT",
        category="LLM",
        description="Large language model by OpenAI",
        pricing="Free / Plus subscription",
        website="https://chat.openai.com/"
    ),
    AIPlatform(
        id=2,
        name="Claude",
        category="LLM",
        description="Conversational AI by Anthropic",
        pricing="Free / Pro subscription",
        website="https://claude.ai/"
    )
]

@router.get("/platforms", response_model=List[AIPlatform])
def get_platforms():
    return platforms_db