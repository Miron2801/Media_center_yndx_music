from yandex_music import Client
from getpass import getpass
import os
from pprint import pprint

password = getpass()
client = Client.from_credentials('hahanov.i@explabs.ru', password)


def download_liked_track():
    if not os.path.isdir("./liked"):
        os.mkdir("./liked")
    for number, track in enumerate(client.users_likes_tracks()):
        track.fetch_track().download(f'liked/{number}.mp3')


# def download_recommendation():
#     if not os.path.isdir("./recommendations"):
#         os.mkdir("./recommendations")
#     for number, track in enumerate(client.playlists_list()):
#         track.fetch_track().download(f'recommendations/{number}.mp3')

def get_all_playlists():
    return client.playlists_list()


if __name__ == '__main__':
    pprint(list(get_all_playlists()))
