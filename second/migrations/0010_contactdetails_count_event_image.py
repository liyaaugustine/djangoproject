# Generated by Django 3.2.3 on 2021-08-30 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0009_auto_20210829_2227'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='certificates/')),
                ('loginid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='second.mylogin')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=10)),
                ('day', models.CharField(max_length=15)),
                ('event', models.CharField(max_length=30)),
                ('loginid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='second.mylogin')),
            ],
        ),
        migrations.CreateModel(
            name='Count',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.CharField(max_length=20)),
                ('teacher', models.CharField(max_length=20)),
                ('course', models.CharField(max_length=20)),
                ('loginid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='second.mylogin')),
            ],
        ),
        migrations.CreateModel(
            name='ContactDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('email', models.EmailField(max_length=100)),
                ('firstnum', models.BigIntegerField()),
                ('secnum', models.BigIntegerField()),
                ('loginid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='second.mylogin')),
            ],
        ),
    ]
