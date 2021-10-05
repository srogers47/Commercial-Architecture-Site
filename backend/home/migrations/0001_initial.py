# Generated by Django 3.2.7 on 2021-10-05 01:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(default=' ', upload_to='')),
                ('featured', models.BooleanField(default=False, help_text='Check this box if you want the images to render in the featured work carousel.')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='images/')),
                ('posts', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='images_post', to='home.blogpost')),
            ],
        ),
    ]
