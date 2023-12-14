# Generated by Django 4.2.8 on 2023-12-14 17:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("zilencer", "0053_remoterealmauditlog_acting_remote_user_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="remoterealmbillinguser",
            name="enable_maintenance_release_emails",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="remoterealmbillinguser",
            name="enable_major_release_emails",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="remoteserverbillinguser",
            name="enable_maintenance_release_emails",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="remoteserverbillinguser",
            name="enable_major_release_emails",
            field=models.BooleanField(default=True),
        ),
    ]