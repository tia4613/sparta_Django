# Generated by Django 4.2 on 2024-04-19 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='articles.article'),
        ),
    ]
