# Generated by Django 3.1.5 on 2021-02-01 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clgInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='quesInfo',
            fields=[
                ('Qid', models.AutoField(primary_key=True, serialize=False)),
                ('questions', models.TextField()),
                ('asked_by_name', models.CharField(max_length=100)),
                ('college_name', models.TextField()),
                ('desig', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ansInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answers', models.TextField()),
                ('ans_by_name', models.CharField(max_length=100)),
                ('desig', models.CharField(max_length=100)),
                ('Qid', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.quesinfo')),
            ],
        ),
    ]