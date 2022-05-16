import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        url_for_save = (requests.get(f'{url}/upload?path={name_file}&overwrite=True', headers={'Authorization': f'OAuth {token}'})).json()
        with open(file_path, 'rb') as file:
            dict_file = {'file': file}
            requests.put(url_for_save['href'], files=dict_file)


if __name__ == '__main__':
    path_to_file = r'D:\python\numbers.txt'
    name_file = 'numbers.txt'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
