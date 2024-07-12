# save_data.py

import json
from django.core.management.base import BaseCommand
from app.models import Insight
from datetime import datetime
import os

class Command(BaseCommand):
    help = 'Save data from JSON file to database'

    def handle(self, *args, **kwargs):
        json_file_path = os.path.join(os.path.dirname(__file__), 'jsondata.json')
        with open(json_file_path, encoding='utf-8') as f:
            json_data = json.load(f)
        
        for item in json_data:
            added_str = item.get('added', '')
            published_str = item.get('published', '')
            added = None
            published = None
    
            try:
                added = datetime.strptime(added_str, '%B, %d %Y %H:%M:%S') if added_str else None
            except ValueError:
                pass
            
            try:
                published = datetime.strptime(published_str, '%B, %d %Y %H:%M:%S') if published_str else None
            except ValueError:
                pass

            try:
                intensity = int(item.get('intensity', 0))
            except (ValueError, TypeError):
                intensity = 0

            try:
                relevance = int(item.get('relevance', 0)) if item.get('relevance', '') else 0
            except (ValueError, TypeError):
                relevance = 0

            try:
                likelihood = int(item.get('likelihood', 0))
            except (ValueError, TypeError):
                likelihood = 0

            insight = Insight(
                end_year=item.get('end_year', ''),
                intensity=intensity,
                sector=item.get('sector', ''),
                topic=item.get('topic', ''),
                insight=item.get('insight', ''),
                url=item.get('url', ''),
                region=item.get('region', ''),
                start_year=item.get('start_year', ''),
                impact=item.get('impact', ''),
                added=added,
                published=published or datetime.now(),  # Set default value to current datetime if published is None
                country=item.get('country', ''),
                relevance=relevance,
                pestle=item.get('pestle', ''),
                source=item.get('source', ''),
                title=item.get('title', ''),
                likelihood=likelihood
            )
            insight.save()
