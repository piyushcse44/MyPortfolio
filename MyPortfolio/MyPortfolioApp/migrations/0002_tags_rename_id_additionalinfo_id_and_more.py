# Generated by Django 4.2.6 on 2023-10-26 13:55

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('MyPortfolioApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('Id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('Name', models.CharField(default='Django', max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='additionalinfo',
            old_name='id',
            new_name='Id',
        ),
        migrations.RenameField(
            model_name='competitiveplateform',
            old_name='id',
            new_name='Id',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='id',
            new_name='Id',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='id',
            new_name='Id',
        ),
        migrations.AlterField(
            model_name='additionalinfo',
            name='ProjectFinished',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='competitiveplateform',
            name='Photo',
            field=models.ImageField(default='images/default.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='FrontPhoto',
            field=models.ImageField(default='images/default.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='Photo',
            field=models.ImageField(default='images/default.png', upload_to=''),
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('Id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('CompanyName', models.CharField(default='Codechef', max_length=200)),
                ('Position', models.CharField(default='DoubtSolver', max_length=200)),
                ('Location', models.CharField(default='Delhi', max_length=200)),
                ('Start_Duration', models.DateField(default='2023-02-02')),
                ('End_Duration', models.DateField(default='2023-06-02')),
                ('Description', models.TextField(max_length=200)),
                ('Tags', models.ManyToManyField(blank=True, null=True, to='MyPortfolioApp.tags')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='Experience',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='MyPortfolioApp.experience'),
        ),
    ]
