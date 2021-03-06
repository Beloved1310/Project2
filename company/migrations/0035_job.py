# Generated by Django 3.1.1 on 2020-10-01 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0034_delete_job'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=500)),
                ('company', models.CharField(max_length=500)),
                ('company2', models.CharField(max_length=500)),
                ('company3', models.CharField(max_length=500)),
                ('location', models.CharField(max_length=500)),
                ('amount', models.CharField(max_length=500)),
                ('amount2', models.CharField(max_length=500)),
                ('amount3', models.CharField(max_length=500)),
                ('requirements', models.TextField()),
                ('requirements2', models.TextField()),
                ('requirements3', models.TextField()),
                ('details', models.TextField()),
                ('url', models.CharField(max_length=200)),
                ('url2', models.CharField(max_length=200)),
                ('url3', models.CharField(max_length=200)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
    ]
