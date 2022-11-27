# Generated by Django 4.1.2 on 2022-11-02 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barApp', '0007_alter_producto_imagen_p'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='categoria_P',
            field=models.CharField(choices=[('hot', 'Bebidas calientes'), ('cold', 'Bebidas frías'), ('food', 'Alimentos')], max_length=45, verbose_name='Categoria del producto'),
        ),
    ]