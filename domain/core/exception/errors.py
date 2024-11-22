class SearchBaseException(Exception):
    def __init__(self, description: str, **extras):
        super().__init__(description)


class FinderException(SearchBaseException):
    def __init__(self, description: str, **extras):
        super().__init__(description=description, extras=extras)


class ParserException(SearchBaseException):
    def __init__(self, description: str, **extras):
        super().__init__(description=description, extras=extras)
