# Generated by Django 2.2.3 on 2019-12-17 11:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('address', models.CharField(max_length=225)),
                ('start_time', models.CharField(max_length=225)),
                ('end_time', models.CharField(max_length=225)),
                ('description', models.TextField()),
                ('likes', models.ManyToManyField(related_name='likes', through='market.Like', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('photo', models.ImageField(upload_to='images/')),
                ('price', models.IntegerField()),
                ('left', models.IntegerField()),
                ('description', models.CharField(max_length=1000)),
                ('market', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='market.Market')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('Totalprice', models.IntegerField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('market', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='market.Market')),
                ('menu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='market.Menu')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='like',
            name='market',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='market.Market'),
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
