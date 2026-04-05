from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Studio
from .serializers import StudioSerializer

class StudioListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Studio.objects.all()
    serializer_class = StudioSerializer

class StudioRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Studio.objects.all()
    serializer_class = StudioSerializer
