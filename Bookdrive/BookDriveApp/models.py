from django.db import models
from django.core.validators import MinValueValidator


class donator(models.Model):
	CHOICES = (
		('Novel', 'Novel'),
		('Fiction', 'Fiction'),
		('Non-Fiction', 'Non-Fiction'),
		('History', 'History'),
		('Textbook', 'Textbook'),
		('Encyclopedia', 'Encyclopedia'),
		('Childrens', 'Childrens'),
		('Fantasy', 'Fantasy'),
		('Poetry', 'Poetry'),
		('Spiritual', 'Spiritual'),	
		('Science', 'Science'),
		('Math', 'Math'),
		('Textbook', 'Textbook'),
		('Journal', 'Journal'),
		('Self Help', 'Self Help'),
		('others', 'others'))

	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=250)
	kindofbooks = models.CharField(max_length=150, choices = CHOICES)
	numberofbooks = models.PositiveIntegerField(validators=[MinValueValidator(1)])
	location = models.CharField(max_length=150)


	
	STATUS = (
		('Delivered', 'Delivered'),
		('Pending', 'Pending'),
		('Pick-up', 'Pick-up'))
	status = models.CharField(max_length=200, choices=STATUS, default= 'Pending')

class benificiary(models.Model):
	CHOICES = (
		('Novel', 'Novel'),
		('Fiction', 'Fiction'),
		('Non-Fiction', 'Non-Fiction'),
		('History', 'History'),
		('Textbook', 'Textbook'),
		('Encyclopedia', 'Encyclopedia'),
		('Childrens', 'Childrens'),
		('Fantasy', 'Fantasy'),
		('Poetry', 'Poetry'),
		('Spiritual', 'Spiritual'),	
		('Science', 'Science'),
		('Math', 'Math'),
		('Textbook', 'Textbook'),
		('Journal', 'Journal'),
		('Self Help', 'Self Help'),
		('others', 'others'))

	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=250)
	kindofbooks = models.CharField(max_length=150, choices = CHOICES)
	countofbooks = models.PositiveIntegerField(validators=[MinValueValidator(1)])
	location = models.CharField(max_length=150)

	STATUS1 = (
		('Delivered', 'Delivered'),
		('Pending', 'Pending'),
		('Pick-up', 'Pick-up'))
	status = models.CharField(max_length=200, choices=STATUS1, default= 'Pending')
