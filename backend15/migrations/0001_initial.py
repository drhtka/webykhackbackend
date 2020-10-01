# Generated by Django 3.1.1 on 2020-10-01 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreateDb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('tovarname', models.CharField(blank=True, max_length=30, null=True)),
                ('price', models.CharField(blank=True, max_length=30, null=True)),
                ('sale', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'test_DB15',
                'ordering': ('id',),
            },
        ),
    ]
