# Generated by Django 2.2.6 on 2019-11-15 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0003_auto_20191115_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propiedad',
            name='imagen',
            field=models.ImageField(default='images/bg.jpg', upload_to='images'),
        ),
    ]
