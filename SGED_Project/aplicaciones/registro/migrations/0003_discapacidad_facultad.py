# Generated by Django 4.2.1 on 2023-05-14 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0002_alter_discapacidad_cantidad_discapacitados_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='discapacidad',
            name='facultad',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='registro.facultad'),
            preserve_default=False,
        ),
    ]