# Generated by Django 4.1.3 on 2022-11-15 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('money_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('spare', models.FloatField(default=0)),
                ('tax', models.FloatField(default=0)),
                ('type', models.CharField(choices=[('INCOME', 'Income'), ('EXPENSE', 'Expense'), ('TRANSFER', 'Transfer')], default='EXPENSE', max_length=10)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='money_management.category')),
            ],
        ),
        migrations.DeleteModel(
            name='Todo',
        ),
    ]
