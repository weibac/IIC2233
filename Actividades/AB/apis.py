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
    url = GITHUB_BASE_URL.format(f'{GITHUB_REPO_OWNER}/{GITHUB_REPO_NAME}/issues')
    headers = {'Authorization': f'token {token}'}
    issue_body = ''
    for anime in animes:
        issue_body += f'{anime.nombre} ({anime.ano})\n'
    data = {
        'owner': GITHUB_REPO_OWNER,
        'repo': GITHUB_REPO_NAME,
        'title': GITHUB_USERNAME,
        'body': issue_body
    }
    data = json.dumps(data)
    response = requests.post(url=url, headers=headers, data=data)
    status_code = response.status_code
    issue_number = response.json()['number']

    return status_code, issue_number


def put_lock_issue(token: str, numero_issue: int) -> int:
    # ToDo: Completar
    status_code = 404
    url = GITHUB_BASE_URL.format(f'{GITHUB_REPO_OWNER}/{GITHUB_REPO_NAME}/issues/{numero_issue}/lock')
    headers = {'Authorization': f'token {token}'}
    data = {
        'owner': GITHUB_REPO_OWNER,
        'repo': GITHUB_REPO_NAME,
        'issue_number': numero_issue
    }
    data = json.dumps(data)
    response = requests.post(url=url, headers=headers, data=data)
    print(response.json())
    status_code = response.status_code

    return status_code


def delete_lock_issue(token: str, numero_issue: int) -> int:
    # ToDo: Completar
    status_code = 404
    url = GITHUB_BASE_URL.format(f'{GITHUB_REPO_OWNER}/{GITHUB_REPO_NAME}/issues/{numero_issue}/lock')
    headers = {'Authorization': f'token {token}'}
    data = {
        'owner': GITHUB_REPO_OWNER,
        'repo': GITHUB_REPO_NAME,
        'issue_number': numero_issue
    }
    data = json.dumps(data)
    response = requests.post(url=url, headers=headers, data=data)
    status_code = response.status_code

    return status_code
