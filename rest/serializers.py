from .model import Person
from rest_framework import serializers

class PersonSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Person
		fields = ('nombres','momento')
		