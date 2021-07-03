# Generated by Django 3.2.4 on 2021-06-30 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clusters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cluster_no', models.IntegerField(default=0)),
                ('total_items', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='articles',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='articles',
            name='headline',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='articles',
            name='cluster',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='blog.clusters'),
            preserve_default=False,
        ),
    ]