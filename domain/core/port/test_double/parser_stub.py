from ..parser import Parser
from ...model.query import Query
from ...exception.errors import ParserException


class ParserStub(Parser):
    def __init__(self, return_value: str = None, raise_parse_exception: bool = False):
        self.raise_parser_exception = raise_parse_exception
        self.return_value = return_value

    def parse(self, query: Query) -> str:
        if self.raise_parser_exception:
            raise ParserException(description="Parser failed!")

        return self.return_value
