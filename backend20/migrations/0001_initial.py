# Generated by Django 3.1.1 on 2020-12-01 04:38

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
                ('category', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'test_DB20',
                'ordering': ('id',),
            },
        ),
    ]
