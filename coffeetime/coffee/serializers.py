from rest_framework import serializers
from coffee.models import Coffee

# Coffee serializer 
class CoffeeSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Coffee
        fields = '__all__'