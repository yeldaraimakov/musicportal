# Generated by Django 2.1.5 on 2019-06-13 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_portal', '0008_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]