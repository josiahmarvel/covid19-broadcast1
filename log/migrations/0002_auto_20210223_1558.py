# Generated by Django 3.1.6 on 2021-02-23 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='speech',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='speech',
            name='summary',
            field=models.TextField(help_text='Enter speech here', max_length=1000),
        ),
    ]