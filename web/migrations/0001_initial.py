# Generated by Django 3.0.2 on 2020-03-09 21:59

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
            name='Activities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.PositiveIntegerField()),
                ('render_tag', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_admin', models.BooleanField(blank=True, default=False)),
                ('is_sales', models.BooleanField(blank=True, default=True)),
                ('phone', models.CharField(blank=True, default='', max_length=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_closed', models.BooleanField(blank=True, default=False)),
                ('price', models.PositiveIntegerField()),
                ('day1', models.ManyToManyField(related_name='day1_activities', to='web.Activities')),
                ('day2', models.ManyToManyField(related_name='day2_activities', to='web.Activities')),
                ('day3', models.ManyToManyField(related_name='day3_activities', to='web.Activities')),
                ('day4', models.ManyToManyField(related_name='day4_activities', to='web.Activities')),
                ('day5', models.ManyToManyField(related_name='day5_activities', to='web.Activities')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='package_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='activities',
            name='loc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities_location', to='web.Location'),
        ),
    ]
