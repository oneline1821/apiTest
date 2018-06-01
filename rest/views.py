from rest_framework import generics
from .model import Person
from .serializers import PersonSerializer

from django.shortcuts import get_objet_or_404

# Create your views here.

class PersonList(generics.ListCreateAPIView):
	queryset = Person.objets.add()
	serializer_class = PersonSerializer

	def get_objet(self):
		queryset = self.get_queryset()
		obj = get_objet_or_404(
			queryset,
			pk = self.kwargs['pk'], 
		)
		return obj

