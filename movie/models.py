from django.db import models


# class Movie(models.Model):
#     GENRES = (
#         ("Action", "Action"),
#         ("Adventure", "Adventure"),
#         ("Animation", "Animation"),
#         ("Children's", "Children's"),
#         ("Comedy", "Comedy"),
#         ("Crime", "Crime"),
#         ("Documentary", "Documentary"),
#         ("Drama", "Drama"),
#         ("Fantasy", "Fantasy"),
#         ("Film-Noir", "Film-Noir"),
#         ("Horror", "Horror"),
#         ("Musical", "Musical"),
#         ("Mystery", "Mystery"),
#         ("Romance", "Romance"),
#         ("Sci-Fi", "Sci-Fi"),
#         ("Thriller", "Thriller"),
#         ("War", "War"),
#         ("Western", "Western"),
#     )
#     title = models.CharField(max_length=50)
#     genres = models.CharField(max_length=100, choices=GENRES)
#
#
# class User(models.Model):
#     GENDERS = (
#         ("F", "FEMALE"),
#         ("M", "MALE"),
#     )
#     gender = models.CharField(max_length=100, choices=GENDERS)
#     AGES = (
#         (1, "Under 18"),
#         (18, "18-24"),
#         (25, "25-34"),
#         (35, "35-44"),
#         (45, "45-49"),
#         (50, "50-55"),
#         (56, "56+"),
#     )
#     age = models.CharField(max_length=100, choices=AGES)
#     OCCUPATION = (
#         (0, "other or not specified"),
#         (1, "academic/educator"),
#         (2, "artist"),
#         (3, "clerical/admin"),
#         (4, "college/grad student"),
#         (5, "customer service"),
#         (6, "doctor/health care"),
#         (7, "executive/managerial"),
#         (8, "farmer"),
#         (9, "homemaker"),
#         (10, "K-12 student"),
#         (11, "lawyer"),
#         (12, "programmer"),
#         (13, "retired"),
#         (14, "sales/marketing"),
#         (15, "scientist"),
#         (16, "self-employed"),
#         (17, "technician/engineer"),
#         (18, "tradesman/craftsman"),
#         (19, "unemployed"),
#         (20, "writer"),
#     )
#     occupation = models.CharField(max_length=100, choices=OCCUPATION)
#     zip_code = models.IntegerField()

class SuspiciousUser(models.Model):
    user_id = models.IntegerField()
    is_return = models.BooleanField(default=False)


class Rate(models.Model):
    user_id = models.IntegerField()
    movie_id = models.IntegerField()
    RATING = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    rating = models.IntegerField(choices=RATING)
    timestamp = models.IntegerField()
