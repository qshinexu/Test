import pytest
import requests

from testcase.yaml_util import read_yaml


class TestApi:
    @pytest.mark.parametrize('args', read_yaml())
    def test_01_api(self, args):
        url = args['api_request']['url']
        method = args['api_request']['method']
        headers = args['api_request']['headers']
        params = args['api_request']['params']
        validate = args['api_validate']
        if method == 'get':
            requests.get()
        else:
            res = requests.post(url, json=params, headers=headers)
            print(args)
            #for val in validate:
                #assert val['eq']['code'] == res.json()['code']


if __name__ == '__main__':
    pytest.main(['-vs', 'test_api.py'])
