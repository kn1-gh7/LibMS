# Generated by Django 4.2.7 on 2023-11-06 00:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_librarydb_not_more_books_issued_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booksandusers',
            name='t_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.transactions'),
            preserve_default=False,
        ),
    ]
