# Generated by Django 5.0.3 on 2024-05-05 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TPO_app', '0007_student_branch_student_prn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='prn',
            field=models.IntegerField(default='001'),
        ),
    ]
