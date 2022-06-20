from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import face_recognition
from glob import glob
from .models import *
import spotipy
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
# Create your views here.
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="7ea12ca83ae84c0989daac9d8f8a85e0",
                                               client_secret="160e31e12342404a9b1e38c621a7ab41",
                                               redirect_uri="http://127.0.0.1:8080/spotify/",
                                               scope="user-library-read"))

def index(request):
    return render(request, 'face/index.html')

def loginform(request):
    return render(request, 'face/login.html')

def signupform(request):
    return render(request, 'face/signup.html')

def signupsubmit(request):
    first_name = request.POST['fname']
    last_name = request.POST['lname']
    username = request.POST['email']
    # phone = request.POST['phone']
    password = request.POST['password']
    spotify_uid = request.POST['spotify_uid']
    profile_pic = request.FILES['file']
    fs = FileSystemStorage()
    user = UserOfApp.objects.create_user(first_name = first_name, last_name = last_name, username = username, password = password, spotify_uid=spotify_uid)
    filename = 'face_db/' + str(user.id) + str(profile_pic)
    user.photo = filename
    print(fs.save(filename, profile_pic), profile_pic)
    user.save()
    return render(request, 'face/login.html')

def loginsubmit(request):
    username = request.POST['email']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        print('sucess')
        return HttpResponseRedirect('/face')
    else:
        return render(reques, 'rentit/login.html')

def face_recog(t):
    files = glob(
        '/Users/adityachavan/Desktop/aditya/Web-Technologies-College/django/first/face_db/*')
    Users = UserOfApp.objects.all()
    print('t: ', t, type(t))
    for i in Users:
        print(i.spotify_uid)
        print("iphoto", i.photo, type(i.photo))
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
        playlists = sp.user_playlists(t[1])
        playlist_tracks = sp.playlist_tracks(playlists['items'][1]['id'])
        # print(playlist_tracks)
        # print(playlists)
        # print(playlists)
        user = {
        'name': t[2].first_name + " " + t[2].last_name
        }
    else:
        print("not found")
        playlists = sp.user_playlists('joab4qf54hmmc19t23jmj7i1h')
        playlist_tracks = sp.playlist_tracks(playlists['items'][1]['id'])
        user = {
        'name': "Guest User"
        }
    playlists_list = playlists['items']
    content = {
        'user': user,
        'playlists': playlists_list,
        'playlist_tracks': playlist_tracks

    }
    return render(request, 'face/showplaylists.html', content)
