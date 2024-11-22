from ..core.port.finder import Finder
from ..core.port.parser import Parser
from ..core.model.query import Query
from ..core.model.result import Result
from ..core.exception.errors import FinderException, ParserException


class SearchUsecase:
    def __init__(self, query_parser: Parser, result_finder: Finder):
        self._query_parser = query_parser
        self._result_finder = result_finder

    def search(self, query: Query) -> Result:
        try:
            query_str = self._query_parser.parse(query=query)
        except ParserException as e:
            raise ParserException(description=f"Something went wrong when parsing the query {query.value}") from e

        try:
            result = self._result_finder.search(query=query_str)
        except FinderException as e:
            raise FinderException(description=f"Something went wrong when finding the query {query_str}") from e

        return result
