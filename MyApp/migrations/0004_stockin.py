# Generated by Django 4.0.5 on 2022-07-05 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0003_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='stockin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stockinid', models.CharField(max_length=30)),
                ('pid', models.CharField(max_length=30)),
                ('pcatid', models.CharField(max_length=30)),
                ('supid', models.CharField(max_length=30)),
                ('datein', models.CharField(max_length=30)),
                ('quantity', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'stockin',
            },
        ),
    ]
