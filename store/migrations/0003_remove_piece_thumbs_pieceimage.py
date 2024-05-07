# Generated by Django 5.0.3 on 2024-05-07 13:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_piece_id_marchand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='piece',
            name='thumbs',
        ),
        migrations.CreateModel(
            name='PieceImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('piece_image', models.ImageField(blank=True, upload_to='Pieces/images/')),
                ('thumbs', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='pieceImage', to='store.piece')),
            ],
        ),
    ]
