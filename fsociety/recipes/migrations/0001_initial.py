# Generated by Django 2.1.6 on 2019-02-18 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ingredients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField(blank=True)),
                ('recipe_summary', models.TextField(blank=True)),
                ('quantity', models.IntegerField(blank=True, default=0)),
                ('preparation_time', models.IntegerField(blank=True, default=0)),
                ('cooking_time', models.IntegerField(blank=True, default=0)),
                ('difficulty', models.CharField(choices=[('Easy', 'Easy'), ('Medium', 'Medium'), ('Advanced', 'Advanced')], default='Easy', max_length=10)),
                ('hint', models.TextField(blank=True)),
                ('ingredients', models.ManyToManyField(blank=True, to='ingredients.Ingredient')),
            ],
        ),
    ]
