from django.shortcuts import render
from .models import Event,MessageForm,Image
from django.http import HttpResponseRedirect
from .forms import ContactForm

def Events(request):
    template="events.html"
    allevents=Event.objects.all()
    context={
        'events':allevents,
    }
    return render(request,template,context)

def Contact(request):
    template='contact.html'
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form=MessageForm()
    return render(request,template,{'form':form})
def Gallery(request):
    template='gallery.html'
    images=Image.objects.all()
    context={
      'allimages':images,
    }
    return  render(request,template,context)