from rest_framework import serializers
from .models import MouseMove, KeyPress, Click

class MouseMoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = MouseMove
        fields = '__all__'

class KeyPressSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyPress
        fields = '__all__'

class ClickSerializer(serializers.ModelSerializer):
    class Meta:
        model = Click
        fields = '__all__'
