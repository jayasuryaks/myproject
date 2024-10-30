# Generated by Django 5.1.2 on 2024-10-22 12:06

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bankmodel',
            options={'ordering': ['-updated_at']},
        ),
        migrations.RenameField(
            model_name='bankmodel',
            old_name='accountnumber',
            new_name='account_number',
        ),
        migrations.RenameField(
            model_name='bankmodel',
            old_name='accountType',
            new_name='account_type',
        ),
        migrations.AddField(
            model_name='bankmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bankmodel',
            name='deposit',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bankmodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterModelTable(
            name='bankmodel',
            table='bank_details',
        ),
        migrations.DeleteModel(
            name='Moneymanagement',
        ),
    ]