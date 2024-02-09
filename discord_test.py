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
