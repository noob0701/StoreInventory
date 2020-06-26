from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from .models import *
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.contrib import messages
from django.db.models import Q,Sum
from django.core import serializers
import json
# Create your views here.


def NewProductViews(request):
    if request.method == 'POST':
        form = NewProductForm(request.POST)
        if form.is_valid():
            ProductName = request.POST.get("ProductName", '')
            Barcode = request.POST.get("Barcode", '')
            CostPrice = request.POST.get("CostPrice", '')
            SellingPrice = request.POST.get("SellingPrice", '')
            QuantityAvilable = request.POST.get("QuantityAvilable", '')
            pro = Products(ProductName=ProductName, Barcode=Barcode,
                           CostPrice=CostPrice, SellingPrice=SellingPrice, QuantityAvilable=QuantityAvilable)
            pro.save()
            form = NewProductForm()
            context = {'form': form}
            product = Products.objects.all()
            total=Products.objects.aggregate(sum=Sum('total'))['sum']
            context = {'form': form, 'product': product,'total':total}
            return render(request, "storeapp/newproduct.html", context)
        else:
            form = NewProductForm()
            product = Products.objects.all()
            total=Products.objects.aggregate(sum=Sum('total'))['sum']
            context = {'form': form, 'product': product,'total':total}
            return render(request, "storeapp/newproduct.html", context)
    else:
        form = NewProductForm()
        product = Products.objects.all()
        total=Products.objects.aggregate(sum=Sum('total'))['sum']
        context = {'form': form, 'product': product,'total':total}
        return render(request, "storeapp/newproduct.html", context)


def dynamiclookup(request, id):
    obj = Products.objects.get(Barcode=id)
    context = {
        "object": obj

    }
    return render(request, "storeapp/dynamic.html", context)


def dynamiclookupdelete(request, id):
    obj = get_object_or_404(Products, Barcode=id)
    if request.method == "POST":
        obj.delete()
        return redirect("new")
    context = {
        "object": obj

    }
    return render(request, "storeapp/productdelete.html", context)


def product_edit(request,id):
    post = get_object_or_404(Products,Barcode = id)
    if request.method == "POST":
        form = EditForm(request.POST or None,instance=post)
        if form.is_valid():
            form.save()
        form1 = NewProductForm()
        product = Products.objects.all()
        context = {'form1': form1, 'product': product}
        return redirect(NewProductViews)


    else:
        form = EditForm(instance=post)

    context = {
        "form": form,
        "post": post,
    }
    return render(request,"storeapp/editproduct.html",context)


def search(request):
    if request.method=="POST":
        srch = request.POST["srh"]

        if srch:
            match = Products.objects.filter(Q(Barcode__iexact=srch))
            if match:
                
                return render(request,"storeapp/search.html", {"sr":match})
            else:
                messages.error(request,"No Product Found")
        else:
            return HttpResponseRedirect("/search/")
    return render(request,"storeapp/search.html")

def costprice(request,id):
    post = get_object_or_404(Products,Barcode = id)
    costtotal = post.CostPrice * post.QuantityAvilable
    print(costtotal)
    return HttpResponse(costtotal)


def search2(request):
    if request.method=="GET":
        srch = request.GET["srh"]

        if srch:
            match = Products.objects.filter(Q(Barcode__iexact=srch))
            if match:

                qs_json = serializers.serialize('json', match)
                return HttpResponse(qs_json, content_type='application/json')
            else:
                messages.error(request,"No Product Found")
        else:
            return HttpResponse("string")
    return HttpResponse("Not Found")


def search3(request):
    return render(request,"storeapp/sales.html")