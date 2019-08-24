from django.http import JsonResponse
from django.shortcuts import render
from django.core.serializers import serialize
# from django.forms.models import model_to_dict



from app.models import Task

# Create your views here.
def index(request):
    return render(request, 'index.html')

def add_task(request):
    task = Task.objects.create(
        name = request.GET['name'],
        detail = request.GET['detail'],
        toggle = request.GET['toggle']=='true',
    )
    print(request.GET)
    return JsonResponse({ 'ok': True })

def created(request):
    tasks = serialize('json', Task.objects.all())
    return JsonResponse(tasks, safe=False)

def rm_task(request):
    return JsonResponse({ 'ok': True })

def toggle_task(request):
    return JsonResponse({ 'ok': True })
