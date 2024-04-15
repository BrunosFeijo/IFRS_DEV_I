# Generated by Django 5.0.2 on 2024-04-09 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trabalho', '0004_alter_producao_titulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='producao',
            name='classificacao',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producao',
            name='especificacoes',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producao',
            name='sinopse',
            field=models.CharField(default=3, max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='producao',
            name='titulo',
            field=models.CharField(max_length=200),
        ),
    ]