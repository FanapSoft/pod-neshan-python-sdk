# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_neshan import PodNeshan

try:
    pod_neshan = PodNeshan(api_token=API_TOKEN, sc_api_key=SC_API_KEY_SEARCH)

    print(pod_neshan.search(term="دانشگاه فردوسی", lat=36.3141962, lng=59.5412054))
    # OUTPUT
    # {
    #   "count": 30,
    #   "items": [
    #     {
    #       "category": "place",
    #       "type": "university",
    #       "region": "مشهد، خراسان رضوی",
    #       "location": {
    #         "x": 59.52963750000001,
    #         "y": 36.309977599999975,
    #         "z": "NaN"
    #       },
    #       "title": "دانشگاه فردوسی مشهد",
    #       "address": "بزرگراه شهید کلانتری، بلوار دانش"
    #     },
    #     {
    #       "category": "place",
    #       "type": "bus_station",
    #       "region": "مشهد، خراسان رضوی",
    #       "location": {
    #         "x": 59.53920999999999,
    #         "y": 36.31107999999999,
    #         "z": "NaN"
    #       },
    #       "title": "ایستگاه اتوبوس دانشگاه فردوسی",
    #       "address": "بزرگراه شهید کلانتری"
    #     },
    #     ...
    #   ]
    # }


except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
