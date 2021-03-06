# Generated by Django 3.2.6 on 2021-08-14 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('synopsis', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animelist.anime')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animelist.user')),
            ],
        ),
        migrations.CreateModel(
            name='CurrentlyWatching',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animelist.anime')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animelist.user')),
            ],
        ),
        migrations.CreateModel(
            name='CompletedAnime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animelist.anime')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animelist.user')),
            ],
        ),
    ]
