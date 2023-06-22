from django.http import HttpResponse
from django.template import loader


conferences = [
   {
     "id" : "1",
     "names": "Gasana James",
     "phone": "078775557483",
     "email": "gasana@gmail.com",
     "date": "11.06.2023",
     "topics": "Gender based violance",
   },
     {
     "id" : "2",
     "names": "Kalisa Emmy",
     "phone": "072755483",
     "email": "kalisa@gmail.com",
     "date": "11.06.2023",
     "topics": "Future of Youth",
   },
     {
     "id" : "2",
     "names": "Uwase Anet",
    "phone": "0737654483",
     "email": "uwase@gmail.com",
     "date": "11.05.2023",
     "topics": "Artificial Intelligence",
   }
]

def ListView(request):
  template = loader.get_template('listConference.html')
  return HttpResponse(template.render())

def CreateView(request):
  template = loader.get_template('createConference.html')
  return HttpResponse(template.render())

def UpdateView(request):
  template = loader.get_template('updateConference.html')
  return HttpResponse(template.render())

def DeleteView(request):
  template = loader.get_template('deleteConference.html')
  return HttpResponse(template.render())

def DeleteConfirmView(request):
  template = loader.get_template('deleteConfirm.html')
  return HttpResponse(template.render())