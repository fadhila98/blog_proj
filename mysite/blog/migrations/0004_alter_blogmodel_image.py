# Generated by Django 4.1.6 on 2023-02-16 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blogmodel_options_alter_blogmodel_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='image',
            field=models.ImageField(upload_to='img/%y'),
        ),
    ]
