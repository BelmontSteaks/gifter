# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('gift_id', models.AutoField(serialize=False, primary_key=True)),
                ('store', models.CharField(max_length=200, null=True, blank=True, default=None)),
                ('item', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('purchased', models.BooleanField(default=False)),
                ('cost', models.CharField(max_length=200, null=True, blank=True, default=None)),
                ('date_purchased', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GiftOnList',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('gift_id', models.ForeignKey(to='lamps.Gift')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('group_id', models.AutoField(serialize=False, primary_key=True)),
                ('group_name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('list_id', models.AutoField(serialize=False, primary_key=True)),
                ('list_name', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
                ('user_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ListInGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('group_id', models.ForeignKey(to='lamps.Group')),
                ('list_id', models.ForeignKey(to='lamps.List')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserInGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('group_id', models.ForeignKey(to='lamps.Group')),
                ('user_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=2)),
                ('zip', models.CharField(max_length=5)),
                ('country', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=15)),
                ('ts_created', models.DateTimeField(auto_now_add=True)),
                ('ts_updated', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='giftonlist',
            name='list_id',
            field=models.ForeignKey(to='lamps.List'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gift',
            name='list',
            field=models.ForeignKey(to='lamps.List'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gift',
            name='purchaser',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, default=None, blank=True),
            preserve_default=True,
        ),
    ]
