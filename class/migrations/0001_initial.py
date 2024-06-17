# Generated by Django 4.2.13 on 2024-06-17 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=20)),
                ('class_number', models.PositiveSmallIntegerField()),
                ('teacher_incharge', models.CharField(max_length=15)),
                ('number_of_students', models.PositiveSmallIntegerField()),
                ('number_of_sits', models.PositiveSmallIntegerField()),
                ('number_of_tables', models.PositiveSmallIntegerField()),
                ('number_of_boards', models.PositiveSmallIntegerField()),
                ('numbers_of_doors', models.PositiveSmallIntegerField()),
                ('class_color', models.CharField(max_length=20)),
                ('number_of_art', models.PositiveSmallIntegerField()),
            ],
        ),
    ]