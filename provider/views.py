from rest_framework import mixins, generics
from django.shortcuts import get_object_or_404


from .models import Provider
from .serializers import ProviderSerializer


# Create your views here.

class ProviderView(generics.ListCreateAPIView, mixins.CreateModelMixin):

	queryset = Provider.objects.all()
	serializer_class = ProviderSerializer


	def perform_create(self, serializer):
		serializer.save()



class SingleProviderView(generics.RetrieveUpdateDestroyAPIView):
	
	queryset = Provider.objects.all()
	serializer_class = ProviderSerializer