from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import face_recognition
from glob import glob
from .models import *
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
# Create your views here.
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="7ea12ca83ae84c0989daac9d8f8a85e0",
                                               client_secret="160e31e12342404a9b1e38c621a7ab41",
                                               redirect_uri="http://127.0.0.1:8080/spotify/",
                                               scope="user-library-read"))

def index(request):
    return render(request, 'face/index.html')


def face_recog(t):
    files = glob(
        '/Users/adityachavan/Desktop/aditya/Web-Technologies-College/django/first/face_db/*')
    Users = UserOfApp.objects.all()
    for i in Users:
        print(i.spotify_uid)
        print(i.photo)
    # print(Users)
    # for i in files:
        picture_of_me = face_recognition.load_image_file(i.photo)
        my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

        # my_face_encoding now contains a universal 'encoding' of my facial features that can be compared to any other picture of a face!
        # t = "unknown" + str(maxi) + ".jpeg"
        unknown_picture = face_recognition.load_image_file(t)

        face_encode = face_recognition.face_encodings(unknown_picture)
        if len(face_encode) > 0:
            unknown_face_encoding = face_encode[0]
        else:
            return[False]
            # Now we can see the two face encodings are of the same person with `compare_faces`!

        results = face_recognition.compare_faces(
            [my_face_encoding], unknown_face_encoding)
        if results[0] == True:
            return [True, i.spotify_uid, i]
    else:                   # For else hai ye chomu
        return [False]


def photodetect(request):
    image = request.FILES['file']
    print(image, type(image), str(image))
    fs = FileSystemStorage()
    filename = 'upload/' + str(image)
    print(fs.save(filename, image), image)
    t = face_recog(filename)
    print(t)
    if t[0]:
        print(t[1][:-5])
    else:
        print("not found")
    if t:
        playlists = sp.user_playlists(t[1])
        playlists_list = playlists['items']
        user = t[2]
        content = {
            'user': user,
            'playlists': playlists_list,
        }
    else:
        content = {
            'user': request.user,
            'playlists':
            [
                {'collaborative': False,
                 'description': '',
                 'external_urls': {'spotify': 'https://open.spotify.com/playlist/0ceKSd8Eh2iwi0oNVPbzpe'},
                 'href': 'https://api.spotify.com/v1/playlists/0ceKSd8Eh2iwi0oNVPbzpe',
                 'id': '0ceKSd8Eh2iwi0oNVPbzpe',
                 'images': [{'height': 640,
                             'url': 'https://mosaic.scdn.co/640/ab67616d0000b273209142163e85eff8ceeac2b2ab67616d0000b273758b7328e71d56dfa11fabf9ab67616d0000b27382b243023b937fd579a35533ab67616d0000b273f7021e7f9cd49138befad615',
                             'width': 640},
                            {'height': 300,
                             'url': 'https://mosaic.scdn.co/300/ab67616d0000b273209142163e85eff8ceeac2b2ab67616d0000b273758b7328e71d56dfa11fabf9ab67616d0000b27382b243023b937fd579a35533ab67616d0000b273f7021e7f9cd49138befad615',
                             'width': 300},
                            {'height': 60,
                             'url': 'https://mosaic.scdn.co/60/ab67616d0000b273209142163e85eff8ceeac2b2ab67616d0000b273758b7328e71d56dfa11fabf9ab67616d0000b27382b243023b937fd579a35533ab67616d0000b273f7021e7f9cd49138befad615',
                             'width': 60}],
                 'name': 'For shirsha',
                 'owner': {'display_name': 'Heena',
                           'external_urls': {'spotify': 'https://open.spotify.com/user/joab4qf54hmmc19t23jmj7i1h'},
                           'href': 'https://api.spotify.com/v1/users/joab4qf54hmmc19t23jmj7i1h',
                           'id': 'joab4qf54hmmc19t23jmj7i1h',
                           'type': 'user',
                           'uri': 'spotify:user:joab4qf54hmmc19t23jmj7i1h'},
                 'primary_color': None,
                 'public': True,
                 'snapshot_id': 'MTIsNTg2MWM5MjMzNzhlNWQ1MThhNTMwZDFkYTg3MjAxYmUzOTU4NzNlZA==',
                 'tracks': {'href': 'https://api.spotify.com/v1/playlists/0ceKSd8Eh2iwi0oNVPbzpe/tracks',
                            'total': 11},
                 'type': 'playlist',
                 'uri': 'spotify:playlist:0ceKSd8Eh2iwi0oNVPbzpe'}

            ]
        }
    return render(request, 'face/showplaylists.html', content)
