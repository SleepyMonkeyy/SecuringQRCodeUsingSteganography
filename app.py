import json
import requests
headers = {"Authorization": "Bearer ya29.a0ARrdaM9RGMf-fI8P_cXa5cB2lios2dOLE_asQIPlwVq96dxdI6CeUt-xsLGFDfTk43JvNmwoQ6icUACyLjtJevGA3s_BIlnk76EqwqW6vL0i9KKOHohj1NrYvJNqfjCHTJpgV1UznljHuInyPzdpErv6AyQv"} #put ur access token after the word 'Bearer '
para = {
    "name": "stegoimage.png", #file name to be uploaded
    "parents": ["1nwDngaAMZ_55Vl8HSehF7MQ8Ap5bGHAP"] # make a folder on drive in which you want to upload files; then open that folder; the last thing in present url will be folder id
}
files = {
    'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
    'file': ('application/zip',open("./stegoimage.png", "rb")) # replace 'application/zip' by 'image/png' for png images; similarly 'image/jpeg' (also replace your file name)
}
r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files
)
print(r.text)