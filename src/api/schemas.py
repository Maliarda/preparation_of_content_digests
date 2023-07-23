from typing import List

from pydantic import BaseModel


class UserDigestResponse(BaseModel):
    posts: List[str]
