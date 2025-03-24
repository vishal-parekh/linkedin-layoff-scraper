from pydantic import BaseModel
from typing import List


class LinkedInUrls(BaseModel):
    """Model for storing LinkedIn profile URLs."""

    urls: List[str]
