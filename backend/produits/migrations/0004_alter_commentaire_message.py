# Generated by Django 3.2.20 on 2024-01-15 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produits', '0003_commentaire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentaire',
            name='message',
            field=models.TextField(),
        ),
    ]
