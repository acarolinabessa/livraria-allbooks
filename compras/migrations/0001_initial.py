# Generated by Django 4.0.6 on 2022-07-19 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('codigo', models.BigAutoField(primary_key=True, serialize=False)),
                ('efetuada_em', models.DateTimeField(auto_now_add=True)),
                ('nome_do_cliente', models.CharField(max_length=100)),
                ('sobrenome_do_cliente', models.CharField(max_length=100)),
                ('usuario', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('endereco', models.CharField(max_length=100)),
                ('segundo_endereco', models.CharField(blank=True, max_length=100)),
                ('CEP', models.BigIntegerField()),
                ('forma_pagamento', models.CharField(choices=[('cartão_de_débito', 'Cartão de Débito'), ('cartão_de_crédito', 'Cartão de Crédito'), ('boleto', 'Boleto'), ('pix', 'Pix')], max_length=17)),
                ('nome_no_cartao', models.CharField(max_length=100)),
                ('numero_do_cartao', models.BigIntegerField()),
                ('validade_do_cartao', models.CharField(max_length=5)),
                ('cvv', models.IntegerField()),
            ],
        ),
    ]
