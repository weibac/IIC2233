import os.path

TOKENS_FILE_PATH = os.path.join('data', 'tokens.csv')
ISSUES_FILE_PATH = os.path.join('data', 'issues.csv')

ANIME_BASE_URL = 'https://backend.chan.ing.puc.cl/animeranking/v1/{}'
ANIME_NUMERO = int('08') % 6
REGEX_FILTRO = r'ha[a-z0-9]+o|(.*a.*){3,}'  # Completar

GITHUB_BASE_URL = 'https://api.github.com/repos/{}'
GITHUB_REPO_OWNER = 'IIC2233'
GITHUB_REPO_NAME = 'weibac-iic2233-2022-2'  # Completar
GITHUB_USERNAME = 'weibac'  # Completar
