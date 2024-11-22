from ..finder import Finder
from ...model.result import Result
from ...exception.errors import FinderException


class FinderStub(Finder):
    def __init__(self, return_value: Result = None, raise_finder_exception: bool = False):
        self.raise_finder_exception = raise_finder_exception
        self.return_value = return_value

    def search(self, query: str) -> Result:
        if self.raise_finder_exception:
            raise FinderException("Finder failed!")

        return self.return_value
