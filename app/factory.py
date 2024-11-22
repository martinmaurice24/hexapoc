from functools import cached_property
from domain.usecase.search import SearchUsecase
from adapter.google_search import GoogleSearch, GoogleQueryParser


class UsecaseFactory:
    def __new__(cls):
        """ creates a singleton object, if it is not created,
            or else returns the previous singleton object"""
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    @cached_property
    def search_usecase(self) -> SearchUsecase:
        return SearchUsecase(
            query_parser=GoogleQueryParser(),
            result_finder=GoogleSearch()
        )
