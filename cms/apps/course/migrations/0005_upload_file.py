# Generated by Django 2.0 on 2019-05-21 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_auto_20190520_1656'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload_file',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_url', models.FileField(upload_to='upload/files/%Y/%m/%d', verbose_name='文件url')),
            ],
            options={
                'verbose_name': '上传文件',
                'verbose_name_plural': '上传文件',
            },
        ),
    ]
