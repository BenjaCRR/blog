from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import ComentarioForm

def inicio(request):
    return render(request, 'inicio.html')

def lista(request):
    return render(request, 'lista.html', {'posts': Post.objects.all()})

def detalle(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            c = form.save(commit=False)
            c.post = post
            c.save()
            return redirect('detalle', pk=pk)
    else:
        form = ComentarioForm()
    return render(request, 'detalle.html', {'post': post, 'form': form})