# Generated by Django 4.1 on 2022-09-04 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppMetal', '0004_rename_anio_fundacion_grupos_fundacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('comision', models.IntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Ingresante',
            new_name='Ingresantes',
        ),
        migrations.DeleteModel(
            name='Grupos',
        ),
        migrations.DeleteModel(
            name='Subgenero',
        ),
    ]
