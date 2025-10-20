#will need to install rest_framework package on your own system
from rest_framework import serializers
from .models import BooksModel

class BooksModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksModel
        fields = '__all__'  #can put fields as all or specify each field