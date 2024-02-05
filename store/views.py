from django.shortcuts import render
from store.models import Movie
from store.forms import MovieForm

# Create your views here.
def home(request):
    movies = Movie.objects.all()
    return render(request,'home.html',{'movies': movies})

def addmovie(request):
    if(request.method=="POST"):  #after submission
        form=MovieForm(request.POST,request.FILES) #Creates form object initialised with values inside request.POST
        if form.is_valid():
            form.save() #saves the form object inside Db table
        return home(request)
    form=MovieForm()   #empty form object with no values
    return render(request, 'addmovie.html',{'form':form})


def update(request, p):
    movie = Movie.objects.get(id=p)
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()

    form = MovieForm(instance=movie)
    return render(request, 'update.html', {'form': form})

def delete(request, p):
    movie = Movie.objects.get(id=p)
    if request.method == "POST":
        movie.delete()
    return render(request, 'delete.html', {'movie': movie})

def viewmovie(request,p):
    # return HttpResponse("Welcome")
    k=Movie.objects.get(id=p)
    return render(request,'viewmovie.html',{'movie':k})