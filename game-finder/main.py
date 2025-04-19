import requests

global IDs, KEY

# Steam IDs to access user data
IDs = {"Rhys": 76561198073983431, "Mike": 97291871927}
# Steam Web API key to access the data
with open("/home/rhys/projects/steam_api.txt") as f:
    KEY = f.readlines()[0].strip()


def player_data() -> None:
    id = IDs["Rhys"]
    url = f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={KEY}&steamids={id}&format=json"
    print(url)
    API = requests.get(url)
    print(API.json())

    url2 = f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={KEY}&steamid={id}&format=json"
    
    API = requests.get(url2)
    print(API.json())


def main() -> None:
    player_data()


if __name__ == "__main__":
    main()
