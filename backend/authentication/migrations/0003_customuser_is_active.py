# Generated by Django 4.2.3 on 2024-06-17 14:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0002_customuser_registered_at_alter_customuser_email"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="is_active",
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]