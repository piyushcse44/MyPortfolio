# Generated by Django 4.2.6 on 2023-10-26 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyPortfolioApp', '0006_profile_frontphoto1'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='subject',
            field=models.CharField(default='a little bit about Joshua', max_length=200),
        ),
    ]
