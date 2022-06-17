# Generated by Django 4.0.5 on 2022-06-14 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appserv', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appli',
            name='serveur',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='appli',
            name='utilisateur',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='service',
            name='serveur_lancement',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='serveur',
        ),
        migrations.DeleteModel(
            name='type',
        ),
        migrations.DeleteModel(
            name='utilisateur',
        ),
    ]