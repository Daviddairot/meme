# Generated by Django 4.2.2 on 2023-08-01 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "bloggerapp",
            "0005_remove_post_likes_remove_post_video_post_date_posted_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="video",
            field=models.FileField(blank=True, null=True, upload_to="videos/"),
        ),
    ]
