# Generated by Django 4.2.6 on 2023-10-26 14:44

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('MyPortfolioApp', '0004_profile_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('Id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('FirstName', models.CharField(default='Piyush', max_length=200)),
                ('LastName', models.CharField(default='Kumar', max_length=200)),
                ('Email', models.EmailField(default='piyushkumarcse44@gmail.com', max_length=200)),
                ('Subject', models.CharField(blank=True, max_length=200, null=True)),
                ('Description', models.TextField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='experience',
            name='Certificate',
            field=models.ImageField(default='images/default.png', upload_to=''),
        ),
        migrations.AddField(
            model_name='experience',
            name='CompanyLogo',
            field=models.ImageField(default='images/default.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='competitiveplateform',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='MyPortfolioApp.user'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='AdditionalInfo',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='MyPortfolioApp.additionalinfo'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='Experience',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.PROTECT, to='MyPortfolioApp.experience'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='User',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='MyPortfolioApp.user'),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('Id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('Title', models.CharField(default='Directory For Developer', max_length=200)),
                ('TeamSize', models.IntegerField(default=4)),
                ('Role', models.CharField(default='Backend Developer', max_length=200)),
                ('Start_Duration', models.DateField(default='2023-02-02')),
                ('End_Duration', models.DateField(default='2023-06-02')),
                ('ProjectImage', models.ImageField(default='images/defaule.png', upload_to='')),
                ('Description', models.TextField(max_length=200)),
                ('GithubLink', models.URLField(default='github.com')),
                ('LiveLink', models.URLField(default='Pythonanywhere.com')),
                ('Profile', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='MyPortfolioApp.profile')),
                ('Tags', models.ManyToManyField(to='MyPortfolioApp.tags')),
            ],
        ),
    ]