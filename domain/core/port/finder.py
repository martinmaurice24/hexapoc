from abc import ABC, abstractmethod
from ..model.result import Result


class Finder(ABC):
    @abstractmethod
    def search(self, query: str) -> Result:
        """ Search result for given query """
        raise NotImplemented()
