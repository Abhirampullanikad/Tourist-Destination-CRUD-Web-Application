from django.shortcuts import get_object_or_404, render

from tourist_app.forms import DestinationForm
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework import generics, permissions
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
import requests
from django.conf import settings
# Create your views here.


class DestinationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Destination.objects.all().order_by('-created_at')
    serializer_class = DestinationSerializer
    permission_classes = [AllowAny]
    
    
    
    
class DestinationDetail(generics.RetrieveAPIView):
    queryset=Destination.objects.all()
    serializer_class = DestinationSerializer
    
    
class DestinationUpdateView(generics.RetrieveUpdateAPIView):
    queryset=Destination.objects.all()
    serializer_class = DestinationSerializer
    
    
class DestinationDelete(generics.DestroyAPIView):
    queryset=Destination.objects.all()
    serializer_class = DestinationSerializer
    
    
    
class DestinationSearch(generics.ListAPIView):
    serializer_class = DestinationSerializer

    def get_queryset(self):
        name = self.kwargs.get('Name', '')
        return Destination.objects.filter(place_Name__icontains=name)
    


API_BASE_URL = 'http://localhost:8000/DestinationCreate/'

def destination_list(request):
    destinations = Destination.objects.all().order_by('-created_at')
    return render(request, 'destination_list.html', {'destinations': destinations})



def destination_detail(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    return render(request, 'destination_detail.html', {'destination': destination})


def destination_create(request):
    if request.method == 'POST':
        data = request.POST.dict()
        files = []
        
        if 'image' in request.FILES:
          files = {'image': request.FILES['image']}

        try:
            response = requests.post(
                API_BASE_URL,
                data=data,
                files=files
            )
            
            if response.status_code == 201:
                messages.success(request, 'Destination created successfully!')
                return redirect('destination_list')
            else:
                messages.error(request, f'Error creating destination: {response.json()}')
        except requests.exceptions.RequestException:
            messages.error(request, 'Failed to connect to the API server')
    
    return render(request, 'destination_create.html', {'title': 'Create Destination'})


def destination_update(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES, instance=destination)
        if form.is_valid():
            form.save()
            messages.success(request, 'Destination updated successfully.')
            return redirect('destination_detail', pk=pk)
    else:
        form = DestinationForm(instance=destination)
    return render(request, 'destination_form.html', {'form': form})

def destination_delete(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    if request.method == 'POST':
        destination.delete()
        messages.success(request, 'Destination deleted successfully.')
        return redirect('destination_list')
    return render(request, 'destination_confirm_delete.html', {'destination': destination})


def destination_search(request):
    query = request.GET.get('q', '')  # Get the search query from the URL (?q=something)
    results = Destination.objects.filter(place_Name__icontains=query) if query else []
    return render(request, 'destination_search.html', {'query': query, 'results': results})