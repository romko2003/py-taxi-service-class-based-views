from django.shortcuts import render

from taxi.models import Driver, Car, Manufacturer
from django.views.generic import ListView
from django.views.generic import DetailView


class ManufacturerListView(ListView):
    model = Manufacturer
    queryset = Manufacturer.objects.order_by("name")
    paginate_by = 5


class CarListView(ListView):
    model = Car
    queryset = (Car.objects.select_related("manufacturer").
                prefetch_related("drivers"))
    paginate_by = 5


class CarDetailView(DetailView):
    model = Car


class DriverListView(ListView):
    model = Driver
    paginate_by = 5


class DriverDetailView(DetailView):
    model = Driver
    queryset = Driver.objects.prefetch_related("car_set__manufacturer")
