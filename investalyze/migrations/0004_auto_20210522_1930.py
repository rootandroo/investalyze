# Generated by Django 3.1.7 on 2021-05-22 19:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('investalyze', '0003_auto_20210522_1856'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lots', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='lot',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='matched_orders', to='investalyze.lot'),
        ),
    ]
