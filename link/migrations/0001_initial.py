# Generated by Django 2.1.7 on 2022-03-01 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('received_url', models.URLField(max_length=100, unique=True, verbose_name='Полученная ссылка')),
                ('short_url', models.URLField(max_length=20, unique=True, verbose_name='Новая ссылка')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Когда создана новая ссылка')),
                ('amount_clicks', models.IntegerField(default=0, verbose_name='Количество переходов по новой ссылки')),
            ],
        ),
    ]
