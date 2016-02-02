from rest_framework import serializers
from s2016.models import Doctor, LANGUAGE_CHOICES, STYLE_CHOICES

class DoctorSerializer(serializers.Serializer):
  pk = serializers.IntegerField(read_only=True)
  name = serializers.CharField(max_length=100)
  education = serializers.CharField(max_length=100)
  specialty = serializers.CharField(max_length=100)
  is_active = serializers.BooleanField(required=True)

  def create(self, validated_data):
    '''
    Create and return a new Doctor data
    '''
    return Doctor.objects.create(**validated_data)

  def update(self, instance, validated_data):
    '''
    Update and return existing 'Doctor' instance
    '''

    instance.name = validated_data.get('name', instance.name)
    instance.education = validated_data.get('education', instance.education)
    instance.specialty = validated_data.get('specialty', instance.name)
    instance.is_active = validated_data.get('is_active', instance.is_active)
    instance.save()
    return instance
   
