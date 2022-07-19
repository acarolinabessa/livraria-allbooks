# Generated by Django 4.0.6 on 2022-07-19 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='estado',
            field=models.CharField(choices=[('maranhão', 'Maranhão'), ('ceará', 'Ceará')], default='Escolha...', max_length=100),
        ),
        migrations.AddField(
            model_name='compra',
            name='pais',
            field=models.CharField(choices=[('brasil', 'Brasil'), ('usa', 'Estados Unicos')], default='Escolha...', max_length=100),
        ),
    ]