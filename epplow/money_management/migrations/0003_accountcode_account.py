# Generated by Django 4.1.3 on 2022-11-15 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('money_management', '0002_category_item_delete_todo'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('balance', models.FloatField(default=0)),
                ('currency', models.CharField(choices=[('RON', 'Ron'), ('PLN', 'Pln'), ('EUR', 'Eur'), ('USD', 'Usd')], default='RON', max_length=10)),
                ('code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='money_management.accountcode')),
            ],
        ),
    ]
