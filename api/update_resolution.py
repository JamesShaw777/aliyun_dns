# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import os
import sys

from typing import List

from alibabacloud_alidns20150109.client import Client as Alidns20150109Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_alidns20150109 import models as alidns_20150109_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient


class UpdateResolution:
    def __init__(self):
        pass

    @staticmethod
    def get_credentials_from_file(file_path: str):
        """
        Read credentials from a config file.
        """
        credentials = {}
        with open(file_path, 'r') as file:
            for line in file:
                name, value = line.strip().split('=')
                credentials[name.strip()] = value.strip().strip("'")
        return credentials

    @staticmethod
    def create_client() -> Alidns20150109Client:
        """
        Initialize the Client with the AccessKey of the account
        @return: Client
        @throws Exception
        """
        # Read credentials from the config file
        credentials = UpdateResolution.get_credentials_from_file('config.txt')
        
        config = open_api_models.Config(
            access_key_id=credentials['access_key_id'],
            access_key_secret=credentials['access_key_secret']
        )
        config.endpoint = 'dns.aliyuncs.com'
        return Alidns20150109Client(config)

    @staticmethod
    def update_domain_record(record_id: str, rr: str, record_type: str, value: str, line: str) -> None:
        client = UpdateResolution.create_client()
        update_domain_record_request = alidns_20150109_models.UpdateDomainRecordRequest(
            record_id=record_id,
            rr=rr,
            type=record_type,
            value=value,
            line=line
        )
        runtime = util_models.RuntimeOptions()
        try:
            client.update_domain_record_with_options(update_domain_record_request, runtime)
        except Exception as error:
            print(error.message)
            print(error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)

    @staticmethod
    async def update_domain_record_async(record_id: str, rr: str, record_type: str, value: str, line: str) -> None:
        client = UpdateResolution.create_client()
        update_domain_record_request = alidns_20150109_models.UpdateDomainRecordRequest(
            record_id=record_id,
            rr=rr,
            type=record_type,
            value=value,
            line=line
        )
        runtime = util_models.RuntimeOptions()
        try:
            await client.update_domain_record_with_options_async(update_domain_record_request, runtime)
        except Exception as error:
            print(error.message)
            print(error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)


if __name__ == '__main__':
    if len(sys.argv) != 6:
        print("Usage: python UpdateResolution.py <record_id> <rr> <type> <value> <line>")
    else:
        record_id = sys.argv[1]
        rr = sys.argv[2]
        record_type = sys.argv[3]
        value = sys.argv[4]
        line = sys.argv[5]
        UpdateResolution.update_domain_record(record_id, rr, record_type, value, line)
