# Generated by Django 2.2.6 on 2019-11-19 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_auto_20191119_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='mobile_no',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]