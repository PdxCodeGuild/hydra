from django.shortcuts import redirect, render 
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import journalEntry
from django.utils import timezone
# from .forms import EntryForm
# from capstone.journal_app.models import journalEntry
# Create your views here.

# Renders home page
def home(request):
    return render(request, 'home.html')

#  Renders about page - didn't use it
def about(request):
    return render(request, 'about.html')

# Renders the journal entry submit page
def journal(request):
    return render(request, 'journal.html')

#  Signup - creates a new user
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.save()
        return redirect("journal_app:signin")
    return render(request, 'signup.html')

# Signin - an already created user
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            firstname = user.first_name
            return render(request, "home.html", {'firstname': firstname})
        else:
            messages.error(request, "The Username or Password is incorrect!")
            return redirect('journal_app:signin')
    return render(request, "signin.html")

#  Log out
def signout(request):
    logout(request)
    # messages.success(request, "Logged out Successfully!")
    return redirect("journal_app:home")

# Add a trading journal entry, post to server
def add_entry(request):
    if request.method == 'GET':
        # form = EntryForm()
        return render(request, 'journal.html')
    elif request.method == 'POST':
        user = request.user
        symbol = request.POST['symbol']
        date = request.POST['date']
        result = request.POST['result']
        detail = request.POST['detail']
        img_link = request.POST['img_link']
        print(user, symbol, date, result, detail, img_link)
        journalEntry.objects.create(user=user, symbol=symbol, date=date, result=result, detail=detail, img_link=img_link)
        return redirect('journal_app:listing')

# Renders the listing page which contains all the trade journal entries
def listing(request):
    entry_items = journalEntry.objects.all()
    # user = request.user
    user_post = journalEntry.objects.filter(user=request.user)
    print(user_post)
    return render(request, 'listing.html', {'user_post': user_post}) 

# Renders the journal entry edit page - for a specific trade entry
def edit(request, id):
    entry_item = journalEntry.objects.get(id=id)
    print(entry_item.date)
    form_date = entry_item.date.strftime('%Y-%m-%d')
    print(form_date)
    return render(request, 'edit.html', {'entry_item': entry_item})

# Deletes a trade entry and then redirects to the trade journal
def delete(request, id):
    entry_item = journalEntry.objects.get(id=id)
    entry_item.delete()
    return redirect('journal_app:listing')

# Saves the journal entry after editing a trading journal entry
def save(request, id):
    entry = journalEntry.objects.get(id=id)
    entry.symbol = request.POST['symbol']
    entry.date = request.POST['date']
    entry.result = request.POST['result']
    entry.detail = request.POST['detail']
    entry.img_link = request.POST['img_link']
    entry.save()
    return redirect("journal_app:listing")

