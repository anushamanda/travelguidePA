# Generated by Django 3.0.5 on 2020-04-16 03:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advisors', '0003_advisor_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advisor',
            old_name='email',
            new_name='advisor_email',
        ),
    ]
