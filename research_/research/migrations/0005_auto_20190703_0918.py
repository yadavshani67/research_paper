# Generated by Django 2.2.2 on 2019-07-03 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0004_auto_20190702_0408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='attachment',
            field=models.FileField(upload_to='documents/'),
        ),
    ]