# Generated by Django 5.0.1 on 2024-02-14 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petstoreapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='pet_images/'),
        ),
    ]
