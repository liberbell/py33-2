# Generated by Django 3.1.7 on 2021-03-11 00:13

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='category_name')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created_date')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('text', models.TextField(verbose_name='content')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created_date')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.category', verbose_name='category')),
            ],
        ),
    ]
