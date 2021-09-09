import json
import urllib.request
from typing import Any
from typing import Dict
from typing import List
from typing import NamedTuple
from typing import Optional


class Response(NamedTuple):
    value: Any
    count: int

def req(url: str, **kwargs: Any) -> Response:
    resp = urllib.request.urlopen(urllib.request.Request(url, **kwargs))
    obj = json.load(resp)
    return Response(obj.get('value'), obj.get('count'))


def get_all(url: str, **kwargs: Any) -> List[Dict[str, Any]]:
    ret: List[Dict[str, Any]] = []
    resp = req(url, **kwargs)
    return resp.value
