# Generated by Django 5.1.1 on 2024-09-25 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0002_rename_descicao_fotografia_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='categoria',
            field=models.CharField(choices=[('NEBULOSA', 'Nebulosa'), ('ESTRELA', 'Estrela'), ('GALAXIA', 'Galáxia'), ('PLANETA', 'Planeta')], default='', max_length=100),
        ),
    ]
