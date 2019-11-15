# Generated by Django 2.2.7 on 2019-11-15 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coffee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('roaster', models.CharField(blank=True, max_length=100)),
                ('brew_method', models.CharField(blank=True, max_length=100)),
                ('taste_note', models.CharField(blank=True, max_length=500)),
                ('rating', models.CharField(blank=True, max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]