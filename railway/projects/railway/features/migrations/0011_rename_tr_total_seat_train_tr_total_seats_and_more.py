# Generated by Django 4.1.5 on 2023-03-14 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0010_route'),
    ]

    operations = [
        migrations.RenameField(
            model_name='train',
            old_name='tr_total_seat',
            new_name='tr_total_seats',
        ),
        migrations.AddField(
            model_name='route',
            name='available_seats',
            field=models.IntegerField(default=1000),
        ),
    ]
