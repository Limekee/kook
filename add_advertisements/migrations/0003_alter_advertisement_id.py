# Generated by Django 4.2.4 on 2023-08-25 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('add_advertisements', '0002_alter_advertisement_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='id',
            field=models.CharField(max_length=64, primary_key=True, serialize=False, verbose_name='id'),
        ),
    ]