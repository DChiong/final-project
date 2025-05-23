# Generated by Django 5.1.5 on 2025-05-09 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentPerformance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours_studied', models.FloatField()),
                ('attendance', models.FloatField()),
                ('previous_grade', models.FloatField()),
                ('assignments_completed', models.IntegerField()),
                ('passed', models.BooleanField(blank=True, null=True)),
            ],
        ),
    ]
