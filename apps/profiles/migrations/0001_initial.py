# Generated by Django 4.1.2 on 2022-10-13 21:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pseudo', models.CharField(blank=True, max_length=48, unique=True)),
                ('bio', models.CharField(blank=True, max_length=360)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('profile_picture', models.ImageField(blank=True, default='https://res.cloudinary.com/doysjtoym/image/upload/v1/cloneTwitter/default/profilePic_hbvouc', null=True, upload_to='cloneTwitter/media/profile')),
                ('cover_picture', models.ImageField(blank=True, default='https://res.cloudinary.com/doysjtoym/image/upload/v1/cloneTwitter/default/coverPic_dbaax4', null=True, upload_to='cloneTwitter/media/cover')),
                ('isUploadProfilePic', models.BooleanField(default=False)),
                ('isUploadCoverPic', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
                'ordering': ('-created',),
            },
        ),
    ]
