from django.db import models

# Create your models here.
from django.db import models


class WeatherRecord(models.Model):
    date_time = models.DateTimeField(verbose_name="观测时间")
    temp_c = models.FloatField(verbose_name="摄氏温度")
    humidity = models.IntegerField(verbose_name="相对湿度(%)")
    wind_speed = models.FloatField(verbose_name="风速(km/h)")
    visibility = models.FloatField(verbose_name="能见度(km)")
    pressure = models.FloatField(verbose_name="气压(kPa)")
    condition = models.CharField(max_length=100, verbose_name="天气状况")

    def __str__(self):
        return f"{self.date_time} - {self.condition}"
