# Generated by Django 3.0.1 on 2020-03-05 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0004_auto_20200212_2328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='op_food',
            name='id_categorie',
        ),
        migrations.AddField(
            model_name='op_food',
            name='categorie',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='search.categorie'),
            preserve_default=False,
        ),
    ]