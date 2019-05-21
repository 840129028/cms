# Generated by Django 2.0 on 2019-05-20 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_video_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(upload_to='course/image/%Y/%m', verbose_name='上传图片'),
        ),
        migrations.AlterField(
            model_name='video',
            name='content',
            field=models.FileField(blank=True, null=True, upload_to='course/vedio/', verbose_name='视频内容'),
        ),
    ]