from urllib.request import urlopen, Request
import http.client
import json
import pprint


test_url = "http://naver.com"
header = {
	'host': 'www.naver.com',
	'user-agent' : 'Mozilla/5.0'
}
data = 'test=post-data'

# # req = urllib.request.Request(test_url, headers=header, data=data)
# req = urllib.request.Request(test_url)
# response = urllib.request.urlopen(req)
#
# result = response.getheade
# print('result = ', result)


# 엘라스틱서치 정보 확인
res = urlopen('http://13.125.100.91:9200')
# print(res.read().decode(res.headers.get_content_charset()))


# 엘라스틱서치 class
class Elasticsearch():

	use_http = True
	conn = None
	url = ''

	def __init__(self, url = ''):
		self.url = url
		# self.conn = http.client.HTTPConnection(url)

	# index 정보를 확인한다
	def get_index(self, index):
		url = self.url + "/" + index
		if self.use_http:
			text = self.request('GET', url)
		else:
			text = self.get(url)
		index_info = json.loads(text)
		return index_info

	# document 정보를 확인한다
	def get_document(self, index, type):
		url = self.url + "/" + index + "/" + type
		text = self.get(url)
		index_info = json.loads(text)
		return index_info

	# index 생성
	def create_index(self, index):
		url = self.url + "/" + index
		payload = {
			'settings' : {
				'index' : {
					'number_of_shards' : 5,
					'number_of_replicas' : 1
				}
			}
		}
		# payload = ""
		return self.post(url, json.dumps(payload))

	# 표준 웹 get
	def get(self, url):
		res = urlopen(url)
		result = res.read().decode(res.headers.get_content_charset())
		return result

	# 표준 웹 post
	def post(self, url, payload):
		print(url, payload)
		req = Request(url, data = payload)
		res = urlopen(req)
		result = res.read().decode(res.headers.get_content_charset())
		return result


	# 표준 웹 http get
	def request(self, method, url, body = ''):
		conn = http.client.HTTPConnection(url)
		self.conn.request(method, url, body)
		res = self.conn.getresponse()
		result = res.read().decode(res.headers.get_content_charset())
		return result


	# HTTP GET
	def http_get(self, url):
		# connection = http.client.HTTPSConnection("www.journaldev.com")
		connection = http.client.HTTPSConnection(url)
		connection.request("GET", "/")
		response = connection.getresponse()
		headers = response.getheaders()
		pp = pprint.PrettyPrinter(indent=4)
		pp.pprint("Headers: {}".format(headers))

	# HTTP POST
	def POST(self, url):
		conn = http.client.HTTPSConnection('www.httpbin.org')

		headers = {'Content-type': 'application/json'}

		foo = {'text': 'Hello HTTP #1 **cool**, and #1!'}
		json_data = json.dumps(foo)

		conn.request('POST', '/post', json_data, headers)

		response = conn.getresponse()
		print(response.read().decode())

	# HTTP PUT
	def PUT(self, url):
		conn = http.client.HTTPSConnection('www.httpbin.org')

		headers = {'Content-type': 'application/json'}

		foo = {'text': 'Hello HTTP #1 **cool**, and #1!'}
		json_data = json.dumps(foo)

		conn.request("PUT", "/put", json_data)
		response = conn.getresponse()
		print(response.status, response.reason)

	# GET
	def DELETE(self, url):
		connection = http.client.HTTPSConnection(url)
		connection.request("GET", "/")
		response = connection.getresponse()
		headers = response.getheaders()
		pp = pprint.PrettyPrinter(indent=4)
		pp.pprint("Headers: {}".format(headers))


# 엘라스틱서치 객체 생성
es = Elasticsearch('http://13.125.100.91:9200')

# es.http_get('http://13.125.100.91:9200')
es.http_get('http://chamsodam.com')

exit()

pprint(es.get_index('potolog'))

# print(es.get('http://13.125.100.91:9200'))

if False:
	pprint(es.get_index('acrm-2018.09.19'))
	pprint(es.get_index('potolog'))
	# print(es.create_index('tot'))
	pprint(es.get_document('acrm-2018.09.19', '_search'))

	# print(es.post('http://13.125.100.91:9200', ''))


exit()

# 색인 생성
pprint(es.create_index('block'))
