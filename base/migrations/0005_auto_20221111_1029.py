# Generated by Django 3.2.15 on 2022-11-11 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_remove_remark_approved'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='remark',
            options={'ordering': ['-publish_date']},
        ),
        migrations.AddField(
            model_name='cocktail',
            name='alcoholic',
            field=models.BooleanField(default=True),
        ),
    ]
