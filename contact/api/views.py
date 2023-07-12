from rest_framework import generics
from .serializers import ContactSerializer, SubscribeSerializer
from ..models import Contact, Subscribe


class ContactListCreateAPIVIew(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class SubscribeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer
