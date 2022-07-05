from django.shortcuts import redirect, render,  HttpResponseRedirect
from playwatch.models import Movie, Watchlater, WatchHistory, WatchChannel, WatchFavourites
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.models import Case, When

def homewatch(request):
    if request.user.is_authenticated:
        if request.user.is_junior:
            is_junior_movies = True
            movie = Movie.objects.filter(is_junior_movie=is_junior_movies)
        elif request.user.is_juniorplus:
            is_juniorplus_movies = True
            movie = Movie.objects.filter(is_juniorplus_movie=is_juniorplus_movies)
        elif request.user.is_senior:
            is_senior_movies = True
            movie = Movie.objects.filter(is_senior_movie=is_senior_movies)
        else:
            movie = Movie.objects.all()[0:3]
        wl = Watchlater.objects.filter(user=request.user)
        ids = []
        for i in wl:
            ids.append(i.watch_video_id)
        preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
        watch = Movie.objects.filter(movie_id__in=ids).order_by(preserved)
        watch = reversed(watch)

        fl = WatchFavourites.objects.filter(user=request.user)
        jds = []
        for j in fl:
            jds.append(j.fvideo_id)
        preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(jds)])
        favourites = Movie.objects.filter(movie_id__in=jds).order_by(preserved)
        favourites = reversed(favourites)

        return render(request, 'playwatch/homewatch.htm', {'movie': movie, 'watch': watch, 'favourites': favourites})
    else:
        return render(request, 'playwatch/loginwatch.htm')

def watchhistory(request):
    if request.method == "POST":
        user = request.user
        video_id = request.POST['video_id']
        watchhistory = WatchHistory(user=user, video_id=video_id)
        watchhistory.save()

        return redirect(f"/playwatch/movies/{video_id}")

    watchhistory = WatchHistory.objects.filter(user=request.user)
    ids = []
    for i in watchhistory:
        ids.append(i.video_id)

    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
    movie = Movie.objects.filter(movie_id__in=ids).order_by(preserved)

    return render(request, 'playwatch/watchhistory.htm', {"watchhistory": movie})

def watchlater(request):
    if request.method == "POST":
        user = request.user
        watch_video_id = request.POST['watch_video_id']

        watch = Watchlater.objects.filter(user=user)

        for i in watch:
            if watch_video_id == i.watch_video_id:
                message = "Your Video is Already Added"
                break
        else:
            watchlater = Watchlater(user=user, watch_video_id=watch_video_id)
            watchlater.save()
            message = "Your Video is Succesfully Added"

        movie = Movie.objects.filter(movie_id=watch_video_id).first()
        return render(request, f"playwatch/moviepost.htm", {'movie': movie, "message": message})

    wl = Watchlater.objects.filter(user=request.user)
    ids = []
    for i in wl:
        ids.append(i.watch_video_id)

    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
    movie = Movie.objects.filter(movie_id__in=ids).order_by(preserved)

    return render(request, "playwatch/watchlater.htm", {'movie': movie})


def removewatchlater(request, id):
    if request.method == "GET":
        user = request.user
        watch_video_id = id
        watch = Watchlater.objects.filter(user=user, watch_video_id=watch_video_id)
        watch.delete()
        return redirect('/playwatch/homewatch/')

def wfavourites(request):
    if request.method == "POST":
        user = request.user
        fvideo_id = request.POST['fvideo_id']

        fav = WatchFavourites.objects.filter(user=user)

        for i in fav:
            if fvideo_id == i.fvideo_id:
                message = "Your Movie is Already Added"
                break
        else:
            favourites = WatchFavourites(user=user, fvideo_id=fvideo_id)
            favourites.save()
            message = "Your Movie is Succesfully Added"

        movie = Movie.objects.filter(movie_id=fvideo_id).first()
        return render(request, f"playwatch/moviepost.htm", {'movie': movie, "message": message})

    wl = WatchFavourites.objects.filter(user=request.user)
    ids = []
    for i in wl:
        ids.append(i.fvideo_id)

    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
    movie = Movie.objects.filter(movie_id__in=ids).order_by(preserved)

    return render(request, "playwatch/wfavourites.htm", {'movie': movie})

def removewfavourites(request, id):
    if request.method == "GET":
        user = request.user
        fvideo_id = id
        favourites = WatchFavourites.objects.filter(user=user, fvideo_id=fvideo_id)
        favourites.delete()
        return redirect('/playwatch/homewatch/')

def movies(request):
    if request.user.is_authenticated:
        if request.user.is_junior:
            is_junior_movies = True
            movie = Movie.objects.filter(is_junior_movie=is_junior_movies)
            return render(request, 'playwatch/movies.htm', {'movie': movie})
        elif request.user.is_juniorplus:
            is_juniorplus_movies = True
            movie = Movie.objects.filter(is_juniorplus_movie=is_juniorplus_movies)
            return render(request, 'playwatch/movies.htm', {'movie': movie})
        else:
            movie = Movie.objects.all()[0:3]
            return render(request, 'playwatch/movies.htm', {'movie': movie})
    else:
        return render(request, 'playwatch/loginwatch.htm')

def actionmovies(request):
    if request.user.is_authenticated:
        if request.user.is_junior:
            is_junior_movies = True
            is_action_movies = True
            movie = Movie.objects.filter(is_junior_movie=is_junior_movies, is_action_movie=is_action_movies)
            return render(request, 'playwatch/movies.htm', {'movie': movie})
        elif request.user.is_juniorplus:
            is_juniorplus_movies = True
            is_action_movies = True
            movie = Movie.objects.filter(is_juniorplus_movie=is_juniorplus_movies, is_action_movie=is_action_movies)
            return render(request, 'playwatch/movies.htm', {'movie': movie})
        elif request.user.is_senior:
            is_senior_movies = True
            is_action_movies = True
            movie = Movie.objects.filter(is_senior_movie=is_senior_movies, is_action_movie=is_action_movies)
            return render(request, 'playwatch/movies.htm', {'movie': movie})
        else:
            movie = Movie.objects.all()[0:3]
            return render(request, 'playwatch/movies.htm', {'movie': movie})
    else:
        return render(request, 'playwatch/loginwatch.htm')


def thrillermovies(request):
    if request.user.is_authenticated:
        if request.user.is_junior:
            is_junior_movies = True
            is_thriller_movies = True
            movie = Movie.objects.filter(is_junior_movie=is_junior_movies, is_thriller_movie=is_thriller_movies)
            return render(request, 'playwatch/movies.htm', {'movie': movie})
        elif request.user.is_juniorplus:
            is_juniorplus_movies = True
            is_thriller_movies = True
            movie = Movie.objects.filter(is_juniorplus_movie=is_juniorplus_movies, is_thriller_movie=is_thriller_movies)
            return render(request, 'playwatch/movies.htm', {'movie': movie})
        elif request.user.is_senior:
            is_senior_movies = True
            is_thriller_movies = True
            movie = Movie.objects.filter(is_senior_movie=is_senior_movies, is_thriller_movie=is_thriller_movies)
            return render(request, 'playwatch/movies.htm', {'movie': movie})
        else:
            movie = Movie.objects.all()[0:3]
            return render(request, 'playwatch/movies.htm', {'movie': movie})
    else:
        return render(request, 'playwatch/loginwatch.htm')

def comedymovies(request):
    if request.user.is_authenticated:
        if request.user.is_junior:
            is_junior_movies = True
            is_comedy_movies = True
            movie = Movie.objects.filter(is_junior_movie=is_junior_movies, is_comedy_movie=is_comedy_movies)
            return render(request, 'playwatch/movies.htm', {'movie': movie})
        elif request.user.is_juniorplus:
            is_juniorplus_movies = True
            is_comedy_movies = True
            movie = Movie.objects.filter(is_juniorplus_movie=is_juniorplus_movies, is_comedy_movie=is_comedy_movies)
            return render(request, 'playwatch/movies.htm', {'movie': movie})
        elif request.user.is_senior:
            is_senior_movies = True
            is_comedy_movies = True
            movie = Movie.objects.filter(is_senior_movie=is_senior_movies, is_comedy_movie=is_comedy_movies)
            return render(request, 'playwatch/movies.htm', {'movie': movie})
        else:
            movie = Movie.objects.all()[0:3]
            return render(request, 'playwatch/movies.htm', {'movie': movie})
    else:
        return render(request, 'playwatch/loginwatch.htm')

def moviepost(request, id):
    movie = Movie.objects.filter(movie_id=id).first()
    return render(request, 'playwatch/moviepost.htm', {'movie': movie})

def loginwatch(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        from django.contrib.auth import login
        if user is not None:
            login(request, user)
            watchchannel = WatchChannel(name=username)
            watchchannel.save()
            return HttpResponseRedirect('/playwatch/homewatch/')

    return render(request, 'playwatch/loginwatch.htm')


def logout_user_watch(request):
    logout(request)
    return redirect("/")

def channelwatch(request, watchchannel):
    chan = WatchChannel.objects.filter(name=watchchannel).first()
    watch_video_ids = str(chan.video).split(" ")[1:]

    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(watch_video_ids)])
    movie = Movie.objects.filter(movie_id__in=watch_video_ids).order_by(preserved)


    return render(request, "playwatch/channelwatch.htm", {"channelwatch": chan, "movie": movie})

def uploadvideo(request):
    if request.method == "POST":
        name = request.POST['name']
        director = request.POST['director']
        tag = request.POST['tag']
        image = request.POST['image']
        description = request.POST['description']
        movie1 = request.FILES['file']

        movie_model = Movie(name=name, director=director, tags=tag, image=image, description=description, movie=movie1)
        movie_model.save()

        video_id = movie_model.movie_id
        channelwatch_find = WatchChannel.objects.filter(name=str(request.user))
        print(channelwatch_find)

        for i in channelwatch_find:
            i.video += f" {video_id}"
            i.save()
        return HttpResponseRedirect('/playwatch/homewatch/')
    return render(request, "playwatch/uploadvideo.htm")



def searchvideo(request):
    query = request.GET.get("query")
    movie = Movie.objects.all()
    qs = movie.filter(name__icontains=query)
    return render(request, 'playwatch/searchvideo.htm', {'movies': qs, "query": query})
