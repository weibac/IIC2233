from typing import Tuple, List
import requests
import json

from parametros import GITHUB_BASE_URL, GITHUB_REPO_OWNER, GITHUB_REPO_NAME
from parametros import GITHUB_USERNAME
from parametros import ANIME_BASE_URL, ANIME_NUMERO
from utils.anime import Anime


def get_animes() -> Tuple[int, List[Anime]]:
    # ToDo: Completar
    status_code = 404
    animes = []
    # Request
    url = ANIME_BASE_URL.format(f'AB?id={ANIME_NUMERO}')
    response = requests.get(url)
    status_code = response.status_code
    animes_dict = response.json()['animes']
    # Procesamiento
    for a in range(len(animes_dict)):
        anime = animes_dict[a]
        nombre = anime['name']
        ano = anime['season']['year']
        tags = []
        for b in range(len(anime['tags'])):
            tags.append(anime['tags'][b]['name'])
        anime = Anime(nombre, ano, tags)
        animes.append(anime)
    return status_code, animes


def post_issue(token, animes: List[Anime]) -> Tuple[int, int]:
    # ToDo: Completar
    status_code = 404
    issue_number = -1

    return status_code, issue_number


def put_lock_issue(token: str, numero_issue: int) -> int:
    # ToDo: Completar
    status_code = 404

    return status_code


def delete_lock_issue(token: str, numero_issue: int) -> int:
    # ToDo: Completar
    status_code = 404

    return status_code
