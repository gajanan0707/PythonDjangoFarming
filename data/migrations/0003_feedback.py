# Generated by Django 2.2.6 on 2019-11-07 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_owner', '0006_auto_20191106_0946'),
        ('data', '0002_contact_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farmer_name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('details', models.TextField()),
                ('happy', models.BooleanField()),
                ('date', models.DateField(auto_now_add=True)),
                ('title', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Feedback', to='admin_owner.Blog')),
            ],
        ),
    ]
