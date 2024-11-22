import pytest
from unittest.mock import MagicMock
from ..usecase.search import SearchUsecase
from ..core.port.test_double.finder_stub import FinderStub
from ..core.port.test_double.parser_stub import ParserStub
from ..core.exception.errors import FinderException, ParserException
from ..core.model.query import Query, QueryType
from ..core.model.result import Result, Match


class TestSearchUsecase:
    def test_search_when_finder_raise(self):
        usecase = SearchUsecase(
            query_parser=ParserStub(return_value="toto"),
            result_finder=FinderStub(raise_finder_exception=True)
        )

        with pytest.raises(FinderException, match="Something went .* finding .* toto"):
            usecase.search(query=Query(value="test", type=QueryType.MATCH_EXACT))

    def test_search_when_parser_raise(self):
        usecase = SearchUsecase(
            query_parser=ParserStub(raise_parse_exception=True),
            result_finder=MagicMock()
        )

        with pytest.raises(ParserException, match="Something went .* parsing .* test"):
            usecase.search(query=Query(value="test", type=QueryType.MATCH_EXACT))

    def test_search_when_succeed(self):
        expected_result = Result(
            count=5,
            best_match=Match(summary="test of new software at NASA", link="http://link1.com"),
            top_3_matches=[
                Match(summary="test of new software at NASA", link="http://link1.com"),
                Match(summary="test of new software at TNL", link="http://link2.com"),
                Match(summary="test of new software at WKM", link="http://link3.com"),
            ]
        )

        usecase = SearchUsecase(
            query_parser=ParserStub(return_value="test"),
            result_finder=FinderStub(return_value=expected_result)
        )

        assert usecase.search(query=Query(value="test", type=QueryType.MATCH_EXACT)) == expected_result
