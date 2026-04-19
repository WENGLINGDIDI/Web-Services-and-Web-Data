from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from .models import WeatherRecord
import json

@csrf_exempt
def weather_list(request):
    # 端点 1: 获取所有天气数据 (Read)
    if request.method == 'GET':
        data = list(WeatherRecord.objects.all().values())
        return JsonResponse(data, safe=False)

    elif request.method == 'POST':
        body = json.loads(request.body)
        new_record = WeatherRecord.objects.create(
            date_time=body['date_time'],
            temp_c=body['temp_c'],
            humidity=body['humidity'],
            wind_speed=body['wind_speed'],
            visibility=body['visibility'],
            pressure=body['pressure'],
            condition=body['condition']
        )
        return JsonResponse({"id": new_record.id, "status": "created"}, status=201)

    return HttpResponseNotAllowed(['GET', 'POST'])

@csrf_exempt
def weather_detail(request, pk):
    try:
        record = WeatherRecord.objects.get(pk=pk)
    except WeatherRecord.DoesNotExist:
        return JsonResponse({"error": "Not found"}, status=404)
    if request.method == 'GET':
        data = {
            "id": record.id,
            "date_time": record.date_time,
            "temp_c": record.temp_c,
            "humidity": record.humidity,
            "wind_speed": record.wind_speed,
            "visibility": record.visibility,
            "pressure": record.pressure,
            "condition": record.condition,
        }
        return JsonResponse(data)
    elif request.method == 'PUT':
        body = json.loads(request.body)
        record.temp_c = body.get('temp_c', record.temp_c)
        record.save()
        return JsonResponse({"status": "updated"})

    elif request.method == 'DELETE':
        record.delete()
        return JsonResponse({"status": "deleted"}, status=204)