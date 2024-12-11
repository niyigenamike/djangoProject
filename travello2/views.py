from django.shortcuts import render
from django.http import HttpResponse
from .models  import Destination
# Create your views here.
def index(request):

    dest1 = Destination()
    dest1.name = "Mike"
    dest1.desc = "This is the best car owner in africa and in austarria"
    dest1.price = 10000000
    dest1.img = "fc3.png"
    dest1.offer = False

    dest2 = Destination()
    dest2.name = "Debie"
    dest2.desc = "The best fried in life"
    dest2.price = 6000000
    dest2.img = "fc2.png"
    dest2.offer = False


    dest3 = Destination()
    dest3.name = "Christian"
    dest3.desc = "This is the best Accountant in africa and in austarria"
    dest3.price = 4000000
    dest3.img = "fc1.png"
    dest3.offer = True


    dest4 = Destination()
    dest4.name = "Verra"
    dest4.desc = "This is the Most women  in africa and in austarria"
    dest4.price = 1000000
    dest4.img = "fc4.png"
    dest4.offer = True


    dests = [dest1, dest2,dest3,dest4]

    return render(request,'index.html',{'dests':dests})
