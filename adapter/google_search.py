import requests
import re
from domain.core.model.query import Query, QueryType
from domain.core.model.result import Result, Match
from domain.core.port.finder import Finder
from domain.core.port.parser import Parser
from domain.core.exception.errors import FinderException, ParserException
from http import HTTPStatus
from bs4 import BeautifulSoup

USER_AGENT = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36")

GOOGLE_SEARCH_URL_TPL = "https://google.com/search?q={}&hl=fr&lr=lang_fr"


class GoogleSearch(Finder):
    @staticmethod
    def _get(url: str) -> bytes:
        response = requests.get(url, headers={"User-Agent": USER_AGENT})
        if response.status_code != HTTPStatus.OK:
            raise Exception(f"something went wrong, error={response.text}",)
        return response.content

    @staticmethod
    def _build_search_url(query: str) -> str:
        return GOOGLE_SEARCH_URL_TPL.format(query)

    @staticmethod
    def _parse_search_result(search_response: bytes) -> Result:
        soup = BeautifulSoup(search_response, "html.parser")

        nb_results = int(re.search(r'\d+', soup.select("#result-stats").pop().text).group())

        h3s = soup.find_all("h3")
        matches = [Match(summary=h3.parent.text, link=h3.parent.attrs.get("href", "link-not-found")) for h3 in h3s]

        return Result(
            count=nb_results,
            best_match=matches[0] if len(matches) > 0 else Match(summary="nothing found", link=""),
            top_3_matches=matches[:3] if len(matches) > 0 else []
        )

    def search(self, query: str):
        try:
            url = self._build_search_url(query=query)
            print(url)
            return self._parse_search_result(
                search_response=self._get(url)
            )
        except Exception as e:
            print(e)
            raise FinderException("GoogleSearch.search failed!") from e


class GoogleQueryParser(Parser):
    def parse(self, query: Query) -> str:
        try:
            if query.type == QueryType.MATCH_IN_URL:
                return f"inurl:{query.value}"

            if query.type == QueryType.MATCH_PDF:
                return f"{query.value} filetype:pdf"

            if query.type == QueryType.MATCH_EXACT:
                return f"\"{query.value}\""

            return query.value
        except Exception as e:
            raise ParserException("GoogleQueryParser.parse failed!") from e
