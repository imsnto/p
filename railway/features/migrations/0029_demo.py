# Generated by Django 4.1.7 on 2023-03-26 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0028_remove_train_tr_arrival_remove_train_tr_departure_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Demo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('roll', models.IntegerField()),
            ],
        ),
    ]
