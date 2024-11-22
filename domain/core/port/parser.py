from abc import ABC, abstractmethod
from ..model.query import Query


class Parser(ABC):
    @abstractmethod
    def parse(self, query: Query) -> str:
        """ Parse given query """
        raise NotImplemented()
