# Generated by Django 4.0.5 on 2022-06-23 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img1', models.ImageField(upload_to='media', verbose_name='HomePage img1')),
                ('img2', models.ImageField(upload_to='media', verbose_name='HomePage img2')),
                ('img3', models.ImageField(upload_to='media', verbose_name='HomePage img3')),
                ('name1', models.CharField(max_length=50, verbose_name='HomePage name1')),
                ('name2', models.CharField(max_length=60, verbose_name='HomePage name2')),
                ('name3', models.CharField(max_length=70, verbose_name='HomePage name3')),
                ('about', models.TextField(verbose_name='HomePage about')),
                ('number', models.CharField(max_length=30, verbose_name='HomePage number')),
            ],
            options={
                'verbose_name': 'Home',
                'verbose_name_plural': 'Homes',
            },
        ),
    ]
