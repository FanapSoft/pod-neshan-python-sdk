# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_neshan import PodNeshan

try:
    pod_neshan = PodNeshan(api_token=API_TOKEN, sc_api_key=SC_API_KEY_NO_TRAFFIC_DIRECTION)

    print(pod_neshan.no_traffic_direction(origin={"lat": 36.3141962, "lng": 59.5412054},
                                          destination={"lat": 36.32203769, "lng": 59.4759667},
                                          # way_points=[{"lat": 36.333556, "lng": 59.5354888}],
                                          # avoidTrafficZone=False,
                                          # avoidOddEvenZone=True,
                                          # alternative=True
                                          ))
    # OUTPUT
    # {
    #   "routes": [
    #     {
    #       "overview_polyline": {
    #         "points": "wss|EqdljJpj@adA_r@tmAygBllIqBvA}]sLXbAr|@j[jXhC|GdCoCjGcDfOnLvE{@dE"
    #       },
    #       "legs": [
    #         {
    #           "summary": "بلوار ملک آباد - بلوار وکیل آباد",
    #           "distance": {
    #             "value": 11131,
    #             "text": "۱۱ کیلومتر"
    #           },
    #           "duration": {
    #             "value": 940,
    #             "text": "۱۶ دقیقه"
    #           },
    #           "steps": [
    #             {
    #               "name": "ورودی بلوار ملک آباد",
    #               "instruction": "در جهت جنوب شرقی در ورودی بلوار ملک آباد قرار بگیرید",
    #               "distance": {
    #                 "value": 245,
    #                 "text": "۲۵۰ متر"
    #               },
    #               "duration": {
    #                 "value": 33,
    #                 "text": "۱ دقیقه"
    #               },
    #               "polyline": "wss|EqdljJlBgD`AcBxAgD",
    #               "maneuver": "depart",
    #               "start_location": [
    #                 59.541365,
    #                 36.314356
    #               ]
    #             },
    #             {
    #               "name": "بلوار ملک آباد",
    #               "instruction": "در بلوار ملک آباد به مسیر خود ادامه دهید",
    #               "distance": {
    #                 "value": 1006,
    #                 "text": "۱ کیلومتر"
    #               },
    #               "duration": {
    #                 "value": 93,
    #                 "text": "۲ دقیقه"
    #               },
    #               "polyline": "mks|EerljJn@oAlBuDLU??bBwCrBmDrBmDpBmDrBmDrBmDrBmDpBmDj@_ANW",
    #               "maneuver": "straight",
    #               "start_location": [
    #                 59.543547,
    #                 36.313031
    #               ]
    #             }
    #           ]
    #         },
    #         ...
    #       ]
    #     }
    #   ]
    # }


except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
