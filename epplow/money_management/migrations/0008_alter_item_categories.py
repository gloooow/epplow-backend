# Generated by Django 4.1.3 on 2022-11-17 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('money_management', '0007_alter_item_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='categories',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='money_management.category'),
        ),
    ]
