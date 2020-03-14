# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_neshan import PodNeshan

try:
    pod_neshan = PodNeshan(api_token=API_TOKEN, sc_api_key=SC_API_KEY_NO_TRAFFIC_DISTANCE_MATRIX)

    points = [
        {
            "lat": 36.317559,
            "lng": 59.532226
        },
        {
            "lat": 36.337077,
            "lng": 59.530843
        },
        {
            "lat": 36.350681,
            "lng": 59.545227
        },
        {
            "lat": 36.337012,
            "lng": 59.530023
        }
    ]

    print(pod_neshan.map_matching(points))
    # OUTPUT
    # {
    #   "snappedPoints": [
    #     {
    #       "location": {
    #         "latitude": 36.318387,
    #         "longitude": 59.532509
    #       },
    #       "originalIndex": 0
    #     },
    #     {
    #       "location": {
    #         "latitude": 36.336187,
    #         "longitude": 59.530746
    #       },
    #       "originalIndex": 1
    #     }
    #   ]
    # }


except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))

except PodException as e:
    print("Pod Exception: ", e.message)
