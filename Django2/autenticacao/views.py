from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def cadastro(request):
#     # return HttpResponse('Faça seu cadastro')
#     nome = 'Alisson José'
#     idade = '26'
#     profissao = 'Programador'
#     return render(request,'cadastro/index.html', {
#         'nome':nome, 
#         'idade':idade,
#         'profissao':profissao} )

def cadastro(request):
    pessoa = {
        'nome':'Alisson', 
        'idade':'26',
        'profissao':'programador'}
    return render(request,'cadastro/index.html',{'pessoa':pessoa} ) 

def auth(request):
    return HttpResponse('AUTH')