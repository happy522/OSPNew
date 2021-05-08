# Generated by Django 3.2 on 2021-04-25 13:56

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Adhar_Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anumber', models.CharField(max_length=12)),
                ('fname', models.CharField(max_length=20)),
                ('mname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE')], default='', max_length=1)),
                ('address', models.CharField(max_length=1000)),
                ('contact', models.CharField(max_length=10)),
                ('dob', models.DateField(default=datetime.datetime.now)),
                ('cast', models.CharField(choices=[('General', 'General'), ('SC', 'SC'), ('ST', 'ST'), ('OBC', 'OBC'), ('Other', 'Other')], default='General', max_length=50)),
                ('scan', models.FileField(blank=True, upload_to='files')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anumber', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('cno', models.CharField(max_length=15)),
                ('message', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Govt_Bodiess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='pics')),
                ('type', models.CharField(choices=[('School', 'School'), ('College', 'College'), ('Hospital', 'Hospital'), ('Police Station', 'Police Station'), ('Court', 'Court'), ('Office', 'Office')], default='School', max_length=50)),
                ('address', models.CharField(max_length=1000)),
                ('contact', models.CharField(max_length=15)),
                ('desc', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Policiess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('policies_for', models.CharField(choices=[('Farmer', 'Farmer'), ('House wife', 'House wife'), ('Self-Employed', 'Self-Employed'), ('Doctor', 'Doctor'), ('Government-Job', 'Government-Job'), ('Student', 'Student'), ('Other', 'Other')], max_length=50)),
                ('logo', models.ImageField(upload_to='pics')),
                ('type', models.CharField(choices=[('Subsidy', 'Subsidy'), ('Scheme', 'Scheme')], default='Subsidy', max_length=50)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('desc', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Post_Announcements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='pics')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('doc', models.FileField(blank=True, upload_to='files')),
            ],
        ),
        migrations.CreateModel(
            name='Post_Bills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='pics')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('desc', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Post_Newss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='pics')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('desc', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Upload_doc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Adhar_card', models.FileField(default='None', upload_to='files')),
                ('Pan_card', models.FileField(default='None', upload_to='files')),
                ('Voterid_card', models.FileField(default='None', upload_to='files')),
                ('Rashan_card', models.FileField(default='None', upload_to='files')),
                ('Passport', models.FileField(default='None', upload_to='files')),
                ('R_C_Book', models.FileField(default='None', upload_to='files')),
                ('Driving_licence', models.FileField(default='None', upload_to='files')),
                ('Income_certi', models.FileField(default='None', upload_to='files')),
                ('Noncriminal_certi', models.FileField(default='None', upload_to='files')),
                ('Other', models.FileField(default='None', upload_to='files')),
                ('anumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('r_id', models.AutoField(primary_key=True, serialize=False)),
                ('anumber', models.CharField(max_length=20)),
                ('role', models.CharField(choices=[('Citizen', 'Citizen'), ('Government_Employee', 'Government_Employee')], max_length=50)),
                ('contact', models.CharField(max_length=20)),
                ('occupation', models.CharField(choices=[('Farmer', 'Farmer'), ('House wife', 'House wife'), ('Self-Employed', 'Self-Employed'), ('Doctor', 'Doctor'), ('Government-Job', 'Government-Job'), ('Student', 'Student'), ('Other', 'Other')], max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]