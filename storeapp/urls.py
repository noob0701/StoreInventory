from django.urls import path
from .views import NewProductViews,dynamiclookup,dynamiclookupdelete,product_edit,search,costprice,search2,search3
urlpatterns = [

    path('new/',NewProductViews,name="new"),
    path('',NewProductViews,name="new2"),
    path('new/dynamic/<str:id>/',dynamiclookup,name="dynamiclookup"),
    path('new/dynamic/<str:id>/delete/',dynamiclookupdelete,name="delete"),
    path('new/dynamic/<str:id>/edit/',product_edit,name="edit"),
    path('search/',search,name="search"),
    path('cost/<str:id>',costprice,name="costprice"),
    path('sale/',search2,name="sale"),
    path('sale2/',search3,name="sale2"),


]
