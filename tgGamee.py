
import requests
import hashlib

def get_checksum(score, play_time, url):
    game_state_data = ""
    str2hash = (
        f"{score}:{play_time}:{url}:{game_state_data}:"
        "crmjbjm3lczhlgnek9uaxz2l9svlfjw14npauhen"
    )
    result = hashlib.md5(str2hash.encode())
    checksum = result.hexdigest()
    return checksum

# Новое значение счета
new_score = 108563

# Время игры
play_time = 11

# URL игры
game_url = "/game-bot/neonracer-c94fc835c451e29841b94038b06a03295bd80cdc"

# Генерация контрольной суммы
checksum = get_checksum(new_score, play_time, game_url)

# URL эндпоинта API
api_endpoint = "https://api.service.gameeapp.com/"

# Запрос на изменение счета
response = requests.post(api_endpoint, json={
    "id": "game.saveWebGameplay",
    "jsonrpc": "2.0",
    "method": "game.saveWebGameplay",
    "params": {
        "gameplayData": {
            "checksum": checksum,
            "createdTime": "2024-03-06T23:52:30+06:00",
            "gameId": 287,
            "gameplayOrigin": "game",
            "gameStateData": None,
            "gameUrl": game_url,
            "isSaveState": False,
            "metadata": {"gameplayId": 18},
            "playTime": play_time,
            "releaseNumber": 3,
            "replayData": None,
            "replayDataChecksum": None,
            "replayVariant": None,
            "score": new_score
        }
    }
})

# Вывод результата запроса
print(response.text)
