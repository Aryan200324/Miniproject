# Generated by Django 5.0.3 on 2024-05-05 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TPO_app', '0010_remove_student_prn'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='prn',
            field=models.IntegerField(null=True),
        ),
    ]
