# Generated by Django 4.2.6 on 2023-10-26 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyPortfolioApp', '0002_tags_rename_id_additionalinfo_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='Experience',
        ),
        migrations.AlterField(
            model_name='experience',
            name='Tags',
            field=models.ManyToManyField(to='MyPortfolioApp.tags'),
        ),
    ]
