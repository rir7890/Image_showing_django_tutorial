# Generated by Django 5.0.4 on 2024-05-28 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
