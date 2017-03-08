# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 06:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('ip_addr', models.GenericIPAddressField(unique=True)),
                ('monitored_by', models.CharField(choices=[('agent', 'Agent'), ('snmp', 'SNMP'), ('wget', 'WGET')], max_length=64, verbose_name='\u76d1\u63a7\u65b9\u5f0f')),
                ('host_alive_check_interval', models.IntegerField(default=30, verbose_name='\u4e3b\u673a\u5b58\u6d3b\u72b6\u6001\u68c0\u6d4b\u95f4\u9694')),
                ('status', models.IntegerField(choices=[(1, 'Online'), (2, 'Down'), (3, 'Unreachable'), (4, 'Offline'), (5, 'Problem')], default=1, verbose_name='\u72b6\u6001')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='\u5907\u6ce8')),
            ],
        ),
    ]