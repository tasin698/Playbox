from django.shortcuts import redirect, render,  HttpResponseRedirect
from musicbeats.models import Song, Listenlater, Favourites, History, Channel
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.db.models import Case, When

def home(request):
    if request.user.is_authenticated:
        if request.user.is_junior:
            is_junior_songs = True
            song = Song.objects.filter(is_junior_song=is_junior_songs)
        elif request.user.is_juniorplus:
            is_juniorplus_songs = True
            song = Song.objects.filter(is_juniorplus_song=is_juniorplus_songs)
        elif request.user.is_senior:
            is_senior_songs = True
            song = Song.objects.filter(is_senior_song=is_senior_songs)
        else:
            song = Song.objects.all()[0:3]
        wl = Listenlater.objects.filter(user=request.user)
        ids = []
        for i in wl:
            ids.append(i.listen_music_id)
        preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
        listen = Song.objects.filter(song_id__in=ids).order_by(preserved) 
        listen = reversed(listen)

        fl = Favourites.objects.filter(user=request.user)
        jds = []
        for j in fl:
            jds.append(j.fmusic_id)
        preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(jds)])
        favourites = Song.objects.filter(song_id__in=jds).order_by(preserved) 
        favourites = reversed(favourites)

        return render(request, 'musicbeats/home.htm', {'song': song, 'listen': listen, 'favourites': favourites})
    else:
        return render(request, 'musicbeats/login.htm') 


def history(request):
    if request.method == "POST":
        user = request.user
        music_id = request.POST['music_id']
        history = History(user=user, music_id=music_id)
        history.save()

        return redirect(f"/musicbeats/songs/{music_id}")

    history = History.objects.filter(user=request.user)
    ids = []
    for i in history:
        ids.append(i.music_id)
    
    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
    song = Song.objects.filter(song_id__in=ids).order_by(preserved)

    return render(request, 'musicbeats/history.htm', {"history": song})

def listenlater(request):
    if request.method == "POST":
        user = request.user
        listen_music_id = request.POST['listen_music_id']

        listen = Listenlater.objects.filter(user=user)
        
        for i in listen:
            if listen_music_id == i.listen_music_id:
                message = "Your Music is Already Added"
                break
        else:
            listenlater = Listenlater(user=user, listen_music_id=listen_music_id)
            listenlater.save()
            message = "Your Music is Succesfully Added"

        song = Song.objects.filter(song_id=listen_music_id).first()
        return render(request, f"musicbeats/songpost.htm", {'song': song, "message": message})

    wl = Listenlater.objects.filter(user=request.user)
    ids = []
    for i in wl:
        ids.append(i.listen_music_id)
    
    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
    song = Song.objects.filter(song_id__in=ids).order_by(preserved)

    return render(request, "musicbeats/listenlater.htm", {'song': song})


def removelistenlater(request, id):
    if request.method == "GET":
        user = request.user
        listen_music_id = id
        listen = Listenlater.objects.filter(user=user, listen_music_id=listen_music_id)
        listen.delete()
        return redirect('/musicbeats/home/')

def favourites(request):
    if request.method == "POST":
        user = request.user
        fmusic_id = request.POST['fmusic_id']

        fav = Favourites.objects.filter(user=user)
        
        for i in fav:
            if fmusic_id == i.fmusic_id:
                message = "Your Music is Already Added"
                break
        else:
            favourites = Favourites(user=user, fmusic_id=fmusic_id)
            favourites.save()
            message = "Your Music is Succesfully Added"

        song = Song.objects.filter(song_id=fmusic_id).first()
        return render(request, f"musicbeats/songpost.htm", {'song': song, "message": message})

    wl = Favourites.objects.filter(user=request.user)
    ids = []
    for i in wl:
        ids.append(i.fmusic_id)
    
    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
    song = Song.objects.filter(song_id__in=ids).order_by(preserved)

    return render(request, "musicbeats/favourites.htm", {'song': song})

def removefavourites(request, id):
    if request.method == "GET":
        user = request.user
        fmusic_id = id
        favourites = Favourites.objects.filter(user=user, fmusic_id=fmusic_id)
        favourites.delete()
        return redirect('/musicbeats/home/')




def songs(request):
    if request.user.is_authenticated:
        if request.user.is_junior:
            is_junior_songs = True
            song = Song.objects.filter(is_junior_song=is_junior_songs)
            return render(request, 'musicbeats/songs.htm', {'song': song})
        elif request.user.is_juniorplus:
            is_juniorplus_songs = True
            song = Song.objects.filter(is_juniorplus_song=is_juniorplus_songs)
            return render(request, 'musicbeats/songs.htm', {'song': song})
        else:
            song = Song.objects.all()[0:3]
            return render(request, 'musicbeats/songs.htm', {'song': song})
    else:
        return render(request, 'musicbeats/login.htm') 

def rocksongs(request):
    if request.user.is_authenticated:
        if request.user.is_junior:
            is_junior_songs = True
            is_rock_songs = True
            song = Song.objects.filter(is_junior_song=is_junior_songs, is_rock_song=is_rock_songs)
            return render(request, 'musicbeats/songs.htm', {'song': song})
        elif request.user.is_juniorplus:
            is_juniorplus_songs = True
            is_rock_songs = True
            song = Song.objects.filter(is_juniorplus_song=is_juniorplus_songs, is_rock_song=is_rock_songs)
            return render(request, 'musicbeats/songs.htm', {'song': song})
        elif request.user.is_senior:
            is_senior_songs = True
            is_rock_songs = True
            song = Song.objects.filter(is_senior_song=is_senior_songs, is_rock_song=is_rock_songs)
            return render(request, 'musicbeats/songs.htm', {'song': song})
        else:
            song = Song.objects.all()[0:3]
            return render(request, 'musicbeats/songs.htm', {'song': song})
    else:
        return render(request, 'musicbeats/login.htm') 


def popsongs(request):
    if request.user.is_authenticated:
        if request.user.is_junior:
            is_junior_songs = True
            is_pop_songs = True
            song = Song.objects.filter(is_junior_song=is_junior_songs, is_pop_song=is_pop_songs)
            return render(request, 'musicbeats/songs.htm', {'song': song})
        elif request.user.is_juniorplus:
            is_juniorplus_songs = True
            is_pop_songs = True
            song = Song.objects.filter(is_juniorplus_song=is_juniorplus_songs, is_pop_song=is_pop_songs)
            return render(request, 'musicbeats/songs.htm', {'song': song})
        elif request.user.is_senior:
            is_senior_songs = True
            is_pop_songs = True
            song = Song.objects.filter(is_senior_song=is_senior_songs, is_pop_song=is_pop_songs)
            return render(request, 'musicbeats/songs.htm', {'song': song})
        else:
            song = Song.objects.all()[0:3]
            return render(request, 'musicbeats/songs.htm', {'song': song})
    else:
        return render(request, 'musicbeats/login.htm') 

def classicalsongs(request):
    if request.user.is_authenticated:
        if request.user.is_junior:
            is_junior_songs = True
            is_classical_songs = True
            song = Song.objects.filter(is_junior_song=is_junior_songs, is_classical_song=is_classical_songs)
            return render(request, 'musicbeats/songs.htm', {'song': song})
        elif request.user.is_juniorplus:
            is_juniorplus_songs = True
            is_classical_songs = True
            song = Song.objects.filter(is_juniorplus_song=is_juniorplus_songs, is_classical_song=is_classical_songs)
            return render(request, 'musicbeats/songs.htm', {'song': song})
        elif request.user.is_senior:
            is_senior_songs = True
            is_classical_songs = True
            song = Song.objects.filter(is_senior_song=is_senior_songs, is_classical_song=is_classical_songs)
            return render(request, 'musicbeats/songs.htm', {'song': song})
        else:
            song = Song.objects.all()[0:3]
            return render(request, 'musicbeats/songs.htm', {'song': song})
    else:
        return render(request, 'musicbeats/login.htm') 




def songpost(request, id):
    song = Song.objects.filter(song_id=id).first()
    return render(request, 'musicbeats/songpost.htm', {'song': song})

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        from django.contrib.auth import login
        if user is not None:
            login(request, user)
            channel = Channel(name=username)
            channel.save()   
            return HttpResponseRedirect('/musicbeats/home/')

    return render(request, 'musicbeats/login.htm')
    
def logout_user(request):
    logout(request)
    return redirect("/")

def channel(request, channel):
    chan = Channel.objects.filter(name=channel).first()
    listen_music_ids = str(chan.music).split(" ")[1:]

    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(listen_music_ids)])
    song = Song.objects.filter(song_id__in=listen_music_ids).order_by(preserved)
    

    return render(request, "musicbeats/channel.htm", {"channel": chan, "song": song})

def upload(request):
    if request.method == "POST":
        name = request.POST['name']
        singer = request.POST['singer']
        tag = request.POST['tag']
        image = request.POST['image']
        movie = request.POST['movie']
        song1 = request.FILES['file']

        song_model = Song(name=name, singer=singer, tags=tag, image=image, movie=movie, song=song1)
        song_model.save()

        music_id = song_model.song_id
        channel_find = Channel.objects.filter(name=str(request.user))
        print(channel_find)

        for i in channel_find:
            i.music += f" {music_id}"
            i.save()
        return HttpResponseRedirect('/musicbeats/home/')
    return render(request, "musicbeats/upload.htm")



def search(request):
    query = request.GET.get("query")
    song = Song.objects.all()
    qs = song.filter(name__icontains=query)
    return render(request, 'musicbeats/search.htm', {'songs': qs, "query": query})
