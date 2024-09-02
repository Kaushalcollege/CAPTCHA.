from rest_framework.response import Response
from rest_framework.views import APIView
from .models import MouseMove, KeyPress, Click
from rest_framework import status
from django.shortcuts import render
from django.http import JsonResponse
from .model_inference import predict_user_behavior


def predict_view(request):
    if request.method == 'POST':
        # Extract data from the POST request
        data = request.POST.get('data')
        data = [float(x) for x in data.split(',')]  # Convert the data to a list of floats

        # Use the model to make a prediction
        prediction = predict_user_behavior(data)

        # Return the prediction as a JSON response
        return JsonResponse({'prediction': prediction.tolist()})

    return JsonResponse({'error': 'Only POST requests are allowed.'})


def home(request):
    return render(request, 'UserBehavior/index1.html')

class MouseMoveCreateView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        required_fields = ['x', 'y', 'timestamp']

        if not all(field in data for field in required_fields):
            return Response({"error": "Missing required fields"}, status=status.HTTP_400_BAD_REQUEST)

        mouse_move = MouseMove(x=data['x'], y=data['y'], timestamp=data['timestamp'])
        try:
            mouse_move.save()
            return Response({"status": "Mouse move recorded"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class KeyPressCreateView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        required_fields = ['key', 'typingSpeed', 'timestamp']

        if not all(field in data for field in required_fields):
            return Response({"error": "Missing required fields"}, status=status.HTTP_400_BAD_REQUEST)

        key_press = KeyPress(key=data['key'], typing_speed=data['typingSpeed'], timestamp=data['timestamp'])
        try:
            key_press.save()
            return Response({"status": "Key press recorded"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ClickCreateView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        required_fields = ['x', 'y', 'timestamp']

        if not all(field in data for field in required_fields):
            return Response({"error": "Missing required fields"}, status=status.HTTP_400_BAD_REQUEST)

        click = Click(x=data['x'], y=data['y'], timestamp=data['timestamp'])
        try:
            click.save()
            return Response({"status": "Click recorded"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#