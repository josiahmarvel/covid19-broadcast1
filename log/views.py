from django.shortcuts import render

# Create your views here.

from log.models import Speech, Speaker, SpeechInstance

from django.views import generic


def index(request):
    
    

    
    num_speeches = Speech.objects.all().count()
    num_instances = SpeechInstance.objects.all().count()

    
    

    
    num_speakers = Speaker.objects.count()

    context = {
        'num_speeches': num_speeches,
        
        'num_speakers': num_speakers,
    }

    
    return render(request, 'index.html', context=context)


class SpeechListView(generic.ListView):
    model = Speech
    paginate_by = 5



class SpeakerListView(generic.ListView):
    model = Speaker
    paginate_by = 5


class SpeechDetailView(generic.DetailView):
    model = Speech



class SpeakerDetailView(generic.DetailView):
    model = Speaker

