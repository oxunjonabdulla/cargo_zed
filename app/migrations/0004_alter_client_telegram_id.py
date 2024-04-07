# Generated by Django 5.0.4 on 2024-04-07 09:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_client_given_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='telegram_id',
            field=models.CharField(help_text='The Telegram ID of the client.', max_length=50, unique=True, validators=[django.core.validators.RegexValidator(message='Telegram ID must contain only numbers.', regex='^[0-9]+$')]),
        ),
    ]
