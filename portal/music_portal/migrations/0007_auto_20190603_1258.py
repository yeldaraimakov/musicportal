# Generated by Django 2.1.5 on 2019-06-03 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_portal', '0006_auto_20190602_2020'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='music_author',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='music',
            name='word_author',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]