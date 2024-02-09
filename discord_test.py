# "NjI0ODY1NTA5MTQ5NzY5Nzcw.GLFsNi.bmt72uID-HbqGJL3egirrWifII5_Yfn8YgjbEA"

import requests

payload = {"content": "hi"}

header = {
    ""
}

headeral = {
    ""
}

r = requests.post(
    "https://discord.com/api/v9/channels/(your channel)/messages",
    json=payload,
    headers=header,
)
