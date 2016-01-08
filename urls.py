from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from . import search_location,show_offers
import json

@csrf_exempt
def test(request):
    if request.method == "GET":
        extra = {
            "method": "GET",
            "requestData": request.GET
        }
    else:
        extra = {
            "method": "POST",
            "requestData": json.loads(request.body.decode())
        }
    return JsonResponse({
        "result": True,
        "Message": "Welcome to the E-commerce App API",
        "extra": extra
    })

urlpatterns = [
    url(r'^$', test),
    url(r'^location',  search_location.get_location),
	url(r'^show_offers',  show_offers.show_offers)

]