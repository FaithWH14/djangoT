from django.shortcuts import render, get_object_or_404, redirect
from .models import familyINFO
from django.views import View
from .forms import familyForm
# Create your views here.

# def familyList(request):
#     queryset = familyINFO.objects.all()
#     context = {
#         "object_list": queryset
#     }

#     return render(request, "familyList.html", context)

class familyListView(View):
    template_name = "familyList.html"
    queryset = familyINFO.objects.all()

    def get_query(self):
        return self.queryset
    
    def get(self, request, *args, **kwargs):
        context = {"object_list": self.get_query()}
        return render(request, self.template_name, context)

class familyObjectMixin(object):
    model = familyINFO
    def get_object(self):
        id = self.kwargs.get("id")
        obj = None
        if id is not None:
            obj = get_object_or_404(self.model, id = id)
        return obj

class familyCreateView(familyObjectMixin, View):
    template_name = "familyCreate.html"
    def get(self, request, *args, **kwargs):
        form = familyForm()
        context = {
            "form": form
        }
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        form = familyForm(request.POST)
        if form.is_valid:
            form.save()
            form = familyForm()
        context = {
            "form": form
        }
        return render(request, self.template_name, context)

class familyDetailView(familyObjectMixin, View):
    template_name = "familyDetail.html"
    def get(self, request, id=None, *args, **kwargs):
        obj = self.get_object()
        context = {"obj": obj}
        return render(request, self.template_name, context)

class familyUpdateView(familyObjectMixin, View):
    template_name = "familyUpdate.html"

    def get(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = familyForm(instance = obj)
            context["form"] = form
            context["object"] = obj
        return render(request, self.template_name, context)
    def post(self, request, id=None, *args, **kwargs):
        context = {}
        obj =self.get_object()
        if obj is not None:
            form = familyForm(request.POST, instance = obj)
            if form.is_valid():
                form.save()
            context["object"] = obj
            context["form"] = form
        return render(request, self.template_name, context)

class familyDeleteView(familyObjectMixin, View):
    template_name = "familydelete.html"

    def get(self, request, id=None, *args, **kwargs):
        obj = self.get_object()
        context = {}
        if obj is not None:
            context["object"] = obj
        return render(request, self.template_name, context)
    def post(self, request, id=None,  *args, **kwargs):
        # POST method
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context['object'] = None
            return redirect('/family/')
        return render(request, self.template_name, context)