# Generated by Django 4.2.3 on 2023-07-27 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='varient',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
