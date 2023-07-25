from django.shortcuts import render
from .models import *
from django.contrib import messages
from .producer import publish_sale

def app(request):
    branch = 'Ngaba'
    msg = Message.objects.filter(branch_name=branch)
    if request.method == 'POST':
        article = request.POST.get('article')
        quantity = int(request.POST.get('quantity'))
        if (article=='Chemise'):
            price = 10
            amount =  price * quantity
        elif (article=='Veste'):
            price = 350
            amount = price * quantity
        elif (article=='Chaussure'):
            price = 150
            amount = price * quantity
        sale = Sale(
            article=article,
            price=str(price),
            quantity=quantity,
            amount=amount,
            branch=branch,
        )
        sale.save()
        messages.success(request, 'Vente enregistrée avec succès')
        data = f"article: {article}, price: {price}, quantity: {quantity}, amount: {amount}, branch: {branch}"
        publish_sale(data)
    return render(request, 'app.html',{
        'branch':branch,
        'msg':msg
    })