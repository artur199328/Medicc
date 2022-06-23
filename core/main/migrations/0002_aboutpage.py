# Generated by Django 4.0.5 on 2022-06-23 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=50, verbose_name='AboutPage name1')),
                ('about1', models.TextField(verbose_name='AboutPage about1')),
                ('about2', models.TextField(verbose_name='HomePage about2')),
                ('year', models.IntegerField(verbose_name='AboutPage year')),
                ('name2', models.CharField(max_length=60, verbose_name='AboutPage name2')),
                ('name3', models.CharField(max_length=70, verbose_name='AboutPage name3')),
                ('img1', models.ImageField(upload_to='media', verbose_name='AboutPage img1')),
                ('img2', models.ImageField(upload_to='media', verbose_name='AboutPage img2')),
            ],
            options={
                'verbose_name': 'About',
                'verbose_name_plural': 'Abouts',
            },
        ),
    ]