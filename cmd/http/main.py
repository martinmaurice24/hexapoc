import json
from typing import Tuple
from flask import Flask, request
from app.application import App
from domain.core.model.query import Query, QueryType
from domain.core.exception.errors import SearchBaseException
from http import HTTPStatus
from cmd.http.exception import BadRequestError, InternalError
from cmd.http.helper import fire_error, fire_json_response

app = Flask(__name__)


@app.get('/')
def home():
    return fire_json_response(json=json.dumps({
        "match_pdf": "/search?q=elasticsearch&t=match_pdf",
        "match_in_url": "/search?q=cybelangel&t=in_url",
        "match_exact": "/search?q=hexagonal%20architecture%20in%20python&t=exact_match"
    }), status=HTTPStatus.OK)


def adapt_request_params(params: dict) -> Tuple[str, QueryType]:
    search_term = params.get("q", "")
    if search_term.strip() == "":
        raise BadRequestError("param q is empty")

    request_query_type = params.get("t", "")
    if request_query_type == "match_pdf":
        return search_term, QueryType.MATCH_PDF

    if request_query_type == "exact_match":
        return search_term, QueryType.MATCH_EXACT

    if request_query_type == "in_url":
        return search_term, QueryType.MATCH_IN_URL

    raise BadRequestError(f"query type value <{request_query_type}> is not expected")


@app.get('/search')
def search():
    try:
        query_value, query_type = adapt_request_params(params=request.args)
    except BadRequestError as e:
        return fire_error(e)

    try:
        application = App()
        result = application.search(query=Query(value=query_value, type=query_type))
    except SearchBaseException:
        return fire_error(InternalError(message="something went wrong"))

    return fire_json_response(json=result.model_dump_json(exclude_unset=True), status=HTTPStatus.OK)


if __name__ == "__main__":
    app.run(debug=True, port=2626)
