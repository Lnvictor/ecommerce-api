import json
import pytest
import requests
from django.urls import reverse


CSV_RECORDS = [
    'product1,this is the product1,1,123.23,1,1\n',
    'product2,this is the product2,1,123.23,1,1\n',
    'product3,this is the product3,1,123.23,1,1\n',
]


def test_should_parse_csv_correctly(client, db, http_request_headers):
    tmp_file = open('/tmp/test.csv', 'w')
    header_str = 'name, desc, domain, value, quantity, provider\n'
    tmp_file.write(header_str)
    tmp_file.writelines(CSV_RECORDS)
    tmp_file.close()
    tmp_file = open('/tmp/test.csv', 'r')
    content = tmp_file.read().encode()
    response = client.post(reverse('core:upload_csv'), content, **http_request_headers, content_type='text/csv')
    content = json.loads(response.content)

    assert response.status_code == 201
    assert content[0]['name'] == 'product1'
    assert content[1]['name'] == 'product2'
    assert content[2]['name'] == 'product3'


def test_should_not_parse_csv_correctly_due_invalid_data(client, db, http_request_headers):
    invalid_data = 'this is a invalid data'.encode()

    response = client.post(reverse('core:upload_csv'), invalid_data, **http_request_headers, content_type='text/csv')

    assert response.status_code == 204 # No content
