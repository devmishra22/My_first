from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import Albums
def index(request):
	all_albums= Albums.objects.all()
	
	context={
		'all_albums': all_albums,
	}
	return render(request,'music/index.html',context)

def detail(request,album_id):
	return HttpResponse("<h2>Details for album id :"+ str(album_id) +"</h2>")
