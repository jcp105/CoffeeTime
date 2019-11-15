from coffee.models import Coffee
from rest_framework import viewsets, permissions
from .serializers import CoffeeSerializer

# Coffee Serializer 
class CoffeeViewSet(viewsets.ModelViewSet):
    queryset = Coffee.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CoffeeSerializer 