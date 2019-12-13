from django.shortcuts import render
import requests
import random
# Create your views here.
   
#    from django.http import HttpResponse


# print( 'asdbvsjbefefvrfvfv',  r.status_code)
# print("asfafav", r.json()["articles"][0]["author"])
# print("ascascvs",r.json() ["articles"][0] )

def index (request):
     return render (request, 'index.html')

def news_list(request):
     r=requests.get("https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=be768f4611de405c98aa56796254b69c")
     news_list = r.json()
     random_number = random.randint(0, 10)
     random_news = news_list['articles'][random_number]
     context= {'xeber':random_news}
     return render(request,'news_list.html',context)


