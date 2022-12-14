# Generated by Django 4.1.3 on 2022-11-27 12:53

from django.db import migrations, models
import magazinslunce.common.validators


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_appuser_profile_picture_alter_appuser_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures', validators=[magazinslunce.common.validators.validate_file_size]),
        ),
    ]
