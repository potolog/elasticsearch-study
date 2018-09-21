from urllib.request import urlopen, Request
import json
import elasticsearch
from pprint import pprint


# 엘라스틱서치 정보 확인
res = urlopen('http://13.125.100.91:9200')
# print(res.read().decode(res.headers.get_content_charset()))


servers = ['http://13.125.100.91:9200',]
index_name = 'acrm-2018.09.20'
type_name = 'acrm'




# 엘라스틱서치 class
class Elasticsearch():
	servers = ''
	index = ''
	type = ''
	es = None

	def __init__(self, servers = '', index = '', type = ''):
		self.servers = servers
		self.index = index
		self.type = type
		self.connect(servers)

	def set_index(self, index):
		self.index = index

	def set_type(self, type):
		self.type = type

	def connect(self, servers):
		self.es = elasticsearch.Elasticsearch(servers)

	# index 정보를 확인한다
	def get_index(self, index):
		url = self.url + "/" + index
		text = self.get(url)
		index_info = json.loads(text)
		return index_info

	# info 엘라스틱서치 정보 확인
	def info(self):
		return self.es.info()

	# count
	def count(self):
		return self.es.count()

	# search
	def search(self):
		result = self.es.search()
		pprint(result)

	# read_elastic
	def read_elastic(self, index_name, query = ''):
		body = {'query': {'match_all': {}}}
		# if query == '':
		# 	query = body
		result = self.es.search(index_name, body = query)
		pprint(result)

	# get
	def get(self, index_name, type_name, query):
		body = {'query': {'match_all': {}}}
		result = self.es.get(index_name, type_name, query = query)
		pprint(result)

	# index 생성
	def create_index(self, index):
		url = self.url + "/" + index
		payload = {
			'settings' : {
				'index' : {
					'number_of_shards' : 1,
					'number_of_replicas' : 1
				}
			}
		}
		self.post(url, json.dumps(payload))

	# 표준 웹 get
	def get(self, url):
		res = urlopen(url)
		result = res.read().decode(res.headers.get_content_charset())
		return result

	# 표준 웹 post
	def post(self, url, payload):
		req = Request(url, data = payload)
		res = urlopen(req)
		result = res.read().decode(res.headers.get_content_charset())
		return result

# 엘라스틱서치 객체 생성
# es = elasticsearch.Elasticsearch(servers)
es = Elasticsearch(servers)

# es.indices(index_name)
# es.cluster.health(wait_for_status = 'yellow')

print('\n** elasticsearch info **')
pprint(es.info())
# pprint(es.search())

print('\n** elasticsearch count **')
pprint(es.count())

# es.search('acrm-2018.09.18', '', '{"query": {"match_all": {}}}')
# es.search('potolog', '', '{"query": {"match_all": {}}}')

print('\n** elasticsearch read_elastic **')
es.read_elastic('potolog')

print('\n** elasticsearch read_elastic **')
body = {'query': {'match_all': {}}}
es.read_elastic('potolog', body)
