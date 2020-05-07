# Generated by Django 3.0.2 on 2020-03-10 00:00

from django.db import migrations, models
import sortedm2m.fields


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_delete_d5'),
    ]

    operations = [
        migrations.AlterField(
            model_name='d6',
            name='day1',
            field=sortedm2m.fields.SortedManyToManyField(help_text=None, related_name='d6_day1_activities', to='web.Activities'),
        ),
        migrations.AlterField(
            model_name='d6',
            name='day3',
            field=models.ManyToManyField(blank=True, related_name='d6_day3_activities', to='web.Activities'),
        ),
        migrations.AlterField(
            model_name='d6',
            name='day4',
            field=models.ManyToManyField(blank=True, related_name='d6_day4_activities', to='web.Activities'),
        ),
        migrations.AlterField(
            model_name='d6',
            name='day5',
            field=models.ManyToManyField(blank=True, related_name='d6_day5_activities', to='web.Activities'),
        ),
        migrations.AlterField(
            model_name='d6',
            name='day6',
            field=models.ManyToManyField(blank=True, related_name='d6_day6_activities', to='web.Activities'),
        ),
        migrations.AlterField(
            model_name='d6',
            name='price',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]
