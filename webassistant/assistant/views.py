from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import TicketForm
from django.shortcuts import render, redirect
from .forms import TicketForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Ticket, Category

def index(request):
    if request.user.is_authenticated:
        return redirect("profile_ticket_list")
    else:
        return render(request,"index.html")



