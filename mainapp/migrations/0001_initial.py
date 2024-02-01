# Generated by Django 5.0.1 on 2024-02-01 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('progress', models.BooleanField(default=False)),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]