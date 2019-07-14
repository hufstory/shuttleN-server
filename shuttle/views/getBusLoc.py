from django.http import JsonResponse
import requests

def getBusLoc(request):
    req= requests.get("http://bis.hufs.ac.kr/getBusLoc").json()

    for i in range(len(req['bus_array'])):
        req['bus_array'][i]['Ntime'] = i

    return JsonResponse(
        req
    )