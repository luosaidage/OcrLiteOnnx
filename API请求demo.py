import requests

def local_ocr(path):
    headers = {
        'accept': 'application/json',
        # requests won't add a boundary if this header is set when you pass files=
        # 'Content-Type': 'multipart/form-data',
    }

    ip = '127.0.0.1'
    port = '7089'
    url = "http://" + ip + ":" + port + '/api/tr-run/'

    files = {
        'file': open(path, 'rb'),
    }

    response = requests.post(url, headers=headers, files=files)
    print(response.json())
    return response.json()

local_ocr('test_imgs/img.png')