# Generated by Django 4.1.3 on 2022-12-05 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productcomment',
            options={'ordering': ['-publication_date_and_time']},
        ),
    ]
