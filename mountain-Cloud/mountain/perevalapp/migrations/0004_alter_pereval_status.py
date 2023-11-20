# Generated by Django 4.2.7 on 2023-11-12 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perevalapp', '0003_alter_images_pereval_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pereval',
            name='status',
            field=models.CharField(choices=[('NEW', 'новая информация'), ('ACCEPTED', 'модератор взял в работу'), ('PENDING', 'модерация прошла успешно'), ('REJECTED', 'модерация прошла, информация не принята')], default='NEW', max_length=10),
        ),
    ]
