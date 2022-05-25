from django.urls import path, include
from .views import jobApplicationList, jobApplicationCreate, jobApplicationView, jobApplicationUpdate, jobApplicationDelete, jobAppliedViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("jobApplied", jobAppliedViewSet, basename = "jobApplied")


urlpatterns = [
    path("", jobApplicationList.as_view(), name = "Job Application List"),
    path("create/", jobApplicationCreate.as_view(), name = "Job Application Create"),
    path("detail/<int:id>/", jobApplicationView.as_view(), name = "Job Application View"),
    path("detail/<int:id>/update/", jobApplicationUpdate.as_view(), name = "Job Application Update"),
    path("detail/<int:id>/delete/", jobApplicationDelete.as_view(), name = "Job Application Delete"),
    path("viewset/", include(router.urls))
]
