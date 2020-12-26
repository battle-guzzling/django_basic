from django.http import JsonResponse
from rest_framework import status


def success(message, data={}):
    # localize message here
    # custom data here
    return JsonResponse(
        {"data": data, "message": message},
        safe=False,
        status=status.HTTP_200_OK,
    )
