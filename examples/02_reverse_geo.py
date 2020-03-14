# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_neshan import PodNeshan

try:
    pod_neshan = PodNeshan(api_token=API_TOKEN, sc_api_key=SC_API_KEY_REVERSE_GEO)

    print(pod_neshan.reverse_geo(lat=36.3141962, lng=59.5412054))
    # OUTPUT
    # {
    #   "status": "OK",
    #   "neighbourhood": "نوفل لوشاتو",
    #   "state": "استان خراسان رضوی",
    #   "city": "مشهد",
    #   "addresses": [
    #     {
    #       "formatted": "بلوار ملک آباد",
    #       "components": [
    #         {
    #           "name": "بلوار ملک آباد",
    #           "type": "primary"
    #         }
    #       ]
    #     }
    #   ],
    #   "place": "باغ ملک آباد",
    #   "municipality_zone": "9",
    #   "in_traffic_zone": None,
    #   "in_odd_even_zone": False,
    #   "route_name": "ورودی بلوار ملک آباد",
    #   "route_type": "primary_link",
    #   "formatted_address": "استان خراسان رضوی، مشهد، نوفل لوشاتو، بلوار ملک آباد، باغ ملک آباد"
    # }


except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
