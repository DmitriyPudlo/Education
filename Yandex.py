import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = 'AQAAAAASal_eAADLW5M3p3j4ykZAoQrLaHNtJVI'

    def upload(self, file_path: str):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        url_for_save = (requests.get(f'{url}/upload?path={name_file}&overwrite=True', headers={'Authorization': f'OAuth {token}'})).json()
        with open(file_path, 'rb') as file:
            dict_file = {'file': file}
            requests.put(url_for_save['href'], files=dict_file)


if __name__ == '__main__':
    path_to_file = r'D:\python\numbers.txt'
    name_file = 'numbers.txt'
    token = 'a67f00c673c3d4b12800dd0ba29579ec56d804f3c5f3bbcef5328d4b3981fa5987b951cf2c8d8b24b9abd'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
