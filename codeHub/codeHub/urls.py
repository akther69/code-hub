"""
URL configuration for codeHub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from store import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/",views.SignUpView.as_view(),name="sign-up"),
    path("",views.SignInView.as_view(),name="sign-in"),
    path("index/",views.IndexView.as_view(),name="index"),
    path("profile/<int:pk>/change/",views.UserProfileUpdateView.as_view(),name="profile-update"),
    path("project/add/",views.ProjectCreateView.as_view(),name="project-add"),
    path("works/all/",views.MyProjectListView.as_view(),name="works-list"),
    path("work/<int:pk>/remove/",views.ProjectDeleteView.as_view(),name="work-delete"),
    path("project/<int:pk>/details/",views.ProjectDetailView.as_view(),name="project-details"),
    path("project/<int:pk>/wishlist/add/",views.AddToWishListView.as_view(),name="add-wishlist"),
    path("wishlist/cart/",views.MyCartItemView.as_view(),name="cart-items"),
    path("wishlistitem/<int:pk>/remove/",views.WishlistItemDeleteView.as_view(),name="cart_item-delete"),
    path("checkout/",views.CheckOutView.as_view(),name="checkout"),
    path("payment/verification/",views.PaymentVerificationView.as_view(),name="payment-verify"),
    path("myorder/",views.MyPurchaseView.as_view(),name="myorders"),
    path("project/<int:pk>/add/review/",views.ReviewCreateView.as_view(),name="review-add")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
