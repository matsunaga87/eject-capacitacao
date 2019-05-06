from django.shortcuts import render , get_object_or_404

from .models import Curses

def index(request):
	curses = Curses.objects.all()
	template_name = 'curses/index.html'
	context = {
		'curses':curses,
	}
	return render(request, template_name, context)
# Create your views here.

#def details(request, pk):
#	curses = get_object_or_404( Curses, pk=pk)
#	context = {
#		'curses':curses
#	}
#	template_name = 'curses/details.html'
#	return render(request, template_name, context)

def details(request, slug):
	curses = get_object_or_404( Curses, slug=slug)
	context = {
		'curses':curses
	}
	template_name = 'curses/details.html'
	return render(request, template_name, context)
