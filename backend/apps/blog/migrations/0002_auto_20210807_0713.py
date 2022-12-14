# Generated by Django 3.2.6 on 2021-08-07 07:13

from django.db import migrations


def create_homepage(apps, schema_editor):
    # Get models
    ContentType = apps.get_model("contenttypes.ContentType")
    Page = apps.get_model("wagtailcore.Page")
    Site = apps.get_model("wagtailcore.Site")
    Locale = apps.get_model("wagtailcore.Locale")
    BlogIndexPage = apps.get_model("blog.BlogIndexPage")

    # Delete the default homepage
    # If migration is run multiple times, it may have already been deleted
    Page.objects.filter(id=2).delete()

    # Create content type for homepage model
    homepage_content_type, __ = ContentType.objects.get_or_create(
        model="blogindexpage", app_label="blog"
    )

    # Create a new homepage
    homepage = BlogIndexPage.objects.create(
        title="Blog",
        intro="Super awesome blog powered by Wagtail CMS",
        draft_title="Blog",
        slug="blog",
        content_type=homepage_content_type,
        path="00010001",
        depth=2,
        numchild=0,
        url_path="/home/",
        locale=Locale.objects.first(),
    )

    # Create a site with the new homepage set as the root
    Site.objects.create(hostname="localhost", root_page=homepage, is_default_site=True)


def remove_homepage(apps, schema_editor):
    # Get models
    ContentType = apps.get_model("contenttypes.ContentType")
    BlogIndexPage = apps.get_model("blog.BlogIndexPage")

    # Delete the default homepage
    # Page and Site objects CASCADE
    BlogIndexPage.objects.filter(slug="blog", depth=2).delete()

    # Delete content type for homepage model
    ContentType.objects.filter(model="blogindexpage", app_label="blog").delete()


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_homepage, remove_homepage),
    ]
