from pydantic import BaseModel
import enum


class QueryType(enum.IntEnum):
    MATCH_EXACT = 0
    MATCH_PDF = 1
    MATCH_IN_URL = 2


class Query(BaseModel):
    value: str
    type: QueryType

