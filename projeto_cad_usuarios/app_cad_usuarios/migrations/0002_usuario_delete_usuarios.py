# Generated by Django 4.2 on 2023-04-11 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cad_usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(max_length=255)),
                ('cidade', models.TextField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Usuarios',
        ),
    ]
