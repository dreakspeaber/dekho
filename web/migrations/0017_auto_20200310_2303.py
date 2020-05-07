# Generated by Django 3.0.2 on 2020-03-10 23:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0016_sales_has_closed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activities',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities_service', to='web.Services'),
        ),
    ]
