from actors.models import Actor
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from actors.serializers import ActorSerializer
from app.permissions import GlobalDefaultPermission


class ActorListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (
        IsAuthenticated,
        GlobalDefaultPermission,
    )
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (
        IsAuthenticated,
        GlobalDefaultPermission,
    )
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
