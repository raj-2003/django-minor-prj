# Generated by Django 4.2 on 2023-04-11 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myjio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.PositiveIntegerField()),
                ('address', models.TextField()),
                ('gender', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
