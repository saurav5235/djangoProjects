# Generated by Django 4.2.18 on 2025-02-05 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='Item_desc',
            new_name='item_desc',
        ),
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://blocks.astratic.com/img/general-img-portrait.png', max_length=500),
        ),
    ]
