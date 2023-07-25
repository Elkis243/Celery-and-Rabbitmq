from django.shortcuts import render
from .models import Sale 
from django.db.models import Sum
from .producer import publish_message

def app(request):
    branch = 'Direction générale'
    if request.method == 'POST':
        branch_name = request.POST.get('branch_name')
        message = request.POST.get('message')
        data = f"branch_name: {branch_name}, message: {message}"
        publish_message(data)
    return render(request, 'app.html',{
        'branch':branch,
        'stock_shirt_lingwala': Sale.objects.filter(article='Chemise', branch='Lingwala').aggregate(Sum('quantity'))['quantity__sum'],
        'amount_shirt_lingwala': Sale.objects.filter(article='Chemise', branch='Lingwala').aggregate(Sum('amount'))['amount__sum'],
        'stock_jacket_lingwala': Sale.objects.filter(article='Veste', branch='Lingwala').aggregate(Sum('quantity'))['quantity__sum'],
        'amount_jacket_lingwala': Sale.objects.filter(article='Veste', branch='Lingwala').aggregate(Sum('amount'))['amount__sum'],
        'stock_shoe_lingwala': Sale.objects.filter(article='Chaussure', branch='Lingwala').aggregate(Sum('quantity'))['quantity__sum'],
        'amount_shoe_lingwala': Sale.objects.filter(article='Chaussure', branch='Lingwala').aggregate(Sum('amount'))['amount__sum'],
        'stock_lingwala': Sale.objects.filter(branch='Lingwala').aggregate(Sum('quantity'))['quantity__sum'],
        'total_lingwala': Sale.objects.filter(branch='Lingwala').aggregate(Sum('amount'))['amount__sum'],
        'stock_shirt_masina': Sale.objects.filter(article='Chemise', branch='Masina').aggregate(Sum('quantity'))['quantity__sum'],
        'amount_shirt_masina': Sale.objects.filter(article='Chemise', branch='Masina').aggregate(Sum('amount'))['amount__sum'],
        'stock_jacket_masina': Sale.objects.filter(article='Veste', branch='Masina').aggregate(Sum('quantity'))['quantity__sum'],
        'amount_jacket_masina': Sale.objects.filter(article='Veste', branch='Masina').aggregate(Sum('amount'))['amount__sum'],
        'stock_shoe_masina': Sale.objects.filter(article='Chaussure', branch='Masina').aggregate(Sum('quantity'))['quantity__sum'],
        'amount_shoe_masina': Sale.objects.filter(article='Chaussure', branch='Masina').aggregate(Sum('amount'))['amount__sum'],
        'stock_masina': Sale.objects.filter(branch='Masina').aggregate(Sum('quantity'))['quantity__sum'],
        'total_masina': Sale.objects.filter(branch='Masina').aggregate(Sum('amount'))['amount__sum'],
        'stock_shirt_ngaba': Sale.objects.filter(article='Chemise', branch='Ngaba').aggregate(Sum('quantity'))['quantity__sum'],
        'amount_shirt_ngaba': Sale.objects.filter(article='Chemise', branch='Ngaba').aggregate(Sum('amount'))['amount__sum'],
        'stock_jacket_ngaba': Sale.objects.filter(article='Veste', branch='Ngaba').aggregate(Sum('quantity'))['quantity__sum'],
        'amount_jacket_ngaba': Sale.objects.filter(article='Veste', branch='Ngaba').aggregate(Sum('amount'))['amount__sum'],
        'stock_shoe_ngaba': Sale.objects.filter(article='Chaussure', branch='Ngaba').aggregate(Sum('quantity'))['quantity__sum'],
        'amount_shoe_ngaba': Sale.objects.filter(article='Chaussure', branch='Ngaba').aggregate(Sum('amount'))['amount__sum'],
        'stock_ngaba': Sale.objects.filter(branch='Ngaba').aggregate(Sum('quantity'))['quantity__sum'],
        'total_ngaba': Sale.objects.filter(branch='Ngaba').aggregate(Sum('amount'))['amount__sum'],
        'stock': Sale.objects.all().aggregate(Sum('quantity'))['quantity__sum'],
        'amount': Sale.objects.all().aggregate(Sum('amount'))['amount__sum'],
    })