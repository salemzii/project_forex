# Generated by Django 3.1.1 on 2020-10-07 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Forex_blog', '0002_auto_20201007_0711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_on',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Forex_blog.post'),
        ),
    ]