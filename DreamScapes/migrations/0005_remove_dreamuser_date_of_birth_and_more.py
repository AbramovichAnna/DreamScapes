# Generated by Django 4.2.4 on 2023-08-07 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("DreamScapes", "0004_alter_dreamuser_email"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="dreamuser",
            name="date_of_birth",
        ),
        migrations.AlterField(
            model_name="dreamuser",
            name="profile_picture",
            field=models.ImageField(
                blank=True, null=True, upload_to="profile_pictures/"
            ),
        ),
    ]