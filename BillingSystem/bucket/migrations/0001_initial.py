# Generated by Django 3.2.6 on 2021-09-29 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=30)),
                ('price', models.FloatField(max_length=7)),
                ('tax', models.FloatField(default=0.0, max_length=3)),
                ('description', models.CharField(max_length=70, null=True)),
            ],
        ),
    ]