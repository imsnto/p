# Generated by Django 4.1.5 on 2023-03-11 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=11)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('nid', models.CharField(max_length=10)),
                ('post_code', models.IntegerField()),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
