from domain.core.model.query import Query
from domain.core.model.result import Result
from .factory import UsecaseFactory


class App:
    def __new__(cls):
        """ creates a singleton object, if it is not created,
            or else returns the previous singleton object"""
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        self._usecase = UsecaseFactory()

    def search(self, query: Query) -> Result:
        search_usecase = self._usecase.search_usecase
        return search_usecase.search(query=query)
