# Generated by Django 3.0.7 on 2020-06-20 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='total2',
            field=models.PositiveIntegerField(blank=True, editable=False, null=True),
        ),
    ]
