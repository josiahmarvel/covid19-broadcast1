# Generated by Django 3.1.6 on 2021-02-24 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0005_auto_20210224_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='biography',
            field=models.TextField(blank=True, help_text='Enter biography here', max_length=5000, null=True),
        ),
    ]
