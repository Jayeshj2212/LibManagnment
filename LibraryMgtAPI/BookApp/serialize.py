from dataclasses import fields
from rest_framework import serializers
from BookApp.models import DetailsBook


class DetailsSerializer(serializers.ModelSerializer):
    # modelSerializer class helps to create serialize class fields corresponding 
    # to model feildsIt will automatically generate a set of fields for you, 
    # based on the model. It will automatically generate validators for 
    # the serializer, such as unique_together validators.
    # It includes simple default implementations of .create() and .update()
    class Meta:
        model = DetailsBook
        fields = "__all__"
