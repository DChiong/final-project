# Generated by Django 5.2.1 on 2025-05-10 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_studentrecord_delete_studentperformance'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentrecord',
            name='student_id',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
