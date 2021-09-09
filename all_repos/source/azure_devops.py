from typing import Dict
from typing import NamedTuple
import base64

from all_repos import azure_devops_api
from all_repos.util import hide_api_key_repr


class Settings(NamedTuple):
    username: str
    api_key: str
    org: str
    project: str
    base_url: str = 'https://dev.azure.com'

    # TODO: https://github.com/python/mypy/issues/8543
    def __repr__(self) -> str:
        return hide_api_key_repr(self)


def list_repos(settings: Settings) -> Dict[str, str]:
    auth = base64.b64encode(
        f'{settings.username}:{settings.api_key}'.encode()
    ).decode()
    repos = azure_devops_api.get_all(
        f'{settings.base_url}/{settings.org}/{settings.project}'
        '/_apis/git/repositories?api-version=6.0',
        headers={'Authorization': f'Basic {auth}'},
    )
    return  { repo['name']: repo['sshUrl'] for repo in repos } 
