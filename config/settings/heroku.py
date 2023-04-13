from .common import *
import os
import dj_database_url

DEBUG = False  

ALLOWED_HOSTS = ["*", ]

AWS_ACCESS_KEY_ID = "AKIAQBPSSXJQVRC4ZUL4"
AWS_SECRET_ACCESS_KEY = "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"
AWS_STORAGE_BUCKET_NAME = "recipe-post-kitamura"

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = S3_URL

DATABASES = {
    'default': dj_database_url.config()
}