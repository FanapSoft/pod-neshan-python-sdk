# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_neshan import PodNeshan

try:
    pod_neshan = PodNeshan(api_token=API_TOKEN, sc_api_key=SC_API_KEY_NO_TRAFFIC_DISTANCE_MATRIX)

    origins = [
        {
            "lat": 36.317559,
            "lng": 59.532226
        },
        {
            "lat": 36.337077,
            "lng": 59.530843
        }
    ]

    destinations = [
        {
            "lat": 36.350681,
            "lng": 59.545227
        },
        {
            "lat": 36.337012,
            "lng": 59.530023
        }
    ]

    print(pod_neshan.no_traffic_distance_matrix(origins=origins, destinations=destinations))
    # OUTPUT
    # {
    #   "status": "Ok",
    #   "rows": [
    #     {
    #       "elements": [
    #         {
    #           "status": "Ok",
    #           "duration": {
    #             "value": 628,
    #             "text": "۱۰ دقیقه"
    #           },
    #           "distance": {
    #             "value": 7606,
    #             "text": "۸ کیلومتر"
    #           }
    #         },
    #         {
    #           "status": "Ok",
    #           "duration": {
    #             "value": 421,
    #             "text": "۷ دقیقه"
    #           },
    #           "distance": {
    #             "value": 4937,
    #             "text": "۵ کیلومتر"
    #           }
    #         }
    #       ]
    #     },
    #     {
    #       "elements": [
    #         {
    #           "status": "Ok",
    #           "duration": {
    #             "value": 485,
    #             "text": "۸ دقیقه"
    #           },
    #           "distance": {
    #             "value": 5311,
    #             "text": "۵ کیلومتر"
    #           }
    #         },
    #         {
    #           "status": "Ok",
    #           "duration": {
    #             "value": 61,
    #             "text": "۱ دقیقه"
    #           },
    #           "distance": {
    #             "value": 389,
    #             "text": "۴۰۰ متر"
    #           }
    #         }
    #       ]
    #     }
    #   ],
    #   "origin_addresses": [
    #     "36.317559,59.532226",
    #     "36.337077,59.530843"
    #   ],
    #   "destination_addresses": [
    #     "36.350681,59.545227",
    #     "36.337012,59.530023"
    #   ]
    # }


except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))

except PodException as e:
    print("Pod Exception: ", e.message)
