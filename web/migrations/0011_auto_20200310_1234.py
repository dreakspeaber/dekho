# Generated by Django 3.0.2 on 2020-03-10 12:34

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0010_auto_20200310_1205'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=100)),
                ('price', models.PositiveIntegerField(blank=True, default=0)),
                ('time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('activities1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loc1_loc', to='web.Activities')),
                ('activities2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loc2_loc', to='web.Activities')),
                ('activities3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loc3_loc', to='web.Activities')),
                ('activities4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loc4_loc', to='web.Activities')),
                ('activities5', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loc5_loc', to='web.Activities')),
                ('activities6', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loc6_loc', to='web.Activities')),
                ('activities7', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loc7_loc', to='web.Activities')),
                ('activities8', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loc8_loc', to='web.Activities')),
                ('activities9', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loc9_loc', to='web.Activities')),
                ('loc1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loc1_loc', to='web.Location')),
                ('loc2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loc2_loc', to='web.Location')),
                ('loc3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loc3_loc', to='web.Location')),
                ('loc4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loc4_loc', to='web.Location')),
                ('loc5', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loc5_loc', to='web.Location')),
                ('loc6', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loc6_loc', to='web.Location')),
                ('loc7', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loc7_loc', to='web.Location')),
                ('loc8', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loc8_loc', to='web.Location')),
                ('loc9', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loc9_loc', to='web.Location')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Sales',
        ),
    ]
