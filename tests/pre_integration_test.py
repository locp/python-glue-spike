# coding=utf-8
"""Pre-Integration Testing feature tests."""
import boto3
import json
import os
import requests
import time

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

s3_client = boto3.client(
    's3',
    endpoint_url="http://localhost:4566",
    use_ssl=False,
    aws_access_key_id='ACCESS_KEY',
    aws_secret_access_key='SECRET_KEY')
s3_resource = boto3.resource(
    's3',
    endpoint_url="http://localhost:4566",
    use_ssl=False,
    aws_access_key_id='test',
    aws_secret_access_key='test')


@scenario('features/pre-integration.feature', 'Setup Entry Criteria')
def test_setup_entry_criteria():
    """Setup Entry Criteria."""


@given('localstack has started')
def localstack_has_started():
    """localstack has started."""
    pass


@when('localstack is ready')
def localstack_is_ready():
    """localstack is ready."""
    attempts = 60
    localstack_is_available = False
    url = 'http://localhost:4566/health'

    while attempts:
        try:
            response = requests.get(url)

            if response.status_code == 200:
                status_data = response.content
                status_data = json.loads(status_data)
                service_names = status_data['services'].keys()

                if len(service_names) > 0:
                    localstack_is_available = True

                for service in service_names:
                    if status_data['services'][service] != 'running':
                        localstack_is_available = False
        except BaseException:
            pass
        except json.decoder.JSONDecoder:
            pass

        if not localstack_is_available:
            time.sleep(1)
        else:
            break

        attempts -= 1

    assert localstack_is_available, 'Localstack is not available.'


@then('transfer input data')
def transfer_input_data():
    """transfer input data."""
    input_file_names = os.listdir('tests/resources/input')

    # Filter out any non-expected files.
    for input_file_name in input_file_names:
        if not input_file_name.endswith('data.txt'):
            input_file_names.remove(input_file_name)

    assert len(input_file_names) > 0, 'No input files.'

    for bucket_name in ['jobs', 'input', 'output']:
        s3_client.create_bucket(Bucket=bucket_name)

    for input_file_name in input_file_names:
        file_name = f'tests/resources/input/{input_file_name}'
        bucket = 'input'
        object_name = input_file_name
        s3_client.upload_file(file_name, bucket, object_name)
