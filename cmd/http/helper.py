from typing import Tuple

from .exception import ApiError


def fire_error(error: ApiError) -> Tuple[str, int, dict[str, str]]:
    return fire_json_response(json=error.dump(), status=error.status)


def fire_json_response(json: str, status: int) -> Tuple[str, int, dict[str, str]]:
    return json, status, {"Content-Type": "application/json"}
