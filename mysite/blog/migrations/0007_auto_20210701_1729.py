# Generated by Django 3.2.4 on 2021-07-01 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_particle_pcluster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='cluster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.cluster', unique=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.CharField(max_length=2000, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='headline',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='cluster',
            name='cluster_no',
            field=models.IntegerField(default=0, unique=True),
        ),
        migrations.AlterField(
            model_name='particle',
            name='cluster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.pcluster', unique=True),
        ),
        migrations.AlterField(
            model_name='particle',
            name='content',
            field=models.CharField(max_length=2000, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='particle',
            name='headline',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='pcluster',
            name='cluster_no',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]