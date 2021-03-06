# Generated by Django 2.2.6 on 2020-02-14 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Racks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('racks_id', models.CharField(max_length=2)),
                ('students', models.ManyToManyField(blank=True, related_name='racks', to='task.Student')),
            ],
        ),
    ]
