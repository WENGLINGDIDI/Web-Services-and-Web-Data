import os
import csv
import django
from datetime import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "weather_api_project.settings")
django.setup()
from api.models import WeatherRecord


def import_weather():
    file_path = "weather_data.csv"
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found!")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        records = []

        print("Starting import...")
        for row in reader:
            try:
                dt = datetime.strptime(row["Date/Time"], "%m/%d/%Y %H:%M")

                records.append(
                    WeatherRecord(
                        date_time=dt,
                        temp_c=float(row["Temp_C"]),
                        humidity=int(row["Rel Hum_%"]),
                        wind_speed=float(row["Wind Speed_km/h"]),
                        visibility=float(row["Visibility_km"]),
                        pressure=float(row["Press_kPa"]),
                        condition=row["Weather"],
                    )
                )
            except Exception as e:
                print(f"Skipping row due to error: {e}")

        WeatherRecord.objects.bulk_create(records, ignore_conflicts=True)
        print(f"Successfully imported {len(records)} records!")


if __name__ == "__main__":
    import_weather()
