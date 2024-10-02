from django.shortcuts import render,redirect

from django.views.generic import View,TemplateView,UpdateView,CreateView,DetailView,ListView,FormView

from store.forms import SignupForm,SignInForm,UserProfileForm,ProjectForm,ReviewForm

from django.contrib.auth import authenticate,login

from store.models import UserProfile,Project,WishListItems,OrderSummary,Reviews

from django.urls import reverse_lazy

from django.db.models import Sum

import razorpay

from decouple import config 

# it is used to secret the key

Key_id=config("Key_id")

Key_secret=config("Key_secret")



class SignUpView(View):
    
    def get(self,request,*args, **kwargs):
        
        form_instance=SignupForm()
        
        return render(request,"store/signup.html",{"form":form_instance})
    
    def post(self,request,*args, **kwargs):
        
        form_instance=SignupForm(request.POST)
        
        if form_instance.is_valid():
            
            form_instance.save()
            
            return redirect("sign-in")
        
        else:
            
            return render(request,"store/signup.html",{"form":form_instance})
        
class SignInView(View):
    
    def get(self,request,*args, **kwargs):
        
        form_instance=SignInForm()
        
        return render(request,"store/signin.html",{"form":form_instance})
    
    def post(self,request,*args, **kwargs):
        
        form_instance=SignInForm(request.POST)
        
        if form_instance.is_valid():
            
            data=form_instance.cleaned_data
            
            user_obj=authenticate(request,**data)
            
            if user_obj:
                
                login(request,user_obj)
                
                return redirect("index")
        
        return render(request,"store/signin.html",{"form":form_instance})
    
class IndexView(View):
    
    template_name="store/index.html"
    
    def get(self,request,*args, **kwargs):
        
        qs=Project.objects.all().exclude(owner=request.user)
        
        return render(request,self.template_name,{"projects":qs})
    
class UserProfileUpdateView(UpdateView):
    
    model=UserProfile
    
    form_class=UserProfileForm
    
    template_name="store/profile_edit.html"
    
    success_url=reverse_lazy("index")
    
class ProjectCreateView(CreateView):
    
    model=Project
    
    form_class=ProjectForm
    
    template_name="store/project_add.html"
    
    success_url=reverse_lazy("index")
    
    def form_valid(self,form):
        
        form.instance.owner=self.request.user
        
        return super().form_valid(form)
    
class MyProjectListView(View):
    
    def get(self,request,*args, **kwargs):
        
        qs=request.user.projects.all()
        
        return render(request,"store/Myprojects.html",{"works":qs})
    
class ProjectDeleteView(View):
    
    def get(self,request,*args, **kwargs):
        
        id=kwargs.get("pk")
        
        Project.objects.get(id=id).delete()
        
        return redirect("works-list")
        
        
class ProjectDetailView(DetailView):
    
    template_name="store/project_detail.html"
    
    context_object_name="project"
    
    model=Project
    
class AddToWishListView(View):
    
    def get(self,request,*args, **kwargs):
        
        id=kwargs.get("pk")
        
        project_obj=Project.objects.get(id=id)
        
        WishListItems.objects.create(wishlist_object=request.user.basket,
                                     project_object=project_obj)
        
        print("item as successfully added to wishlistitem")
        
        return redirect("index")
        

class MyCartItemView(View):
    
    def get(self,request,*args, **kwargs):
        
        qs=request.user.basket.basket_items.filter(is_order_placed=False)
        
        total=request.user.basket.wishlist_total
        
        return render(request,"store/cartitems.html",{"cartitems":qs,"total":total})
    
class WishlistItemDeleteView(View):
    
    def get(self,request,*args, **kwargs):
        
        id=kwargs.get("pk")
        
        WishListItems.objects.get(id=id).delete()
        
        return redirect("cart-items")
    
    
class CheckOutView(View):
    
    def get(self,request,*args, **kwargs):
    
        client = razorpay.Client(auth=(Key_id,Key_secret))
    
        amount= request.user.basket.wishlist_total*100

        data = { "amount": amount, "currency": "INR", "receipt": "order_rcptid_11" }
    
        payment = client.order.create(data=data)
        
        #create a order object
        
        cart_items=request.user.basket.basket_items.filter(is_order_placed=False)
        
        order_summary_obj=OrderSummary.objects.create(
            
            user_object=request.user,
            
            order_id=payment.get("id"),
            
            total=request.user.basket.wishlist_total
            
        )
        
        # order_summary_obj.project_objects.add(cart_items.values("project_object__id"))
        
        for ci in cart_items:
            
            order_summary_obj.project_objects.add(ci.project_object)
            
            order_summary_obj.save()
        
        # for ci in cart_items:
            
        #     ci.is_order_placed=True
            
        #     ci.save()
        
        context={
            "key":Key_id,
            "amount":data.get("amount"),
            "currency":data.get("currency"),
            "order_id":payment.get("id")
        }
    
        return render(request,"store/payment.html",context)
    
from django.views.decorators.csrf import csrf_exempt

from django.utils.decorators import method_decorator
    
@method_decorator(csrf_exempt,name="dispatch")

class PaymentVerificationView(View):
    
    def post(self,request,*args, **kwargs):   
        
        client = razorpay.Client(auth=(Key_id,Key_secret))
        
        user_summary_object=OrderSummary.objects.get(order_id=request.POST.get('razorpay_order_id'))
        
        login(request,user_summary_object.user_object)
        
        try:
            # doughtfull code
            
            client.utility.verify_payment_signature(request.POST)
            
            print("payment successfull")
            
            order_id=request.POST.get('razorpay_order_id')
            
            OrderSummary.objects.filter(order_id=order_id).update(is_paid=True)
            
            cart_items=request.user.basket.basket_items.filter(is_order_placed=False)
            
            for ci in cart_items:
            
                ci.is_order_placed=True
            
                ci.save()
            
        except:
            
            # handling code
            
            print("payment failed")
        # (request,"store/success.html")
        return redirect("index")
    
class MyPurchaseView(View):
    
    model=OrderSummary
    
    context_object_name="orders"
    
    def get(self,request,*args, **kwargs):
        
        qs=OrderSummary.objects.filter(user_object=request.user,
                                       is_paid=True).order_by('-created_date')
        
        return render(request,"store/myordersummary.html",{"orders":qs})
    

# url:lh:2000/project/<int:pk>/review/add/

class ReviewCreateView(FormView):
        
        template_name="store/review.html"
        
        form_class=ReviewForm
        
        model=Reviews
        
        def post(self,request,*args, **kwargs):
            
            form_instance=ReviewForm(request.POST)
            
            id=kwargs.get("pk")
            
            project_obj=Project.objects.get(id=id)
            
            if form_instance.is_valid():
                
                form_instance.instance.user_object=request.user
                
                form_instance.instance.project_object=project_obj
                
                form_instance.save()
                
                return redirect("myorders")
            else:
                
                return render(request,self.template_name,{"form":form_instance})
        
        