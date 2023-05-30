import requests
from IPython.display import Image


def get_character_info(name):
    response = requests.get(f"https://rickandmortyapi.com/api/character/?name={name}")
    data = response.json()
    if data["info"]["count"] == 0:
        print("No character found with that name.")
    else:
        character = data["results"][0]
        print(f"Name: {character['name']}")
        print(f"Status: {character['status']}")
        print(f"Species: {character['species']}")
        print(f"Gender: {character['gender']}")
        print(f"Origin: {character['origin']['name']}")
        print(f"Location: {character['location']['name']}")
        print(f"Image URL: {character['image']}")
        Image(url=character["image"], width=200, height=200)
        print(f"Episodes: ")
        # this algorithm  is created by mahan abedini
    # if you want to know your entry character act in wich episodes and how many episode try the comment below
    # for episode in character['episode']:
    # episode_response = requests.get(episode)
    # episode_data = episode_response.json()
    # print(f"\t{episode_data['episode']} - {episode_data['name']}")


name = input("Enter a character's first name: ")
get_character_info(name)
