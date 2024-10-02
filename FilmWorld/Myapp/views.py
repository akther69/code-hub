from django.shortcuts import render,redirect
from django.views.generic import View
# Create your views here.
from Myapp.models import Film
from django.contrib import messages
#employeelisting
#url:localhost:8000/employees/all/
# method :get
class FilmListView(View):
    def get(self,request,*args, **kwargs):
        
        # orm query for fetching of film records
        qs=Film.objects.all()
        return render(request,"film_list.html",{"films":qs})


class FilmCreateView(View):
    def get(self,request,*args, **kwargs):
        return render(request,"film_create.html")
    def post(self,request,*args, **kwargs):
        title_box=request.POST.get("titleBox")
        year_box=request.POST.get("yearBox")
        genre_box=request.POST.get("genreBox")
        director_box=request.POST.get("directorBox")
        tags_box=request.POST.get("tagsBox")
        song_count_box=request.POST.get("song_countBox")
        language_box=request.POST.get("languageBox")
        is_trending_box=request.POST.get("is_trendingBox")
        Film.objects.create(title=title_box,year=year_box,genre=genre_box,director=director_box,tags=tags_box,song_count=song_count_box,language=language_box,is_trending=is_trending_box)
        messages.success(request,"Film added successfully")
        return redirect("film-list")
    
class FilmDetailView(View):
    def get(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        qs=Film.objects.get(id=id)
        return render(request,"film_info.html",{"film":qs})
    
class FilmDeleteView(View):
    def get(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        Film.objects.get(id=id).delete()
        messages.success(request,"Deletion successfull")
        return redirect("film-list")


class FilmUpdateView(View):
    def get(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        flm_obj=Film.objects.get(id=id)
        return render(request,"film_edit.html",{"film":flm_obj})
    def post(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        Film.objects.filter(id=id).update(title=request.POST.get("title"),
                                          year=int(request.POST.get("year")),
                                          genre=request.POST.get("genre"),
                                          director=request.POST.get("director"),
                                          tags=request.POST.get("tags"),
                                          song_count=int(request.POST.get("song_count")),
                                          language=request.POST.get("language"),
                                          is_trending=request.POST.get("is_trending"))
        messages.success(request,"Updation successfull")
        return redirect("film-list")