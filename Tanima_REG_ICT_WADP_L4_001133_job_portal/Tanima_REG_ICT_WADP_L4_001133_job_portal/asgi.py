"""
ASGI config for Tanima_REG_ICT_WADP_L4_001133_job_portal project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Tanima_REG_ICT_WADP_L4_001133_job_portal.settings')

application = get_asgi_application()
