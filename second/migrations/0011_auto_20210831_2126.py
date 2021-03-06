# Generated by Django 3.2.3 on 2021-08-31 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0010_contactdetails_count_event_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('candidatename', models.CharField(max_length=50)),
                ('parentname', models.CharField(max_length=50)),
                ('phonenumber', models.BigIntegerField()),
                ('category', models.CharField(max_length=50)),
                ('application', models.CharField(max_length=100)),
                ('sslcmark', models.CharField(max_length=10)),
                ('plus2mark', models.CharField(max_length=10)),
                ('sslc', models.FileField(upload_to='certificates/')),
                ('plus2', models.FileField(upload_to='certificates/')),
                ('qualification', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='admission',
            name='password',
            field=models.CharField(default=10, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admission',
            name='plus2mark',
            field=models.CharField(default=10, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admission',
            name='sslcmark',
            field=models.CharField(default=10, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admission',
            name='ugmark',
            field=models.CharField(default=10, max_length=10),
            preserve_default=False,
        ),
    ]
