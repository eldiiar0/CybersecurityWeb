from django.db import models
import os


def save_news_img(instance, filename):
	extension = filename.split('.')[-1]
	new_filename = f"{instance.title}'_'{instance.date}.{extension}"
	
	return  os.path.join('news/', new_filename) 


def save_events_img(instance, filename):
	extension = filename.split('.')[-1]
	new_filename = f"{instance.title}'_'{instance.date}.{extension}"
	
	return  os.path.join('events/', new_filename) 


def save_logo(instance, filename):
	extension = filename.split('.')[-1]
	new_filename = f"{instance.name}.{extension}"
	
	return  os.path.join('logos/', new_filename)


def save_info_img(instance, filename):
	extension = filename.split('.')[-1]
	new_filename = f"{instance.title}'_info'.{extension}"
	return  os.path.join('info/', new_filename)



class News(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()
	date = models.DateField(auto_now_add=True)
	image = models.ImageField(upload_to=save_news_img)

	
class Events(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()
	date = models.DateField(auto_now_add=True)
	image = models.ImageField(upload_to=save_events_img, blank=True)


class HomePage(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	image = models.ImageField(upload_to=save_info_img, blank=True)


class HomePageInfos(models.Model):
	title = models.CharField(max_length=255, blank=True)
	text = models.TextField( blank=True)
	image = models.ImageField(upload_to=save_info_img, blank=True)


class Partner(models.Model):
	name = models.CharField(max_length=255, blank=True)
	description = models.TextField(blank=True)
	image = models.ImageField(upload_to=save_logo, blank=True)


class AboutPage(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	image = models.ImageField(upload_to=save_info_img, blank=True)


class AboutPageInfos(models.Model):
	title = models.CharField(max_length=255, blank=True)
	text = models.TextField( blank=True)
	image = models.ImageField(upload_to=save_info_img, blank=True)


class ChildrenPage(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	image = models.ImageField(upload_to=save_info_img, blank=True)


class ChildrenPageInfos(models.Model):
	title = models.CharField(max_length=255, blank=True)
	text = models.TextField( blank=True)
	image = models.ImageField(upload_to=save_info_img, blank=True)


class ParentPage(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	image = models.ImageField(upload_to=save_info_img, blank=True)


class ParentPageInfos(models.Model):
	title = models.CharField(max_length=255, blank=True)
	text = models.TextField( blank=True)
	image = models.ImageField(upload_to=save_info_img, blank=True)


class SocialMediaUrls(models.Model):
	instagram = models.URLField(max_length=255, blank=True)
	facebook = models.URLField(max_length=255,  blank=True)
	twitter = models.URLField(max_length=255, blank=True)