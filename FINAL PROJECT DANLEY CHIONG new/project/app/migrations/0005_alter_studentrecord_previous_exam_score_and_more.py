# Generated by Django 5.2.1 on 2025-05-10 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_studentrecord_student_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentrecord',
            name='previous_exam_score',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='studentrecord',
            name='study_hours',
            field=models.CharField(max_length=255),
        ),
    ]
