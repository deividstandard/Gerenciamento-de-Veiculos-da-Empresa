# Generated by Django 3.0.2 on 2020-01-27 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200127_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carro',
            name='id_carro',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='cdc',
            name='id_cdc',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='registro',
            name='id_registro',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
