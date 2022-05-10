from cProfile import Profile
from email import charset
from encodings import utf_8
import json


from rest_framework.renderers import JSONRenderer

class ProfileJSONRenderer(JSONRenderer):
    charset = "utf-8"

    def render(self, data, accepted_media_type=None, renderer_context=None):
        errors = data.get("errors", None)

        if errors is not None:
            return super(ProfileJSONRenderer, self).render(data)
            
        return json.dumps({"profile": data})

import json

from rest_framework.renderers import JSONRenderer


class ProfileJSONRenderer(JSONRenderer):
    charset = "utf-8"

    def render(self, data, accepted_media_types=None, renderer_context=None):
        errors = data.get("errors", None)

        if errors is not None:
            return super(ProfileJSONRenderer, self).render(data)

        return json.dumps({"profile": data})