# Generated by Django 3.2.3 on 2021-08-29 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0007_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentLogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=8)),
                ('studid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='second.admission')),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.CharField(max_length=20)),
                ('teacher', models.CharField(max_length=20)),
                ('course', models.CharField(max_length=20)),
                ('month', models.CharField(max_length=10)),
                ('day', models.CharField(max_length=15)),
                ('event', models.CharField(max_length=30)),
                ('address', models.TextField()),
                ('email', models.EmailField(max_length=100)),
                ('firstnum', models.BigIntegerField()),
                ('secnum', models.BigIntegerField()),
                ('images', models.FileField(upload_to='certificates/')),
                ('loginid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='second.mylogin')),
            ],
        ),
    ]
