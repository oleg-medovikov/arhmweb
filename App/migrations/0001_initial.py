# Generated by Django 4.1.7 on 2023-03-03 20:18

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('node_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name_node', models.CharField(max_length=50)),
                ('declension', models.CharField(max_length=50)),
                ('contact_list_id', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('district', models.CharField(max_length=50)),
                ('district_id', models.IntegerField()),
                ('street', models.BooleanField(default=False)),
                ('dict', models.BooleanField(default=False)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
