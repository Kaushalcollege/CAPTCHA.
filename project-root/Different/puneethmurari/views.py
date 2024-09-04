from django.shortcuts import render
from django.http import JsonResponse
from .model_inference import make_prediction

def predict_view(request):
    if request.method == "POST":
        try:
            input_data = request.POST.dict()  # Get all POST parameters as a dictionary
            # Ensure the input_data is properly formatted for your model
            prediction = make_prediction(input_data)
            return JsonResponse({'prediction': prediction})
        except Exception as e:
            # Catch any errors and return an error response
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Only POST method is allowed'}, status=405)

def home(request):
    return render(request, 'UserBehavior/index1.html')
