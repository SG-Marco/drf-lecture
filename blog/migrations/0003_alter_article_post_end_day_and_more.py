# Generated by Django 4.0.5 on 2022-06-20 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='post_end_day',
            field=models.DateField(null=True, verbose_name='노출 종료일'),
        ),
        migrations.AlterField(
            model_name='article',
            name='post_start_day',
            field=models.DateField(null=True, verbose_name='노출 시작일'),
        ),
    ]