# Generated by Django 4.0.5 on 2022-07-05 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='productcat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pcatid', models.CharField(max_length=30)),
                ('catname', models.CharField(max_length=30)),
                ('desc', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'productcat',
            },
        ),
    ]
