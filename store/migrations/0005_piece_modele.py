# Generated by Django 5.0.3 on 2024-05-23 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_pieceimage_thumbs'),
    ]

    operations = [
        migrations.AddField(
            model_name='piece',
            name='modele',
            field=models.CharField(default='4x4', max_length=512),
        ),
    ]
