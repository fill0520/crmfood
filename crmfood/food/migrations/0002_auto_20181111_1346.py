# Generated by Django 2.1.2 on 2018-11-11 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='roleid',
            new_name='departmentid',
        ),
    ]