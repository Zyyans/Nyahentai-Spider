from requests import get

# Made by Zyyans


def get_response(url):
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'
    }

    try:
        response = get(url, headers=headers)
    except:
        pass
    else:
        return response
