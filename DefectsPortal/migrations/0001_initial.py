# Generated by Django 5.0.2 on 2025-02-19 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Defect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('defect_id', models.IntegerField()),
                ('defect_name', models.CharField(max_length=100)),
                ('defect_type', models.TextField()),
                ('assigned_by', models.DateTimeField(auto_now_add=True)),
                ('assigned_to', models.DateTimeField(auto_now=True)),
                ('description', models.TextField()),
                ('priority', models.CharField(max_length=100)),
            ],
        ),
    ]
