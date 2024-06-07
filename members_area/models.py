from django.db import models
import os


def save_main_img(instance, filename):
	extension = filename.split('.')[-1]
	new_filename = f"{instance.title}'_Info'.{extension}"
	return  os.path.join('members_info/', new_filename) 


def save_mnews_img(instance, filename):
	extension = filename.split('.')[-1]
	new_filename = f"{instance.title}'_'{instance.date}.{extension}"
	return  os.path.join('members_news/', new_filename) 


def save_mevents_img(instance, filename):
	extension = filename.split('.')[-1]
	new_filename = f"{instance.title}'_'{instance.date}.{extension}"
	return  os.path.join('members_events/', new_filename) 


def save_mevents_files(instance, filename):
	extension = filename.split('.')[-1]
	new_filename = f"{instance.title}'_CSresource'.{extension}"
	return  os.path.join('members_resources/', new_filename) 


class MembersPageInfos(models.Model):
	title = models.CharField(max_length=255, blank=True)
	text = models.TextField( blank=True)
	image = models.ImageField(upload_to=save_main_img, blank=True)


class MembersNews(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()
	date = models.DateField(auto_now_add=True)
	image = models.ImageField(upload_to=save_mnews_img)

	
class MembersEvents(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()
	date = models.DateField(auto_now_add=True)
	image = models.ImageField(upload_to=save_mevents_img, blank=True)


class MembersResources(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField(blank=True)
	date = models.DateField(auto_now_add=True)
	files = models.FileField(upload_to=save_mevents_files)


class MembersMessage(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	date = models.DateField(auto_now_add=True)



