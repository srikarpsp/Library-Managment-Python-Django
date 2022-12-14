# Generated by Django 2.0 on 2018-05-21 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookId', models.IntegerField(blank=True, null=True)),
                ('bookname', models.CharField(blank=True, max_length=120, null=True)),
                ('author', models.CharField(blank=True, max_length=120, null=True)),
                ('publication', models.CharField(blank=True, max_length=120, null=True)),
                ('published', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Types', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='Books',
            name='Types',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='library_management.Books'),
        ),
        migrations.AddField(
            model_name='admin',
            name='Books',
            field=models.ManyToManyField(to='library_management.Books'),
        ),
    ]
