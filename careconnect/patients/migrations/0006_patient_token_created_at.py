# Generated by Django 5.2.3 on 2025-06-28 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0005_patient_token_used'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='token_created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
