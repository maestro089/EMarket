# Generated by Django 4.0.6 on 2022-07-29 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='the_cart',
            name='quentity',
            field=models.FloatField(null=True, verbose_name='Quantity'),
        ),
    ]
