from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Message
from django.urls import reverse
from .forms import MessageForm

@login_required
def sent_messages(request):
    messages = Message.objects.filter(sender=request.user)
    return render(request, 'messaging/sent_messages.html', {'messages': messages})

@login_required
def inbox(request):
    msgs = Message.objects.filter(recipient=request.user)
    return render(request, 'messaging/inbox.html', {'messages_list': msgs})

@login_required
def sent(request):
    msgs = Message.objects.filter(sender=request.user)
    return render(request, 'messaging/sent.html', {'messages_list': msgs})

@login_required
def compose(request):
    form = MessageForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        msg = form.save(commit=False)
        msg.sender = request.user
        msg.save()
        messages.success(request, 'Mensaje enviado.')
        return redirect('messaging:sent')
    return render(request, 'messaging/compose.html', {'form': form})

@login_required
def compose(request):
    # Creamos el formulario, con datos POST si vienen
    form = MessageForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            # Guardamos pero asignando el usuario actual como remitente
            msg = form.save(commit=False)
            msg.sender = request.user
            msg.save()

            messages.success(request, "Mensaje enviado.")
            # Redirige a la bandeja de enviados para evitar recarga en blanco
            return redirect(reverse('messaging:sent'))
        else:
            messages.error(request, "Revisá el formulario antes de enviar.")

    return render(request, 'messaging/compose.html', {'form': form})

@login_required
def detail(request, pk):
    msg = get_object_or_404(Message, pk=pk)
    # Permitir ver solo si sos remitente o destinatario
    if msg.sender != request.user and msg.recipient != request.user:
        messages.error(request, "No tenés permiso para ver este mensaje.")
        return redirect('messaging:inbox')
    # Marcar como leído si corresponde
    if msg.recipient == request.user and not msg.is_read:
        msg.is_read = True
        msg.save()
    return render(request, 'messaging/detail.html', {'message': msg})

