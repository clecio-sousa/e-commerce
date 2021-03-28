# Generated by Django 3.0.7 on 2020-06-26 21:14

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='publicado',
            new_name='ativado',
        ),
        migrations.AddField(
            model_name='produto',
            name='data_alteracao',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='data_criacao',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='produto',
            name='data_publicacao',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 26, 18, 12, 13, 602789)),
        ),
    ]
