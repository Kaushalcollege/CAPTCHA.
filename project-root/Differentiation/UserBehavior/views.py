from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.dateparse import parse_datetime
import json
from .models import MouseMove, KeyPress, Click
from django.shortcuts import render

@csrf_exempt
def mouse_moves(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        mouse_move = MouseMove(x=data['x'], y=data['y'], timestamp=parse_datetime(data['timestamp']))
        mouse_move.save()
        return JsonResponse({'status': 'success'})

@csrf_exempt
def key_presses(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        key_press = KeyPress(key=data['key'], typing_speed=data['typingSpeed'], timestamp=parse_datetime(data['timestamp']))
        key_press.save()
        return JsonResponse({'status': 'success'})

@csrf_exempt
def clicks(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        click = Click(x=data['x'], y=data['y'], timestamp=parse_datetime(data['timestamp']))
        click.save()
        return JsonResponse({'status': 'success'})



def index(request):
    return render(request, 'index.html')
