# Generated by Django 3.1.1 on 2020-11-01 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='msg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=300)),
                ('email', models.TextField(max_length=300)),
                ('msg', models.TextField(max_length=300)),
                ('subject', models.TextField(max_length=300)),
            ],
        ),
    ]