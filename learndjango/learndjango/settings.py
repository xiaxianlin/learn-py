import os
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-c!5#&wxe!7hx35q88b0-$&lw57olt^&&+96l-w3r)8tg=y5%_h"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "polls",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "learndjango.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "learndjango.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        # 数据库引擎配置
        "ENGINE": "django.db.backends.mysql",
        # 数据库的名字
        "NAME": "vote",
        # 数据库服务器的IP地址（本机可以写localhost或127.0.0.1）
        "HOST": "localhost",
        # 启动MySQL服务的端口号
        "PORT": 3306,
        # 数据库用户名和口令
        "USER": "hellokitty",
        "PASSWORD": "Hellokitty.618",
        # 数据库使用的字符集
        "CHARSET": "utf8",
        # 数据库时间日期的时区设定
        "TIME_ZONE": "Asia/Chongqing",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "zh-hans"
TIME_ZONE = "Asia/Chongqing"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
LOGGING = {
    "version": 1,
    # 是否禁用已经存在的日志器
    "disable_existing_loggers": False,
    # 日志格式化器
    "formatters": {
        "simple": {
            "format": "%(asctime)s %(module)s.%(funcName)s: %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "verbose": {
            "format": "%(asctime)s %(levelname)s [%(process)d-%(threadName)s] "
            "%(module)s.%(funcName)s line %(lineno)d: %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    # 日志过滤器
    "filters": {
        # 只有在Django配置文件中DEBUG值为True时才起作用
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    # 日志处理器
    "handlers": {
        # 输出到控制台
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "filters": ["require_debug_true"],
            "formatter": "simple",
        },
        # 输出到文件(每周切割一次)
        "file1": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": "access.log",
            "when": "W0",
            "backupCount": 12,
            "formatter": "simple",
            "level": "INFO",
        },
        # 输出到文件(每天切割一次)
        "file2": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": "error.log",
            "when": "D",
            "backupCount": 31,
            "formatter": "verbose",
            "level": "WARNING",
        },
    },
    # 日志器记录器
    "loggers": {
        "django": {
            # 需要使用的日志处理器
            "handlers": ["console", "file1", "file2"],
            # 是否向上传播日志信息
            "propagate": True,
            # 日志级别(不一定是最终的日志级别)
            "level": "DEBUG",
        },
    },
}

# 下面的配置根据项目需要进行设置
REST_FRAMEWORK = {
    # 配置默认页面大小
    # 'PAGE_SIZE': 10,
    # 配置默认的分页类
    # 'DEFAULT_PAGINATION_CLASS': '...',
    # 配置异常处理器
    # 'EXCEPTION_HANDLER': '...',
    # 配置默认解析器
    # 'DEFAULT_PARSER_CLASSES': (
    #     'rest_framework.parsers.JSONParser',
    #     'rest_framework.parsers.FormParser',
    #     'rest_framework.parsers.MultiPartParser',
    # ),
    # 配置默认限流类
    # 'DEFAULT_THROTTLE_CLASSES': (
    #     '...'
    # ),
    # 配置默认授权类
    # 'DEFAULT_PERMISSION_CLASSES': (
    #     '...',
    # ),
    # 配置默认认证类
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     '...',
    # ),
}
