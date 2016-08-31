# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-13 12:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='OAuthProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oauth_token', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FacebookProfile',
            fields=[
                ('oauthprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='socialaccess.OAuthProfile')),
                ('uid', models.CharField(max_length=80)),
            ],
            bases=('socialaccess.oauthprofile',),
        ),
        migrations.CreateModel(
            name='GithubProfile',
            fields=[
                ('oauthprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='socialaccess.OAuthProfile')),
                ('uid', models.CharField(max_length=80)),
            ],
            bases=('socialaccess.oauthprofile',),
        ),
        migrations.CreateModel(
            name='GoogleProfile',
            fields=[
                ('oauthprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='socialaccess.OAuthProfile')),
                ('uid', models.CharField(max_length=80)),
            ],
            bases=('socialaccess.oauthprofile',),
        ),
        migrations.CreateModel(
            name='LinkedinProfile',
            fields=[
                ('oauthprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='socialaccess.OAuthProfile')),
                ('uid', models.CharField(max_length=80)),
            ],
            bases=('socialaccess.oauthprofile',),
        ),
        migrations.CreateModel(
            name='TwitterProfile',
            fields=[
                ('oauthprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='socialaccess.OAuthProfile')),
                ('uid', models.CharField(max_length=80)),
            ],
            bases=('socialaccess.oauthprofile',),
        ),
        migrations.AddField(
            model_name='oauthprofile',
            name='site',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sites.Site'),
        ),
        migrations.AddField(
            model_name='oauthprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='oauth_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]