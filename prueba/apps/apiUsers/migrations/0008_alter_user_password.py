# Generated by Django 3.2.9 on 2021-11-07 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiUsers', '0007_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=120),
        ),
    ]
