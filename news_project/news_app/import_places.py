import os
import sys
import django
import pandas as pd
from decimal import Decimal

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "news_project.settings")
django.setup()

# Импортируем модель Place из models.py
from news_app.models import Place

def import_places(file_path):
    df = pd.read_excel(file_path)

    for index, row in df.iterrows():
        place_data = {
            'name': row['Name place'],
            'latitude': Decimal(row['Geo-position'].split(',')[0].strip()),
            'longitude': Decimal(row['Geo-position'].split(',')[1].strip()),
            'rating': Decimal(row['Rate']),
        }
        Place.objects.create(**place_data)


if __name__ == "__main__":
    file_path = "D:/work/test/news_project/Places.xlsx"
    import_places(file_path)
