from django.db import models

# Create your models here.
from django.db import models


class WeatherRecord(models.Model):
    # 对应 CSV 中的 Date/Time
    date_time = models.DateTimeField(verbose_name="观测时间")

    # 对应 Temp_C
    temp_c = models.FloatField(verbose_name="摄氏温度")

    # 对应 Rel Hum_%
    humidity = models.IntegerField(verbose_name="相对湿度(%)")

    # 对应 Wind Speed_km/h
    wind_speed = models.FloatField(verbose_name="风速(km/h)")

    # 对应 Visibility_km
    visibility = models.FloatField(verbose_name="能见度(km)")

    # 对应 Press_kPa
    pressure = models.FloatField(verbose_name="气压(kPa)")

    # 对应 Weather
    condition = models.CharField(max_length=100, verbose_name="天气状况")

    def __str__(self):
        return f"{self.date_time} - {self.condition}"
