# Generated by Django 3.2.7 on 2021-09-18 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('admission_number', models.IntegerField(unique=True)),
                ('is_qualified', models.BooleanField(default=False)),
                ('average_score', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('student_capacity', models.IntegerField()),
                ('students', models.ManyToManyField(to='classroom.Student')),
            ],
        ),
    ]
