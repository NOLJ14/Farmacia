# Generated by Django 3.1.3 on 2021-01-18 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Medicamentos', '0005_auto_20210118_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='idProducto',
            field=models.IntegerField(default='', editable=False, primary_key=True, serialize=False),
        ),
    ]