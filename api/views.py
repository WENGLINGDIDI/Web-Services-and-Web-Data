from django.db.models import Avg, Max, Min
from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from .models import WeatherRecord
import json


# 查询或者提交天气记录
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

# 修改天气记录的属性
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

# 查询气温统计数据
@csrf_exempt
def weather_temStats(request):
    if request.method == 'GET':
        stats = WeatherRecord.objects.aggregate(
            avg_temp=Avg('temp_c'),
            max_temp=Max('temp_c'),
            min_temp=Min('temp_c'),
            avg_humidity=Avg('humidity')
        )
        return JsonResponse(stats)

# 筛选天气
@csrf_exempt
def weather_search(request):
    if request.method == 'GET':
        condition = request.GET.get('condition')
        temp_min = request.GET.get('temp_min')
        temp_max = request.GET.get('temp_max')



        queryset = WeatherRecord.objects.all()
        if condition:
            queryset = queryset.filter(condition__icontains=condition)
        if temp_min:
            queryset = queryset.filter(temp_c__gte=float(temp_min))
        if temp_max:
            queryset = queryset.filter(temp_c__lte=float(temp_max))
        data = list(queryset.values())

        # 返回结果及其元数据
        return JsonResponse({
            "count": len(data),
            "filters_applied": {
                "condition": condition,
                "temp_min": temp_min,
                "temp_max": temp_max
            },
            "results": data
        }, safe=False)