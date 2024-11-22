import typer
import pprint
from app.application import App
from domain.core.model.query import Query, QueryType

cli = typer.Typer()


def adapt_search_input(q: str, query_type: str) -> Query:
    if query_type == 'in_url':
        return Query(value=q, type=QueryType.MATCH_IN_URL)

    if query_type == 'file_extension':
        return Query(value=q, type=QueryType.MATCH_PDF)

    raise ValueError("query_type value should be either in_url or file_extension")


@cli.command()
def search(q: str, query_type: str = 'in_url'):
    application = App()
    result = application.search(query=adapt_search_input(q=q, query_type=query_type))
    pprint.pp(result.model_dump())


if __name__ == "__main__":
    cli()
