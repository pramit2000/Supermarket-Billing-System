# Generated by Django 3.2.6 on 2021-10-05 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emp_reg',
            name='gender',
            field=models.CharField(default='Male', max_length=6),
        ),
        migrations.AlterField(
            model_name='emp_reg',
            name='contact_no',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='emp_reg',
            name='pin_code',
            field=models.IntegerField(),
        ),
    ]
