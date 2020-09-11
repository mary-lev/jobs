import json
import django
from django.conf import settings
from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

settings.configure(DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
})

django.setup()

def main():
    with open('mock_data.py', 'r', encoding='utf-8') as file:
        data = file.read()

    print(data)

if __name__ == '__main__':
    main()