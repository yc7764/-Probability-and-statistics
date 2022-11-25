from django.shortcuts import render
from topics.models import Topic
# Create your views here.
def index(request):

    topics = Topic.objects.all()

    context = {
        'topics': topics
    }
    return render(request, "index.html", context)