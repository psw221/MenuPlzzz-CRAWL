# Generated by Django 2.1.5 on 2019-02-11 09:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('crawl', '0003_auto_20190211_0823'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='생성 시간'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menu',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, verbose_name='수정 시간'),
        ),
        migrations.AddField(
            model_name='store',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='생성 시간'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='store',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, verbose_name='수정 시간'),
        ),
        migrations.AddField(
            model_name='storetype',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='생성 시간'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='storetype',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, verbose_name='수정 시간'),
        ),
    ]
