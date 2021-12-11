# Generated by Django 3.2.9 on 2021-12-10 19:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('qr_app', '0002_remove_attendance_qr_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='qr_code',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='image/'),
            preserve_default=False,
        ),
    ]
