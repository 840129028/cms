# Generated by Django 2.0 on 2019-05-20 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='content',
            field=models.FileField(blank=True, null=True, upload_to='sourse/vedio/', verbose_name='视频内容'),
        ),
    ]