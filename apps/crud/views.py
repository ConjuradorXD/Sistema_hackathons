from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.http import require_POST
from .models import Item
from .forms import ItemForm

# Create your views here.
@login_required
def index(request):
    itens = Item.objects.all()
    return render(request, "index.html", {'itens':itens})


@login_required
def novo_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('novo_item_sucesso')
    else:
        form = ItemForm()
    return render(request, "novo-item.html",{
        'form':form,
    })


@login_required
def novo_item_sucesso(request):
    return render(request, "novo-item-sucesso.html")


@login_required
def alterar_item(request,codigo_item):
    item = get_object_or_404(Item, codigo_item=codigo_item)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ItemForm(instance=item)
    return render(request, 'alterar_dados.html',{
        'form':form,
        'item':item,
    })


@login_required
@require_POST
def excluir_item(request, codigo_item):
    item = get_object_or_404(Item, codigo_item=codigo_item)
    item.delete()
    return redirect('index')


@login_required
def buscar_item(request):
    query = request.GET.get('buscar','')
    itens = Item.objects.filter(nome_item__icontains=query)
    return render(request, 'index.html', {
        'itens':itens,
        'query':query
    })
