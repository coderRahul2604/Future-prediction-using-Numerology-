from django.shortcuts import render, HttpResponse
from django.core.serializers import serialize
from .models import Insight
from django.db.models import Count
import json

# Create your views here.

def index(request):
    return render(request, 'index.html')


def chart_intensity(request):

    # Fetch the sector and intensity columns from the Insight table
    insights = Insight.objects.all().values('sector', 'topic', 'region', 'end_year', 'source', 'country', 'intensity')
    insights_list = list(insights.values())
    for item in insights_list:
        item['added'] = item['added'].strftime('%Y-%m-%d %H:%M:%S') 
        item['published'] = item['published'].strftime('%Y-%m-%d %H:%M:%S')  

    # Convert the queryset into a dictionary format
    chart_data = {}
    chart_data_end_year = {}
    chart_data_topic = {}
    chart_data_region = {}
    chart_data_source = {}
    chart_data_country = {}
    for insight in insights:
        sector = insight['sector']
        end_year = insight['end_year']
        topic = insight['topic']
        region = insight['region']
        source = insight['source']
        country = insight['country']
        intensity = insight['intensity']

        if end_year and intensity:
            if end_year not in chart_data_end_year:
                chart_data_end_year[end_year] = []
            chart_data_end_year[end_year].append(intensity)

        if sector and intensity:
            if sector not in chart_data:
                chart_data[sector] = []
            chart_data[sector].append(intensity)

        if topic and intensity:
            if topic not in chart_data_topic:
                chart_data_topic[topic] = []
            chart_data_topic[topic].append(intensity)

        if region and intensity:
            if region not in chart_data_region:
                chart_data_region[region] = []
            chart_data_region[region].append(intensity)
 
        if source and intensity:
            if source not in chart_data_source:
                chart_data_source[source] = []
            chart_data_source[source].append(intensity)
 
        if country and intensity:
            if country not in chart_data_country:
                chart_data_country[country] = []
            chart_data_country[country].append(intensity)
 
    insights_str = json.dumps(insights_list)
    chart_data_str = json.dumps(chart_data)
    chart_data_topic_str = json.dumps(chart_data_topic)
    chart_data_region_str = json.dumps(chart_data_region)
    chart_data_end_year_str = json.dumps(chart_data_end_year)
    chart_data_source_str = json.dumps(chart_data_source)
    chart_data_country_str = json.dumps(chart_data_country)

    return render(request, 'intensityChart.html', {'insights_str':insights_str,
        'chart_data': chart_data, 'chart_data_str':chart_data_str,
        'chart_data_topic':chart_data_topic, 'chart_data_topic_str':chart_data_topic_str,
        'chart_data_region':chart_data_region, 'chart_data_region_str':chart_data_region_str,
        'chart_data_end_year':chart_data_end_year, 'chart_data_end_year_str':chart_data_end_year_str,
        'chart_data_source':chart_data_source, 'chart_data_source_str':chart_data_source_str,
        'chart_data_country':chart_data_country, 'chart_data_country_str':chart_data_country_str
        })

def chart_likelihood(request):
    insights = Insight.objects.all().values('sector', 'topic', 'region', 'end_year', 'source', 'country','likelihood')
    insights_list = list(insights.values())
    for item in insights_list:
        item['added'] = item['added'].strftime('%Y-%m-%d %H:%M:%S') 
        item['published'] = item['published'].strftime('%Y-%m-%d %H:%M:%S')  
    
    chart_data = {}
    chart_data_end_year = {}
    chart_data_topic = {}
    chart_data_region = {}
    chart_data_source = {}
    chart_data_country = {}
    for insight in insights:
        sector = insight['sector']
        end_year = insight['end_year']
        topic = insight['topic']
        region = insight['region']
        source = insight['source']
        country = insight['country']
        likelihood = insight['likelihood']

        if end_year and likelihood:
            if end_year not in chart_data_end_year:
                chart_data_end_year[end_year] = []
            chart_data_end_year[end_year].append(likelihood)

        if sector and likelihood:
            if sector not in chart_data:
                chart_data[sector] = []
            chart_data[sector].append(likelihood)

        if topic and likelihood:
            if topic not in chart_data_topic:
                chart_data_topic[topic] = []
            chart_data_topic[topic].append(likelihood)

        if region and likelihood:
            if region not in chart_data_region:
                chart_data_region[region] = []
            chart_data_region[region].append(likelihood)
 
        if source and likelihood:
            if source not in chart_data_source:
                chart_data_source[source] = []
            chart_data_source[source].append(likelihood)
 
        if country and likelihood:
            if country not in chart_data_country:
                chart_data_country[country] = []
            chart_data_country[country].append(likelihood)
 
    insights_str = json.dumps(insights_list)
    chart_data_str = json.dumps(chart_data)
    chart_data_topic_str = json.dumps(chart_data_topic)
    chart_data_region_str = json.dumps(chart_data_region)
    chart_data_end_year_str = json.dumps(chart_data_end_year)
    chart_data_source_str = json.dumps(chart_data_source)
    chart_data_country_str = json.dumps(chart_data_country)

    return render(request, 'likelihoodChart.html', {'insights_str':insights_str,
        'chart_data': chart_data, 'chart_data_str':chart_data_str,
        'chart_data_topic':chart_data_topic, 'chart_data_topic_str':chart_data_topic_str,
        'chart_data_region':chart_data_region, 'chart_data_region_str':chart_data_region_str,
        'chart_data_end_year':chart_data_end_year, 'chart_data_end_year_str':chart_data_end_year_str,
        'chart_data_source':chart_data_source, 'chart_data_source_str':chart_data_source_str,
        'chart_data_country':chart_data_country, 'chart_data_country_str':chart_data_country_str
        })

def chart_relevance(request):
    # Fetch the sector and relevance columns from the Insight table
    insights = Insight.objects.all().values('sector', 'topic', 'region', 'end_year', 'source', 'country', 'relevance')
    insights_list = list(insights.values())
    for item in insights_list:
        item['added'] = item['added'].strftime('%Y-%m-%d %H:%M:%S') 
        item['published'] = item['published'].strftime('%Y-%m-%d %H:%M:%S')  

    # Convert the queryset into a dictionary format
    chart_data = {}
    chart_data_end_year = {}
    chart_data_topic = {}
    chart_data_region = {}
    chart_data_source = {}
    chart_data_country = {}
    for insight in insights:
        sector = insight['sector']
        end_year = insight['end_year']
        topic = insight['topic']
        region = insight['region']
        source = insight['source']
        country = insight['country']
        relevance = insight['relevance']

        if end_year and relevance:
            if end_year not in chart_data_end_year:
                chart_data_end_year[end_year] = []
            chart_data_end_year[end_year].append(relevance)

        if sector and relevance:
            if sector not in chart_data:
                chart_data[sector] = []
            chart_data[sector].append(relevance)

        if topic and relevance:
            if topic not in chart_data_topic:
                chart_data_topic[topic] = []
            chart_data_topic[topic].append(relevance)

        if region and relevance:
            if region not in chart_data_region:
                chart_data_region[region] = []
            chart_data_region[region].append(relevance)

        if source and relevance:
            if source not in chart_data_source:
                chart_data_source[source] = []
            chart_data_source[source].append(relevance)

        if country and relevance:
            if country not in chart_data_country:
                chart_data_country[country] = []
            chart_data_country[country].append(relevance)

    insights_str = json.dumps(insights_list)
    chart_data_str = json.dumps(chart_data)
    chart_data_topic_str = json.dumps(chart_data_topic)
    chart_data_region_str = json.dumps(chart_data_region)
    chart_data_end_year_str = json.dumps(chart_data_end_year)
    chart_data_source_str = json.dumps(chart_data_source)
    chart_data_country_str = json.dumps(chart_data_country)

    return render(request, 'relevanceChart.html', {'insights_str': insights_str,
        'chart_data': chart_data, 'chart_data_str': chart_data_str,
        'chart_data_topic': chart_data_topic, 'chart_data_topic_str': chart_data_topic_str,
        'chart_data_region': chart_data_region, 'chart_data_region_str': chart_data_region_str,
        'chart_data_end_year': chart_data_end_year, 'chart_data_end_year_str': chart_data_end_year_str,
        'chart_data_source': chart_data_source, 'chart_data_source_str': chart_data_source_str,
        'chart_data_country': chart_data_country, 'chart_data_country_str': chart_data_country_str
        })

def chart_country(request):
    # Fetch the sector and country columns from the Insight table
    insights = Insight.objects.all().values('sector', 'topic', 'region', 'end_year', 'source', 'country')
    insights_list = list(insights.values())
    for item in insights_list:
        item['added'] = item['added'].strftime('%Y-%m-%d %H:%M:%S') 
        item['published'] = item['published'].strftime('%Y-%m-%d %H:%M:%S')  

    # Convert the queryset into a dictionary format
    chart_data = {}
    chart_data_end_year = {}
    chart_data_topic = {}
    chart_data_region = {}
    chart_data_source = {}
    chart_data_country = {}
    for insight in insights:
        sector = insight['sector']
        end_year = insight['end_year']
        topic = insight['topic']
        region = insight['region']
        source = insight['source']
        country = insight['country']

        if end_year and country:
            if end_year not in chart_data_end_year:
                chart_data_end_year[end_year] = []
            chart_data_end_year[end_year].append(country)

        if sector and country:
            if sector not in chart_data:
                chart_data[sector] = []
            chart_data[sector].append(country)

        if topic and country:
            if topic not in chart_data_topic:
                chart_data_topic[topic] = []
            chart_data_topic[topic].append(country)

        if region and country:
            if region not in chart_data_region:
                chart_data_region[region] = []
            chart_data_region[region].append(country)

        if source and country:
            if source not in chart_data_source:
                chart_data_source[source] = []
            chart_data_source[source].append(country)

        if country and country:
            if country not in chart_data_country:
                chart_data_country[country] = []
            chart_data_country[country].append(country)

    insights_str = json.dumps(insights_list)
    chart_data_str = json.dumps(chart_data)
    chart_data_topic_str = json.dumps(chart_data_topic)
    chart_data_region_str = json.dumps(chart_data_region)
    chart_data_end_year_str = json.dumps(chart_data_end_year)
    chart_data_source_str = json.dumps(chart_data_source)
    chart_data_country_str = json.dumps(chart_data_country)

    return render(request, 'countryChart.html', {'insights_str': insights_str,
        'chart_data': chart_data, 'chart_data_str': chart_data_str,
        'chart_data_topic': chart_data_topic, 'chart_data_topic_str': chart_data_topic_str,
        'chart_data_region': chart_data_region, 'chart_data_region_str': chart_data_region_str,
        'chart_data_end_year': chart_data_end_year, 'chart_data_end_year_str': chart_data_end_year_str,
        'chart_data_source': chart_data_source, 'chart_data_source_str': chart_data_source_str,
        'chart_data_country': chart_data_country, 'chart_data_country_str': chart_data_country_str
        })

def chart_topic(request):
    # Fetch the sector and topic columns from the Insight table
    insights = Insight.objects.all().values('sector', 'topic', 'region', 'end_year', 'source', 'country')
    insights_list = list(insights.values())
    for item in insights_list:
        item['added'] = item['added'].strftime('%Y-%m-%d %H:%M:%S') 
        item['published'] = item['published'].strftime('%Y-%m-%d %H:%M:%S')  

    # Convert the queryset into a dictionary format
    chart_data = {}
    chart_data_end_year = {}
    chart_data_topic = {}
    chart_data_region = {}
    chart_data_source = {}
    chart_data_country = {}
    
    for insight in insights:
        sector = insight['sector']
        end_year = insight['end_year']
        topic = insight['topic']
        region = insight['region']
        source = insight['source']
        country = insight['country']

        if end_year and topic:
            if end_year not in chart_data_end_year:
                chart_data_end_year[end_year] = []
            chart_data_end_year[end_year].append(topic)

        if sector and topic:
            if sector not in chart_data:
                chart_data[sector] = []
            chart_data[sector].append(topic)

        if topic and topic:
            if topic not in chart_data_topic:
                chart_data_topic[topic] = []
            chart_data_topic[topic].append(topic)

        if region and topic:
            if region not in chart_data_region:
                chart_data_region[region] = []
            chart_data_region[region].append(topic)

        if source and topic:
            if source not in chart_data_source:
                chart_data_source[source] = []
            chart_data_source[source].append(topic)

        if country and topic:
            if country not in chart_data_country:
                chart_data_country[country] = []
            chart_data_country[country].append(topic)

    insights_str = json.dumps(insights_list)
    chart_data_str = json.dumps(chart_data)
    chart_data_topic_str = json.dumps(chart_data_topic)
    chart_data_region_str = json.dumps(chart_data_region)
    chart_data_end_year_str = json.dumps(chart_data_end_year)
    chart_data_source_str = json.dumps(chart_data_source)
    chart_data_country_str = json.dumps(chart_data_country)
    insights_list_json = json.dumps(insights_list)

    return render(request, 'topicChart.html', {'insights_str': insights_str,
    'chart_data': chart_data, 'chart_data_str': chart_data_str,
    'chart_data_topic': chart_data_topic, 'chart_data_topic_str': chart_data_topic_str,
    'chart_data_region': chart_data_region, 'chart_data_region_str': chart_data_region_str,
    'chart_data_end_year': chart_data_end_year, 'chart_data_end_year_str': chart_data_end_year_str,
    'chart_data_source': chart_data_source, 'chart_data_source_str': chart_data_source_str,
    'chart_data_country': chart_data_country, 'chart_data_country_str': chart_data_country_str,
})

def chart_region(request):
    # Fetch the sector and region columns from the Insight table
    insights = Insight.objects.all().values('sector', 'topic', 'region', 'end_year', 'source', 'country', 'region')
    insights_list = list(insights.values())
    for item in insights_list:
        item['added'] = item['added'].strftime('%Y-%m-%d %H:%M:%S') 
        item['published'] = item['published'].strftime('%Y-%m-%d %H:%M:%S')  

    # Convert the queryset into a dictionary format
    chart_data = {}
    chart_data_end_year = {}
    chart_data_topic = {}
    chart_data_region = {}
    chart_data_source = {}
    chart_data_country = {}
    for insight in insights:
        sector = insight['sector']
        end_year = insight['end_year']
        topic = insight['topic']
        region = insight['region']
        source = insight['source']
        country = insight['country']
        region = insight['region']

        if end_year and region:
            if end_year not in chart_data_end_year:
                chart_data_end_year[end_year] = []
            chart_data_end_year[end_year].append(region)

        if sector and region:
            if sector not in chart_data:
                chart_data[sector] = []
            chart_data[sector].append(region)

        if topic and region:
            if topic not in chart_data_topic:
                chart_data_topic[topic] = []
            chart_data_topic[topic].append(region)

        if region and region:
            if region not in chart_data_region:
                chart_data_region[region] = []
            chart_data_region[region].append(region)

        if source and region:
            if source not in chart_data_source:
                chart_data_source[source] = []
            chart_data_source[source].append(region)

        if country and region:
            if country not in chart_data_country:
                chart_data_country[country] = []
            chart_data_country[country].append(region)

    insights_str = json.dumps(insights_list)
    chart_data_str = json.dumps(chart_data)
    chart_data_topic_str = json.dumps(chart_data_topic)
    chart_data_region_str = json.dumps(chart_data_region)
    chart_data_end_year_str = json.dumps(chart_data_end_year)
    chart_data_source_str = json.dumps(chart_data_source)
    chart_data_country_str = json.dumps(chart_data_country)

    return render(request, 'regionChart.html', {'insights_str': insights_str,
        'chart_data': chart_data, 'chart_data_str': chart_data_str,
        'chart_data_topic': chart_data_topic, 'chart_data_topic_str': chart_data_topic_str,
        'chart_data_region': chart_data_region, 'chart_data_region_str': chart_data_region_str,
        'chart_data_end_year': chart_data_end_year, 'chart_data_end_year_str': chart_data_end_year_str,
        'chart_data_source': chart_data_source, 'chart_data_source_str': chart_data_source_str,
        'chart_data_country': chart_data_country, 'chart_data_country_str': chart_data_country_str
        })

def chart_country(request):
    # Fetch the sector and region columns from the Insight table
    insights = Insight.objects.all().values('sector', 'topic', 'region', 'end_year', 'source', 'country', 'region')
    insights_list = list(insights.values())
    for item in insights_list:
        item['added'] = item['added'].strftime('%Y-%m-%d %H:%M:%S') 
        item['published'] = item['published'].strftime('%Y-%m-%d %H:%M:%S')  

    # Convert the queryset into a dictionary format
    chart_data = {}
    chart_data_end_year = {}
    chart_data_topic = {}
    chart_data_region = {}
    chart_data_source = {}
    chart_data_country = {}
    for insight in insights:
        sector = insight['sector']
        end_year = insight['end_year']
        topic = insight['topic']
        region = insight['region']
        source = insight['source']
        country = insight['country']
        region = insight['region']

        if end_year and region:
            if end_year not in chart_data_end_year:
                chart_data_end_year[end_year] = []
            chart_data_end_year[end_year].append(region)

        if sector and region:
            if sector not in chart_data:
                chart_data[sector] = []
            chart_data[sector].append(region)

        if topic and region:
            if topic not in chart_data_topic:
                chart_data_topic[topic] = []
            chart_data_topic[topic].append(region)

        if region and region:
            if region not in chart_data_region:
                chart_data_region[region] = []
            chart_data_region[region].append(region)

        if source and region:
            if source not in chart_data_source:
                chart_data_source[source] = []
            chart_data_source[source].append(region)

        if country and region:
            if country not in chart_data_country:
                chart_data_country[country] = []
            chart_data_country[country].append(region)

    insights_str = json.dumps(insights_list)
    chart_data_str = json.dumps(chart_data)
    chart_data_topic_str = json.dumps(chart_data_topic)
    chart_data_region_str = json.dumps(chart_data_region)
    chart_data_end_year_str = json.dumps(chart_data_end_year)
    chart_data_source_str = json.dumps(chart_data_source)
    chart_data_country_str = json.dumps(chart_data_country)

    return render(request, 'countryChart.html', {'insights_str': insights_str,
        'chart_data': chart_data, 'chart_data_str': chart_data_str,
        'chart_data_topic': chart_data_topic, 'chart_data_topic_str': chart_data_topic_str,
        'chart_data_region': chart_data_region, 'chart_data_region_str': chart_data_region_str,
        'chart_data_end_year': chart_data_end_year, 'chart_data_end_year_str': chart_data_end_year_str,
        'chart_data_source': chart_data_source, 'chart_data_source_str': chart_data_source_str,
        'chart_data_country': chart_data_country, 'chart_data_country_str': chart_data_country_str
        })

