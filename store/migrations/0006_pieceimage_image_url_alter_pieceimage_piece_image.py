# Generated by Django 5.0.4 on 2024-05-17 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_pieceimage_public_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='pieceimage',
            name='image_url',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='pieceimage',
            name='piece_image',
            field=models.ImageField(blank=True, default='', upload_to='Pieces/images/'),
        ),
    ]
