# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 23:07
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PointsOfInterest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age_of_dgps_data', models.TextField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('dgps_id', models.TextField(blank=True, null=True)),
                ('elevation', models.TextField(blank=True, null=True)),
                ('extensions', models.TextField(blank=True, null=True)),
                ('geoid_height', models.TextField(blank=True, null=True)),
                ('horizontal_dilution', models.TextField(blank=True, null=True)),
                ('latitude', models.TextField(blank=True, null=True)),
                ('link', models.TextField(blank=True, null=True)),
                ('link_text', models.TextField(blank=True, null=True)),
                ('link_type', models.TextField(blank=True, null=True)),
                ('longitude', models.TextField(blank=True, null=True)),
                ('magnetic_variation', models.TextField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('position_dilution', models.TextField(blank=True, null=True)),
                ('satellites', models.TextField(blank=True, null=True)),
                ('source', models.TextField(blank=True, null=True)),
                ('symbol', models.TextField(blank=True, null=True)),
                ('time', models.TextField(blank=True, null=True)),
                ('gtype', models.TextField(blank=True, null=True)),
                ('type_of_gpx_fix', models.TextField(blank=True, null=True)),
                ('vertical_dilution', models.TextField(blank=True, null=True)),
                ('owner', models.CharField(blank=True, max_length=255, null=True)),
                ('group', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('extensions', models.TextField(blank=True, null=True)),
                ('gpxtype', models.TextField(blank=True, null=True)),
                ('link', models.TextField(blank=True, null=True)),
                ('link_text', models.TextField(blank=True, null=True)),
                ('link_type', models.TextField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('number', models.TextField(blank=True, null=True)),
                ('points', models.TextField(blank=True, null=True)),
                ('source', models.TextField(blank=True, null=True)),
                ('owner', models.CharField(blank=True, max_length=255, null=True)),
                ('group', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('geom', django.contrib.gis.db.models.fields.LineStringField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='RoutePoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age_of_dgps_data', models.TextField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('dgps_id', models.TextField(blank=True, null=True)),
                ('elevation', models.TextField(blank=True, null=True)),
                ('extensions', models.TextField(blank=True, null=True)),
                ('geoid_height', models.TextField(blank=True, null=True)),
                ('gtype', models.TextField(blank=True, null=True)),
                ('horizontal_dilution', models.TextField(blank=True, null=True)),
                ('latitude', models.TextField(blank=True, null=True)),
                ('link', models.TextField(blank=True, null=True)),
                ('link_text', models.TextField(blank=True, null=True)),
                ('link_type', models.TextField(blank=True, null=True)),
                ('longitude', models.TextField(blank=True, null=True)),
                ('magnetic_variation', models.TextField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('position_dilution', models.TextField(blank=True, null=True)),
                ('satellites', models.TextField(blank=True, null=True)),
                ('source', models.TextField(blank=True, null=True)),
                ('symbol', models.TextField(blank=True, null=True)),
                ('time', models.TextField(blank=True, null=True)),
                ('type_of_gpx_fix', models.TextField(blank=True, null=True)),
                ('vertical_dilution', models.TextField(blank=True, null=True)),
                ('ordinal', models.IntegerField(default=0)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.Route')),
            ],
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('identifier', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('trip_type', models.CharField(choices=[('air', 'air'), ('boat', 'boat'), ('cycle', 'cycle'), ('road', 'road'), ('tramping', 'tramping')], default='tramping', max_length=64)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('subject', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('days_length', models.IntegerField(default=1)),
                ('owner', models.CharField(blank=True, max_length=255, null=True)),
                ('group', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TemplateNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(blank=True, max_length=255, null=True)),
                ('group', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.Template')),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('extensions', models.TextField(blank=True, null=True)),
                ('gtype', models.TextField(blank=True, null=True)),
                ('link', models.TextField(blank=True, null=True)),
                ('link_text', models.TextField(blank=True, null=True)),
                ('link_type', models.TextField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('number', models.TextField(blank=True, null=True)),
                ('source', models.TextField(blank=True, null=True)),
                ('owner', models.CharField(blank=True, max_length=255, null=True)),
                ('group', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiLineStringField(blank=True, null=True, srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='TrackPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age_of_dgps_data', models.TextField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('course', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('dgps_id', models.TextField(blank=True, null=True)),
                ('elevation', models.TextField(blank=True, null=True)),
                ('extensions', models.TextField(blank=True, null=True)),
                ('geoid_height', models.TextField(blank=True, null=True)),
                ('gtype', models.TextField(blank=True, null=True)),
                ('horizontal_dilution', models.TextField(blank=True, null=True)),
                ('latitude', models.TextField(blank=True, null=True)),
                ('link', models.TextField(blank=True, null=True)),
                ('link_text', models.TextField(blank=True, null=True)),
                ('link_type', models.TextField(blank=True, null=True)),
                ('longitude', models.TextField(blank=True, null=True)),
                ('magnetic_variation', models.TextField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('position_dilution', models.TextField(blank=True, null=True)),
                ('satellites', models.TextField(blank=True, null=True)),
                ('source', models.TextField(blank=True, null=True)),
                ('speed', models.TextField(blank=True, null=True)),
                ('symbol', models.TextField(blank=True, null=True)),
                ('time', models.TextField(blank=True, null=True)),
                ('type_of_gpx_fix', models.TextField(blank=True, null=True)),
                ('vertical_dilution', models.TextField(blank=True, null=True)),
                ('ordinal', models.IntegerField(default=0)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='TrackSegment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extensions', models.TextField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('geom', django.contrib.gis.db.models.fields.LineStringField(blank=True, null=True, srid=4326)),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.Track')),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('identifier', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('trip_type', models.CharField(choices=[('air', 'air'), ('boat', 'boat'), ('cycle', 'cycle'), ('road', 'road'), ('tramping', 'tramping')], default='tramping', max_length=64)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('subject', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('days_length', models.IntegerField(default=1)),
                ('owner', models.CharField(blank=True, max_length=255, null=True)),
                ('group', models.CharField(blank=True, max_length=255, null=True)),
                ('start_date_planned', models.DateField(blank=True, null=True)),
                ('end_date_planned', models.DateField(blank=True, null=True)),
                ('start_date_actual', models.DateField(blank=True, null=True)),
                ('end_date_actual', models.DateField(blank=True, null=True)),
                ('templates', models.ManyToManyField(to='trips.Template')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TripNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(blank=True, max_length=255, null=True)),
                ('group', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('trips', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='trips.Trip')),
            ],
        ),
        migrations.CreateModel(
            name='TripReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('working', 'working'), ('pending', 'pending'), ('publshed', 'published'), ('withdrawn', 'withdrawn')], default='Unclassified', max_length=64)),
                ('date_pub', models.DateTimeField()),
                ('author', models.CharField(blank=True, max_length=255, null=True)),
                ('report_text', models.TextField(blank=True, null=True)),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.Trip')),
            ],
        ),
        migrations.CreateModel(
            name='Waypoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age_of_dgps_data', models.TextField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('dgps_id', models.TextField(blank=True, null=True)),
                ('elevation', models.TextField(blank=True, null=True)),
                ('extensions', models.TextField(blank=True, null=True)),
                ('geoid_height', models.TextField(blank=True, null=True)),
                ('horizontal_dilution', models.TextField(blank=True, null=True)),
                ('latitude', models.TextField(blank=True, null=True)),
                ('link', models.TextField(blank=True, null=True)),
                ('link_text', models.TextField(blank=True, null=True)),
                ('link_type', models.TextField(blank=True, null=True)),
                ('longitude', models.TextField(blank=True, null=True)),
                ('magnetic_variation', models.TextField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('position_dilution', models.TextField(blank=True, null=True)),
                ('satellites', models.TextField(blank=True, null=True)),
                ('source', models.TextField(blank=True, null=True)),
                ('symbol', models.TextField(blank=True, null=True)),
                ('time', models.TextField(blank=True, null=True)),
                ('gtype', models.TextField(blank=True, null=True)),
                ('type_of_gpx_fix', models.TextField(blank=True, null=True)),
                ('vertical_dilution', models.TextField(blank=True, null=True)),
                ('owner', models.CharField(blank=True, max_length=255, null=True)),
                ('group', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('trips', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.Trip')),
            ],
        ),
        migrations.AddField(
            model_name='trackpoint',
            name='segment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.TrackSegment'),
        ),
        migrations.AddField(
            model_name='track',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.Trip'),
        ),
        migrations.AddField(
            model_name='route',
            name='template',
            field=models.ManyToManyField(to='trips.Template'),
        ),
        migrations.AddField(
            model_name='route',
            name='trips',
            field=models.ManyToManyField(to='trips.Trip'),
        ),
        migrations.AddField(
            model_name='pointsofinterest',
            name='template',
            field=models.ManyToManyField(related_name='pois', to='trips.Template'),
        ),
        migrations.AddField(
            model_name='pointsofinterest',
            name='trips',
            field=models.ManyToManyField(related_name='pois', to='trips.Trip'),
        ),
    ]