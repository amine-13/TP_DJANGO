from genericpath import exists
from posixpath import split
import this
from django.shortcuts import get_object_or_404, redirect, render

from tpproduit.models import Magasin
from tpproduit.models import Produit
from tpproduit.models import MagasinProfile
from tpproduit.form import *

def index(request, *args, **kwargs):
    template_name = 'index.html'

    context = {

    }
    
    return render(
        request=request,
        template_name=template_name,
        context=context
    )

def MagasinView(request, *args, **kwargs):
    template_name = 'magasin.html'

    magasins = Magasin.objects.all()


    context = {
        'magasins':magasins,
    }
    
    return render(
        request=request,
        template_name=template_name,
        context=context
    )

def addMagasin(request, *args, **kwargs):
    template_name = 'add_magasin.html'
    
    obj = Magasin()

    if request.method == 'GET':
        form = MagasinForm()
        context = {
            'form': form
        }
            
        return render(
            request=request,
            template_name=template_name,
            context=context
        )
        
    if request.method == 'POST':
        form = MagasinForm(request.POST, request.FILES)
        context = {
            'form': form
        }
        if form.is_valid():
            print(form.cleaned_data)
            obj.name = form.cleaned_data.get('name')
            obj.country = form.cleaned_data.get('country')
            obj.created_at = form.cleaned_data.get('created_at')
            obj.updated_at = form.cleaned_data.get('updated_at')
            obj.save()
            redirect('index')
        return render(
    
        request=request,
            template_name=template_name,
            context=context
        )

def update_magasin(request, *args, **kwargs):
        template_name = 'update_magasin.html'
        obj = get_object_or_404(
            Magasin,
            pk=kwargs.get('pk')
        )

        if request.method == 'GET':
            form = MagasinForm(
                initial={
                    'name':obj.name,
                    'country':obj.country,
                    'created_at':obj.created_at,
                    'updated_at':obj.updated_at,
                }
            )
            context = {
                'form': form
            }
            return render(
                request=request,
                template_name=template_name,
                context=context
            )
        
        if request.method == 'POST':
            form = MagasinForm(
                request.POST,
                request.FILES,
                initial={
                    'name':obj.name,
                    'country':obj.country,
                    'created_at':obj.created_at,
                    'updated_at':obj.updated_at,
                }
            )
            context = {
                'form': form
            }
            if form.is_valid():
                print(form.cleaned_data)
                obj.name = form.cleaned_data.get('name')
                obj.country = form.cleaned_data.get('country')
                obj.created_at = form.cleaned_data.get('created_at')
                obj.updated_at = form.cleaned_data.get('updated_at')
                obj.save()
                redirect('index')
            return render(
                request=request,
                template_name=template_name,
                context=context
            )

def MagasinProfilView(request, *args, **kwargs):
    template_name = 'profil_magasin.html'
    
    obj = get_object_or_404(
            Magasin,
            pk=kwargs.get('pk')
        )
    
    objp = MagasinProfile()

    magasin= Magasin.objects.filter(id=obj.id)

    magasinProfile= MagasinProfile.objects.filter(magasin_id=obj.id)

    # len = magasin.values().get()['created_at']

    len = magasinProfile.__len__

    if magasinProfile:
        idmagp = magasinProfile.values().get()['id']
    else:
        idmagp = ''

    idmag = kwargs.get('pk')

    if request.method == 'GET':
        form = ajoutProfil()
        
    if request.method == 'POST':
        form = ajoutProfil(request.POST, request.FILES)

        if form.is_valid():
            print(form.cleaned_data)
            objp.email = form.cleaned_data.get('email')
            objp.phone = form.cleaned_data.get('phone')
            objp.created_at = magasin.values().get()['created_at']
            objp.updated_at = magasin.values().get()['updated_at']
            objp.magasin_id = magasin.values().get()['id']
            objp.save()
            redirect('index')
        
    context = {
        'len':len,
        'magasin':magasin,
        'magasinp':magasinProfile,
        'form':form,
        'idmag':idmag,
        'idmagp': idmagp
    }
    
    return render(
        request=request,
        template_name=template_name,
        context=context
    )

def update_magasin_profil(request, *args, **kwargs):
        template_name = 'update_profile_magasin.html'
        
        obj = get_object_or_404(
            MagasinProfile,
            pk=kwargs.get('pk')
        )

        if request.method == 'GET':
            form = ajoutProfil(
                initial={
                    'email':obj.email,
                    'phone':obj.phone,
                }
            )
            context = {
                'form': form
            }
            return render(
                request=request,
                template_name=template_name,
                context=context
            )
        
        if request.method == 'POST':
            form = ajoutProfil(
                request.POST,
                request.FILES,
                initial={
                    'email':obj.email,
                    'phone':obj.phone,
                }
            )
            context = {
                'form': form
            }
            if form.is_valid():
                print(form.cleaned_data)
                obj.phone = form.cleaned_data.get('phone')
                obj.email = form.cleaned_data.get('email')
                obj.save()
                redirect('index')
            return render(
                request=request,
                template_name=template_name,
                context=context
            )

def addMagasin(request, *args, **kwargs):
    template_name = 'add_magasin.html'
    
    obj = Magasin()

    if request.method == 'GET':
        form = MagasinForm()
        context = {
            'form': form
        }
            
        return render(
            request=request,
            template_name=template_name,
            context=context
        )
        
    if request.method == 'POST':
        form = MagasinForm(request.POST, request.FILES)
        context = {
            'form': form
        }
        if form.is_valid():
            print(form.cleaned_data)
            obj.name = form.cleaned_data.get('name')
            obj.country = form.cleaned_data.get('country')
            obj.created_at = form.cleaned_data.get('created_at')
            obj.updated_at = form.cleaned_data.get('updated_at')
            obj.save()
            redirect('index')
        return render(
    
        request=request,
            template_name=template_name,
            context=context
        )

def ProduitView(request, *args, **kwargs):
    template_name = 'produit.html'

    produits = Produit.objects.all()

    context = {
        'produits':produits,
    }
    
    return render(
        request=request,
        template_name=template_name,
        context=context
    )

def addProduit(request, *args, **kwargs):
    template_name = 'add_produit.html'
    
    obj = Produit()

    if request.method == 'GET':
        form = ProduitForm()
        context = {
            'form': form
        }
            
        return render(
            request=request,
            template_name=template_name,
            context=context
        )
        
    if request.method == 'POST':
        form = ProduitForm(request.POST, request.FILES)
        context = {
            'form': form
        }
        if form.is_valid():
            print(form.cleaned_data)
            obj.name = form.cleaned_data.get('name')
            obj.country = form.cleaned_data.get('country')
            obj.created_at = form.cleaned_data.get('created_at')
            obj.updated_at = form.cleaned_data.get('updated_at')
            obj.price = form.cleaned_data.get('price')
            obj.magasin_id = form.cleaned_data.get('magasin_id')
            obj.save()
            redirect('index')
        return render(
    
        request=request,
            template_name=template_name,
            context=context
        )

def update_produit(request, *args, **kwargs):
        template_name = 'update_produit.html'
        obj = get_object_or_404(
            Produit,
            pk=kwargs.get('pk')
        )

        if request.method == 'GET':
            form = ProduitForm(
                initial={
                    'name':obj.name,
                    'country':obj.country,
                    'created_at':obj.created_at,
                    'updated_at':obj.updated_at,
                    'price':obj.price,
                    'magasin_id':obj.magasin_id,
                }
            )
            context = {
                'form': form
            }
            return render(
                request=request,
                template_name=template_name,
                context=context
            )
        
        if request.method == 'POST':
            form = ProduitForm(
                request.POST,
                request.FILES,
                initial={
                    'name':obj.name,
                    'country':obj.country,
                    'created_at':obj.created_at,
                    'updated_at':obj.updated_at,
                    'price':obj.price,
                    'magasin_id':obj.magasin_id,
                }
            )
            context = {
                'form': form
            }
            if form.is_valid():
                print(form.cleaned_data)
                obj.name = form.cleaned_data.get('name')
                obj.country = form.cleaned_data.get('country')
                obj.created_at = form.cleaned_data.get('created_at')
                obj.updated_at = form.cleaned_data.get('updated_at')
                obj.price = form.cleaned_data.get('price')
                obj.magasin_id = form.cleaned_data.get('magasin_id')
                obj.save()
                redirect('index')
            return render(
                request=request,
                template_name=template_name,
                context=context
            )