# Generated by Django 4.0.5 on 2022-07-05 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0002_productcat'),
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.CharField(max_length=30)),
                ('pcatid', models.CharField(max_length=30)),
                ('productname', models.CharField(max_length=30)),
                ('unit', models.CharField(max_length=30)),
                ('priceperunit', models.CharField(max_length=30)),
                ('openqty', models.CharField(max_length=30)),
                ('currentqty', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'products',
            },
        ),
    ]
