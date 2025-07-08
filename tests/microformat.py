import extruct
import requests
from w3lib.html import get_base_url


def read(
    url: str,
    headers={
        'User-Agent': 'SchemaOrgMicroformatTest/1.0 (Python; +http://example.com/my-test-suite)'
    },
    syntaxes=['json-ld'],
    errors='strict',  # 'log' or 'ignore' or 'strict'
) -> dict:
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4XX or 5XX)
    except requests.RequestException as e:
        raise Exception(f"Failed to fetch URL {url}: {e}")
    base_url = get_base_url(response.text, response.url)
    data = extruct.extract(
        response.text, base_url=base_url, syntaxes=syntaxes, errors=errors
    )
    return data
