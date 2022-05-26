# Generated by Django 4.0.4 on 2022-05-26 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_application', '0005_rename_working experience_jobapplication_working_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='CGPA',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='working_experience',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
    ]
