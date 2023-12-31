# Generated by Django 3.2.4 on 2022-09-22 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Host', '0005_alter_registration_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='requestpass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regid', models.IntegerField()),
                ('fromdate', models.DateField()),
                ('fromtime', models.TimeField()),
                ('todate', models.DateField()),
                ('totime', models.TimeField()),
                ('reqtime', models.DateTimeField()),
                ('reason', models.TextField()),
                ('status', models.BooleanField()),
                ('adminremark', models.TextField()),
                ('permitstatus', models.CharField(max_length=100)),
            ],
        ),
    ]
