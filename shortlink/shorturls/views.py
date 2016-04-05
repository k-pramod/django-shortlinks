from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Shortlink
from .forms import ShortlinkForm

from django.views.decorators.http import require_http_methods
# Create your views here.

import hashlib

def home(request):
    return HttpResponse("Welcome shortening site!")

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ShortlinkForm(request.POST)
        if form.is_valid():
            long_url = form.cleaned_data['long_url']
            short_id = get_md5(long_url, 4)
            new_shortlink = Shortlink(long_url=long_url, short_id=short_id)
            new_shortlink.save()
            return render(request, 'create.html', {'new_shortlink': new_shortlink})
    else:
        form = ShortlinkForm()
    return render(request, 'create.html', {'form': form})

def match(request, pattern):
    try:
        shortlink = Shortlink.objects.filter(short_id=pattern.lower())[0]
    except Shortlink.DoesNotExist:
        return HttpResponse("Cannot find pattern! :) Try again.")
    return HttpResponseRedirect(shortlink.long_url)

def get_md5(string, length):
    encoded_string = string.encode(encoding='UTF-8', errors='strict')
    hashed = hashlib.md5(encoded_string).hexdigest()
    return hashed[0:length]
