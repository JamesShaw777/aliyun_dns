# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import sys
import os

from typing import List

from alibabacloud_alidns20150109.client import Client as Alidns20150109Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_alidns20150109 import models as alidns_20150109_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient


class GetResolution:
    def __init__(self):
        pass

    @staticmethod
    def load_config(file_path: str) -> dict:
        """
        Load configuration from a file.
        @param file_path: The path to the config file
        @return: A dictionary containing the configuration
        """
        config = {}
        with open(file_path, 'r') as file:
            for line in file:
                key, value = line.strip().split('=')
                config[key.strip()] = value.strip().strip("'")
        print("Loaded config:", config)  # Print the loaded config for debugging
        return config

    @staticmethod
    def create_client(config: dict) -> Alidns20150109Client:
        """
        Initialize the Client with the AccessKey of the account
        @return: Client
        @throws Exception
        """
        client_config = open_api_models.Config(
            access_key_id=config['access_key_id'],
            access_key_secret=config['access_key_secret']
        )
        client_config.endpoint = 'alidns.cn-beijing.aliyuncs.com'
        return Alidns20150109Client(client_config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        # Adjusting the config path to point to the parent directory
        config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config.txt'))
        config = GetResolution.load_config(config_path)
        client = GetResolution.create_client(config)
        
        describe_domain_records_request = alidns_20150109_models.DescribeDomainRecordsRequest(
            domain_name=config['domain_name'],
            type=config['type']
        )
        runtime = util_models.RuntimeOptions()
        try:
            response = client.describe_domain_records_with_options(describe_domain_records_request, runtime)
            if response:
                response_map = response.to_map()
                print("Response:", response_map)
                return response_map  # Return the response for further processing
            else:
                print("Error: No response received from describe_domain_records_with_options")
                return None
        except Exception as error:
            print("Exception occurred:", error.message)
            if hasattr(error, 'data') and error.data:
                print("Error data:", error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)
            return None

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        # Adjusting the config path to point to the parent directory
        config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config.txt'))
        config = GetResolution.load_config(config_path)
        client = GetResolution.create_client(config)
        
        describe_domain_records_request = alidns_20150109_models.DescribeDomainRecordsRequest(
            domain_name=config['domain_name'],
            type=config['type']
        )
        runtime = util_models.RuntimeOptions()
        try:
            response = await client.describe_domain_records_with_options_async(describe_domain_records_request, runtime)
            if response:
                response_map = response.to_map()
                print("Response:", response_map)
                return response_map  # Return the response for further processing
            else:
                print("Error: No response received from describe_domain_records_with_options_async")
                return None
        except Exception as error:
            print("Exception occurred:", error.message)
            if hasattr(error, 'data') and error.data:
                print("Error data:", error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)
            return None


if __name__ == '__main__':
    GetResolution.main(sys.argv[1:])
