# Generated by Django 3.2.9 on 2023-02-04 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20230204_0611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='user',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
