import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'intelligence.settings')
django.setup()

from data_processing.models import IntelligenceReport, Entity, User, EntityIntelligenceReport

def populate():
    User.objects.all().delete()

    manager1 = User.objects.create_user(username='admin', password='Admin12345',policeID='ADMIN001', rank='Commander', isManager=True)

    print("Database populated with test data.")

if __name__ == '__main__':
    populate()