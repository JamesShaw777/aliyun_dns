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


class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> Alidns20150109Client:
        """
        Initialize the Client with the AccessKey of the account
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config(
            # Directly using AccessKey ID and AccessKey Secret in the code
            access_key_id='your_access_key_id',
            access_key_secret='your_access_key_secret'
        )
        # See https://api.alibabacloud.com/product/Alidns.
        config.endpoint = 'alidns.cn-beijing.aliyuncs.com'
        return Alidns20150109Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        describe_domain_records_request = alidns_20150109_models.DescribeDomainRecordsRequest(
            domain_name='emailposter.net',
            type='A'
        )
        runtime = util_models.RuntimeOptions()
        try:
            # Run the API and print the return value
            response = client.describe_domain_records_with_options(describe_domain_records_request, runtime)
            print(response.to_map())
        except Exception as error:
            # Only a printing example. Please be careful about exception handling and do not ignore exceptions directly in engineering projects.
            # print error message
            print(error.message)
            # Please click on the link below for diagnosis.
            print(error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        describe_domain_records_request = alidns_20150109_models.DescribeDomainRecordsRequest(
            domain_name='emailposter.net',
            type='A'
        )
        runtime = util_models.RuntimeOptions()
        try:
            # Run the API and print the return value
            response = await client.describe_domain_records_with_options_async(describe_domain_records_request, runtime)
            print(response.to_map())
        except Exception as error:
            # Only a printing example. Please be careful about exception handling and do not ignore exceptions directly in engineering projects.
            # print error message
            print(error.message)
            # Please click on the link below for diagnosis.
            print(error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)


if __name__ == '__main__':
    Sample.main(sys.argv[1:])
