from django.http import HttpResponse

def view_b(request):
  if request.method == 'GET':
    print('THIS IS GET')
  elif request.method == 'POST':
    print('THIS IS POST')

  return HttpResponse('Hello World')