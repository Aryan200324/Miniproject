# Generated by Django 5.0.3 on 2024-05-05 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TPO_app', '0011_student_prn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='branch',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='prn',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
