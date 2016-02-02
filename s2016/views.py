from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from s2016.models import Doctor
from s2016.serializers import DoctorSerializer

def index(request):
  return HttpResponse("Hello, world")

class JSONResponse(HttpResponse):
  '''
  An HttpResponse that renders its content into JSON.
  '''

  def __init__(self, data, **kwargs):
    content = JSONRenderer().render(data)
    kwargs['content_type'] = 'application/json'
    super(JSONResponse, self).__init__(content, **kwargs)

  def doctor_list(request):
    '''
    List all doctors, or create a new doctor
    '''
   
    if request.method == 'GET':
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':







