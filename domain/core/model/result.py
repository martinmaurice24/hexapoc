from pydantic import BaseModel


class Match(BaseModel):
    summary: str
    link: str


class Result(BaseModel):
    count: int
    best_match: Match
    top_3_matches: list[Match]

    def found(self) -> bool:
        return self.count > 0

