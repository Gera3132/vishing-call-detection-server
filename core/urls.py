from django.urls import path
from .views import analyze_audio

urlpatterns = [

    path(
        "analyze_audio/",
        analyze_audio
    )
]