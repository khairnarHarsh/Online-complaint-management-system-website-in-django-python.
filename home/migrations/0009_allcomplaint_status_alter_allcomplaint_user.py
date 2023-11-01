# Generated by Django 4.1.7 on 2023-04-03 07:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0008_delete_solvedcomplaint_delete_unsolvedcomplaint_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='allcomplaint',
            name='status',
            field=models.IntegerField(choices=[(1, 'pending'), (2, 'solved'), (3, 'unsolved')], default=1),
        ),
        migrations.AlterField(
            model_name='allcomplaint',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
