# Generated by Django 5.1 on 2024-08-14 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donors', '0003_alter_donor_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='last_donated_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='donor',
            name='next_estimated_donating_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
