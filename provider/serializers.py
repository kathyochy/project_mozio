from rest_framework import serializers


from .models import Provider



class ProviderSerializer(serializers.ModelSerializer):

	class Meta:
		model = Provider
		fields = ('name', 'email', 'phone', 'language', 'currency')