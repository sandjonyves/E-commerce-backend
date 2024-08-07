# Generated by Django 5.0.3 on 2024-06-13 14:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_otherclient'),
        ('store', '0009_merge_20240607_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='operator',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='commande',
            name='transaction_id',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='commande',
            name='client_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='commande_id', to='account.otherclient'),
        ),
    ]
