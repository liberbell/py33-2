# Generated by Django 3.1.7 on 2021-03-16 05:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='nemo', max_length=30, verbose_name='name')),
                ('text', models.TextField(verbose_name='text')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created_date')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.post', verbose_name='linkedcontent')),
            ],
        ),
    ]
