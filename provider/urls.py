from django.urls import path


from .views import ProviderView, SingleProviderView


app_name = "providers"


urlpatterns = [
    path('providers/', ProviderView.as_view()),
    path('providers/<int:pk>', SingleProviderView.as_view())
]