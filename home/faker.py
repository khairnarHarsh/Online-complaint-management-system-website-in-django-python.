from .models import*
from faker import Faker
fake = Faker()
import random


def generate_random_data(n=10)->bool:
    [c.objects.create(
            id=fake.id(),
            Subject=fake.Subject(),
            Time=fake.Time()
        )for i in range(0,n)]
    
    return True
