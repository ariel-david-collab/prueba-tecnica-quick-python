# Generated by Django 3.2.9 on 2021-11-07 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiUsers', '0005_auto_20211107_0003'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='token',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=120),
        ),
    ]
