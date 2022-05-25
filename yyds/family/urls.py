from .views import (
    familyListView, familyCreateView, familyDetailView, familyUpdateView, familyDeleteView
)
from django.urls import path

app_name = "family"

urlpatterns = [
    path("", familyListView.as_view(), name = "Family_Information"),
    path("create/", familyCreateView.as_view(), name = "Family_Form"),
    path("<int:id>/detail/", familyDetailView.as_view(), name = "Family_Detail"),
    path("<int:id>/update", familyUpdateView.as_view(), name = "Family_Update"),
    path("<int:id>/delete/", familyDeleteView.as_view(), name = "Family_Delete")
]