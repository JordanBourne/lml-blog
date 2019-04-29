from django.http import HttpResponse
from django.views import View
from api.models import Topic
import json

class View_A(View):
  def get(self, request):
    all_topics = Topic.objects.all()
    # use serpy to serialize the object into json?
    return HttpResponse(all_topics)

  def post(self, request):
    body = json.loads(request.body)
    new_topic = Topic(subject = body['subject'])
    new_topic.save()

    return HttpResponse('success')