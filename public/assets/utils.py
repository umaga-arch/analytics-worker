# utils.py

import os
import logging
import json
import requests

from analytics_worker.config import config
from analytics_worker.utils.exceptions import UnsupportedMediaTypeException

def get_analytics_data(url):
    """Fetch analytics data from the given URL."""
    try:
        response = requests.get(url, headers={'Authorization': f'Bearer {config.get("api_key")}'})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f'Failed to fetch analytics data from URL {url}: {e}')
        raise

def validate_media_type(media_type):
    """Validate the given media type."""
    supported_media_types = ['csv', 'json']
    if media_type not in supported_media_types:
        raise UnsupportedMediaTypeException(f'Media type {media_type} is not supported')
    return media_type