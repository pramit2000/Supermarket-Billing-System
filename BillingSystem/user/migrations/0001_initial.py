# Generated by Django 3.2.6 on 2021-10-05 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='emp_reg',
            fields=[
                ('emp_id', models.IntegerField(auto_created=True)),
                ('email_id', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=30)),
                ('dateOfBirth', models.DateField()),
                ('contact_no', models.IntegerField(max_length=10)),
                ('city', models.CharField(max_length=25)),
                ('state', models.CharField(max_length=25)),
                ('pin_code', models.IntegerField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='emp_login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_id', models.EmailField(max_length=254)),
                ('password', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.emp_reg')),
            ],
        ),
    ]
