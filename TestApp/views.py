from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from elasticsearch import Elasticsearch
import urllib.parse

# Create your views here.
def hello(request):
    curr_stock = request.GET.get("curr_stock")
    if curr_stock != None :
        curr_stock = urllib.parse.unquote(curr_stock)
    else :
        curr_stock = '萬　企 (2701)'
    return render(request, 'index.html', {
        'data': ['萬　企 (2701)','華　園 (2702)','國　賓 (2704)','六　福 (2705)','第一店 (2706)'],
        'curr_stock' : curr_stock,
    })

def queryEsTest(request):
    query_str = request.GET.get("queryStr")
    es = Elasticsearch(hosts='localhost', port='9200')
    res = es.search(index="doc_index", body={"query": {"match": {'內容': str(query_str)}}})
    return JsonResponse(res['hits']['hits'], safe=False)