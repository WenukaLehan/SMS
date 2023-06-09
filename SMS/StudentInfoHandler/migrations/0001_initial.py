# Generated by Django 4.1.6 on 2023-03-15 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('GuardianInfoHandler', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('index_number', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('full_name', models.CharField(max_length=255)),
                ('name_with_initials', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=1)),
                ('enrolled_date', models.DateField(auto_now=True)),
                ('address', models.TextField()),
                ('alumni_status', models.BooleanField(default=False)),
                ('special_notes', models.JSONField()),
                ('class_info', models.CharField(max_length=10)),
                ('RFID_key', models.CharField(max_length=25)),
                ('Guardian', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GuardianInfoHandler.guardianinfo')),
            ],
        ),
        migrations.CreateModel(
            name='ParentInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mother_name', models.CharField(max_length=255)),
                ('mother_status', models.BooleanField(default=True)),
                ('mother_special_notes', models.JSONField()),
                ('father_name', models.CharField(max_length=255)),
                ('father_status', models.BooleanField(default=True)),
                ('father_special_notes', models.JSONField()),
                ('student_index_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudentInfoHandler.studentinfo')),
            ],
        ),
    ]
