# Generated by Django 2.2 on 2019-07-21 03:59

from django.db import migrations
import shortuuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20190708_2046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseorder',
            name='id',
        ),
        migrations.AddField(
            model_name='courseorder',
            name='uid',
            field=shortuuidfield.fields.ShortUUIDField(blank=True, editable=False, max_length=22, primary_key=True, serialize=False),
        ),
    ]
