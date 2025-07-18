from rest_framework import generics
from actors.models import Actor
from actors.serializers import ActorSerializer  


class ActorCreateListView(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    lookup_field = 'name'  # Assuming you want to use 'id' as the lookup field