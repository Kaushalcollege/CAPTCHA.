from django.shortcuts import render
from django.http import JsonResponse
from .model_inference import make_prediction

def predict_view(request):
    if request.method == "POST":
        input_data = request.POST.dict()  # Get all POST parameters
        prediction = make_prediction(input_data)
        return JsonResponse({'prediction': prediction})
    else:
        return JsonResponse({'error': 'Only POST method is allowed'}, status=405)

def home(request):
    return render(request, 'UserBehavior/index1.html')

