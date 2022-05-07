from email.policy import default
from rest_framework.exceptions import APIException


class ProfileNotFound(APIException):
    status_code = 404
    default_details = "The Requested profile does not exist"


class NotYourProfile(APIException):
    status_code = 403
    default_details = "You can't edit a profile that doesn't belong to you"