# Generated by Django 3.1.1 on 2020-09-21 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0011_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'reviews',
            },
        ),
    ]