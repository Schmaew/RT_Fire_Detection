# "NjI0ODY1NTA5MTQ5NzY5Nzcw.GLFsNi.bmt72uID-HbqGJL3egirrWifII5_Yfn8YgjbEA"

import requests

payload = {"content": "/play รู้กันแค่สี้"}

header = {
    ""
}

headeral = {
    ""
}

r = requests.post(
    "https://discord.com/api/v9/channels/558474184989212693/messages",
    json=payload,
    headers=header,
)
