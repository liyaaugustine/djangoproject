# Generated by Django 3.2.3 on 2021-09-01 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0013_auto_20210901_1216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admission',
            name='password',
        ),
        migrations.RemoveField(
            model_name='content',
            name='loginid',
        ),
        migrations.AddField(
            model_name='admission',
            name='logid',
            field=models.ForeignKey(default=10, on_delete=django.db.models.deletion.CASCADE, to='second.studentlogin'),
            preserve_default=False,
        ),
    ]
