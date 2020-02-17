# Generated by Django 3.0.3 on 2020-02-17 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(default=101, max_length=255)),
                ('state', models.CharField(default=101, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(help_text='Enter your email', max_length=254, unique=True)),
                ('location', models.ForeignKey(default=101, help_text='Enter your location', on_delete=django.db.models.deletion.SET_DEFAULT, to='signup.Location')),
            ],
        ),
    ]
