# Generated by Django 4.1.5 on 2023-02-24 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_dastavka_delete_mymodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='dastavka',
            name='all_price',
            field=models.PositiveBigIntegerField(blank=True, default=0, null=True),
        ),
    ]
