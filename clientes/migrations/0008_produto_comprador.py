# Generated by Django 4.2.5 on 2023-09-09 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0007_alter_produto_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='comprador',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente'),
        ),
    ]
