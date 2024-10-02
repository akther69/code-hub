from django.shortcuts import render
# Create your views here.
from django.views.generic import View
#localhost:8000/helloworld
#method=get
class HelloWorldView(View):
    def get(self,request,*args, **kwargs):
        return render(request,"helloworld.html")
    
class GoodMorningView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"good_morning.html")

class GoodEveningView(View):
    def get(self,request,*args, **kwargs):
        return render(request,"good_evening.html")

class SelfIntroView(View):
    def get(self,request,*args, **kwargs):
        data={"name":"suhaib","course":"django","age":12,"gender":"male"}
        return render(request,"self_intro.html",data)
    
class VehicleDetailsView(View):
    def get(self,request,*args, **kwargs):
        data={'company':"Royal enfield","name":"metor350","Vehicle_no":"TN 43W1785","color":"brown"}
        return render(request,"vehicle_detail.html",data)
    
class MobileDetailsView(View):
    def get(self,request,*args, **kwargs):
        data={'company':"Sumsung","name":"galaxy s24 ultra","Ram":"4GB","Processor":"snapDragon"}
        return render(request,"mobile_detail.html",data)
    
class LaptopDetailsView(View):
    def get(self,request,*args, **kwargs):
        data={'company':"hp","name":"Envy360","Ram":"8GB","Processor":"inteli7"}
        return render(request,"Laptop_detail.html",data)
    
class WatchView(View):
    def get(self,request,*args, **kwargs):
        data={'company':"nothing","name":"nordwatch","Ram":"8GB","Price":"7000"}
        return render(request,"watch_detail.html",data)
    
class HeadphoneDetailsView(View):
    def get(self,request,*args, **kwargs):
        data={'company':"boat","name":"beat10","color":"red","Price":"25000"}
        return render(request,"headphone_detail.html",data)