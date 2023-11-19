# Generated by Django 4.2.3 on 2023-11-19 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remove_bg', '0002_images_image_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='converted_image',
            field=models.ImageField(default=1, upload_to='bg_removed_images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]