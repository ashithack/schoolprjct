# Generated by Django 4.2.3 on 2023-10-25 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formdatas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='some_value', max_length=250)),
                ('dob', models.DateField(default='some_value')),
                ('age', models.IntegerField(default='some_value')),
                ('gender', models.CharField(default='some_value', max_length=12)),
                ('phone', models.CharField(default='some_value', max_length=10)),
                ('email', models.CharField(default='some_value', max_length=250)),
                ('address', models.CharField(default='some_value', max_length=250)),
                ('dept', models.CharField(default='some_value', max_length=50)),
                ('course', models.CharField(default='some_value', max_length=50)),
            ],
        ),
    ]
