# Generated by Django 3.1.3 on 2021-07-09 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='country',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='place',
            name='image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='images/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='place',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]