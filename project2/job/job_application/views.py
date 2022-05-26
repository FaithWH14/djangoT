from tokenize import Token
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import jobApplication
from .forms import jobAppliedForm

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import jobAppliedSerializer

# Create your views here.

class AppliedObjectMixin(object):
    model = jobApplication
    
    def get_object(self):
        id = self.kwargs.get("id")
        obj = None
        if id is not None:
            obj = get_object_or_404(self.model, id = id)
        return obj

class jobApplicationList(View):
    template_name = "jobAppliedList.html"

    def get(self, request, *args, **kwargs):
        queryset = jobApplication.objects.all()
        context = {
            "objects": queryset
        }
        return render(request, self.template_name, context)

class jobApplicationCreate(View):
    template_name = "jobAppliedCreate.html"

    def get(self, request, *args, **kwargs):
        form = jobAppliedForm()
        context = {
            "form": form
        }
        return render(request, self.template_name, context)


    def post(self, request, *args, **kwargs):
        form = jobAppliedForm(request.POST)
        if form.is_valid():
            form.save()
            form = jobAppliedForm()
        context = {
            "form": form
        }
        return render(request, self.template_name, context)

class jobApplicationView(AppliedObjectMixin, View):
    template_name = "jobAppliedView.html"

    def get(self, request, id = None, *args, **kwargs):
        context = {
        "object": self.get_object()
    }   
        return render(request, self.template_name, context)
            
class jobApplicationUpdate(AppliedObjectMixin, View):
    template_name = "jobAppliedUpdate.html"

    def get(self, request, id = None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = jobAppliedForm(instance = obj)
            context["object"] = obj
            context["form"] = form
        return render(request, self.template_name, context)
    
    def post(self, request, id = None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = jobAppliedForm(request.POST, instance = obj)
        if form.is_valid():
            form.save()
            return redirect("../../..")
        context["object"] = obj
        context["form"] = form
        return render(request, self.template_name, context)

class jobApplicationDelete(AppliedObjectMixin, View):
    template_name = "jobAppliedDelete.html"

    def get(self, request, id = None, *args, **kwargs):
        obj = self.get_object()
        context = {}
        if obj is not None:
            form = jobAppliedForm(instance = obj)
        context = {
            "object": obj,
            "form": form
        }
        return render(request, self.template_name, context)

    def post(self, request, id = None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context["object"] = None
            return redirect("../../..")
        return render(request, self.template_name, context)
    

class jobAppliedViewSet(viewsets.ModelViewSet):
    serializer_class = jobAppliedSerializer
    queryset = jobApplication.objects.all() 

class jobAppliedGenericSet(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                            mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    lookup_field = "id"
    serializer_class = jobAppliedSerializer
    queryset = jobApplication.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id = None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id = None):
        return self.update(request, id)

    def destroy(self, request, id):
        return self.destroy(request, id)