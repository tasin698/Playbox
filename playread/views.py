from django.shortcuts import render
from playread.models import Book, Readlater, Readhistory, Readchannel
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.db.models import Case, When

def homeread(request):
    book = Book.objects.all()[0:3]

    if request.user.is_authenticated:
        wl = Readlater.objects.filter(user=request.user)
        ids = []
        for i in wl:
            ids.append(i.read_novel_id)
        
        preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
        read = Book.objects.filter(book_id__in=ids).order_by(preserved) 
        read = reversed(read)
    
    else:
        read = Book.objects.all()[0:3]

    return render(request, 'playread/homeread.htm', {'book': book, 'read': read})


def readhistory(request):
    if request.method == "POST":
        user = request.user
        novel_id = request.POST['novel_id']
        readhistory = Readhistory(user=user, novel_id=novel_id)
        readhistory.save()

        return redirect(f"/playread/books/{novel_id}")

    readhistory = Readhistory.objects.filter(user=request.user)
    ids = []
    for i in readhistory:
        ids.append(i.novel_id)
    
    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
    book = Book.objects.filter(book_id__in=ids).order_by(preserved)

    return render(request, 'playread/readhistory.htm', {"readhistory": book})

def readlater(request):
    if request.method == "POST":
        user = request.user
        read_novel_id = request.POST['read_novel_id']

        read = Readlater.objects.filter(user=user)
        
        for i in read:
            if read_novel_id == i.read_novel_id:
                message = "Your Novel is Already Added"
                break
        else:
            readlater = Readlater(user=user, read_novel_id=read_novel_id)
            readlater.save()
            message = "Your Novel is Succesfully Added"

        book = Book.objects.filter(book_id=read_novel_id).first()
        return render(request, f"playread/bookpost.htm", {'book': book, "message": message})

    wl = Readlater.objects.filter(user=request.user)
    ids = []
    for i in wl:
        ids.append(i.read_novel_id)
    
    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
    book = Book.objects.filter(book_id__in=ids).order_by(preserved)

    return render(request, "playread/readlater.htm", {'book': book})


def removereadlater(request, id):
    if request.method == "GET":
        user = request.user
        read_novel_id = id
        read = Readlater.objects.filter(user=user, read_novel_id=read_novel_id)
        read.delete()
        return redirect('/playread/homeread/')







def books(request):
    book = Book.objects.all()
    return render(request, 'playread/books.htm', {'book': book})

def bookpost(request, id):
    book = Book.objects.filter(book_id=id).first()
    return render(request, 'playread/bookpost.htm', {'book': book})

def loginread(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            readchannel = Readchannel(name=username)
            readchannel.save()   
            redirect("/")

    return render(request, 'playread/loginread.htm')

def signup(request):
    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # if User.objects.filter(username=username).exists():
        #     messages.error(request, "Username is already taken. Please try another one !")
        #     return redirect("/")

        # if len(username) > 15:
        #     messages.error(request, "Username must be less than 15 characters")
        #     return redirect("/")
        
        # if not username.isalnum():
        #     messages.error(request, "Username should only contain Letters and Numbers.")

        # if pass1 != pass2:
        #     messages.error(request, "Password Do not Match. Please Sign Up Again")
        #     return redirect("/")


            
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = first_name
        myuser.last_name = last_name
        myuser.save()
        user = authenticate(username=username, password=pass1)
        from django.contrib.auth import login
        login(request, user)

        

        return redirect('/')

    return render(request, 'musicbeats/signup.htm')

def logout_user_read(request):
    logout(request)
    return redirect("/")

def channelread(request, readchannel):
    chan = Readchannel.objects.filter(name=readchannel).first()
    read_novel_ids = str(chan.novel).split(" ")[1:]

    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(read_novel_ids)])
    book = Book.objects.filter(book_id__in=read_novel_ids).order_by(preserved)
    

    return render(request, "playread/channelread.htm", {"channelread": chan, "book": book})

def uploadnovel(request):
    if request.method == "POST":
        name = request.POST['name']
        author = request.POST['author']
        tag = request.POST['tag']
        image = request.POST['image']
        description = request.POST['description']
        book1 = request.FILES['file']

        book_model = Book(name=name, author=author, tags=tag, image=image, description=description, book=book1)
        book_model.save()

        novel_id = book_model.book_id
        channelread_find = Readchannel.objects.filter(name=str(request.user))
        print(channelread_find)

        for i in channelread_find:
            i.novel += f" {novel_id}"
            i.save()

    return render(request, "playread/uploadnovel.htm")



def searchnovel(request):
    query = request.GET.get("query")
    book = Book.objects.all()
    qs = book.filter(name__icontains=query)
    return render(request, 'playread/searchnovel.htm', {'books': qs, "query": query})
