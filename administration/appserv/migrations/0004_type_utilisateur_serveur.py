# Generated by Django 4.0.5 on 2022-06-16 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appserv', '0003_alter_appli_id_alter_service_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('mail', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='serveur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('proc', models.IntegerField()),
                ('mem', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('type', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='appserv.type')),
            ],
        ),
    ]
