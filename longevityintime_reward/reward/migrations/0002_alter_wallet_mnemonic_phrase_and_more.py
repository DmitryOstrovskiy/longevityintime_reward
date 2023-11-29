# Generated by Django 4.2.7 on 2023-11-29 12:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reward', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='mnemonic_phrase',
            field=models.TextField(blank=True, null=True, verbose_name='Mnemonic Phrase'),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='private_key',
            field=models.TextField(blank=True, null=True, verbose_name='Rrivate Key'),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='public_key',
            field=models.TextField(blank=True, null=True, verbose_name='Public Key'),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='wallet_address',
            field=models.CharField(blank=True, max_length=254, null=True, verbose_name='Wallet Address'),
        ),
        migrations.CreateModel(
            name='TestCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Name of the analysis')),
                ('parameter', models.TextField(verbose_name='Name of the parameter')),
                ('parameter_value', models.TextField(verbose_name='Parameter value')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='testcards', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]