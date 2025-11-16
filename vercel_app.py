"""
WSGI application for Vercel deployment
"""
from harmony_housing.wsgi import application

# Vercel will use this as the entry point
app = application

