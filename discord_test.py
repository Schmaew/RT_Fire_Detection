# "NjI0ODY1NTA5MTQ5NzY5Nzcw.GLFsNi.bmt72uID-HbqGJL3egirrWifII5_Yfn8YgjbEA"

import requests

payload = {"content": "/play รู้กันแค่สี้"}

header = {
    "authorization": "NjI1NjQxNTE1NzA4MDU1NTUy.GFpfhK.GOZG-i5REp7w0U7VKq4itgdwA-wWhdVgOxrq2E"
}

headeral = {
    "authorization": "NjI0ODY1NTA5MTQ5NzY5Nzcw.GLFsNi.bmt72uID-HbqGJL3egirrWifII5_Yfn8YgjbEA"
}

r = requests.post(
    "https://discord.com/api/v9/channels/558474184989212693/messages",
    json=payload,
    headers=header,
)
