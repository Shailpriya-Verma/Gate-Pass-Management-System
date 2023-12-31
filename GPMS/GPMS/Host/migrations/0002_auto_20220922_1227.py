# Generated by Django 3.2.4 on 2022-09-22 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Host', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='guardregistration',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('guardid', models.IntegerField(primary_key=True, serialize=False)),
                ('passwd', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('pic', models.ImageField(null=True, upload_to='Profile/')),
                ('mob', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=100)),
                ('rdate', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='registration',
            name='rid',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
