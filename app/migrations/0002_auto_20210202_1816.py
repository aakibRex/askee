# Generated by Django 3.1.5 on 2021-02-02 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ansinfo',
            name='user_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='quesinfo',
            name='user_id',
            field=models.IntegerField(default=0),
        ),
    ]