__author__ = 'Pradeep'from bson.json_util import dumpsfrom django.http import HttpResponsefrom django.views.decorators.csrf import csrf_exemptimport refrom . import dbimport jsonfailure = dumps({"success":0})@csrf_exemptdef get_qrcode(request):	data = db.codes	try:		code = request.GET['code']	except:		return HttpResponse(failure, content_type="application/json")	result = data.find({"used":False , "qrcode":code}).distinct("qrcode")	success = dumps({"success": 1, "data": result, "total": len(result)})	return HttpResponse(success, content_type="application/json")	def get_vendor(request):	data = db.vendors	try:		location = request.GET['location']	except:		return HttpResponse(failure, content_type="application/json")	result = data.find({"address.location":location}).distinct("qrcode")	success = dumps({"success": 1, "data": result, "total": len(result)})	return HttpResponse(success, content_type="application/json")	def getLocation(request):	data = db.locations	try:		area = request.GET['area']	except:		return HttpResponse(failure, content_type="application/json")	query = {"area":area}	result = data.find(query, {"_id":False,"locations": True})	success = dumps({"success": 1, "data": result['data'][0]['location'], "total": result.count()})	return HttpResponse(success, content_type="application/json")