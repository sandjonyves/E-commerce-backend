# Generated by Django 5.0.3 on 2024-05-23 11:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
        ('store', '0006_piece_id_marque'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piece',
            name='id_marque',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='marque', to='app.marque'),
        ),
    ]
