#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import webapp2
import logging
import json

from models.setup import ConstructData
from google.appengine.ext import ndb
from google.appengine.ext.webapp import template
from models.factories import SecretIdentityFactory


class BaseHandler(webapp2.RequestHandler):
    def __init__(self, request, response):
        self.initialize(request, response)
        self.url_safe_participant_key = self.request.cookies.get('participant_key')

    def get_participant(self):
        participant_key = ndb.Key(urlsafe=self.url_safe_participant_key)
        return participant_key.get()

class SecuredBaseHandler(BaseHandler):
    def dispatch(self):
        if self.get_participant() is None or self.get_participant().character_key is not None:
            self.redirect('/')
        else:
            super(SecuredBaseHandler, self).dispatch()

class SetParticipantHandler(webapp2.RequestHandler):
    def get(self, url_safe_participant_key):
        logging.warning(self.request.host_url)
        if url_safe_participant_key is not None:
            self.response.set_cookie('participant_key', url_safe_participant_key, max_age=None)
        self.redirect('/')

class CharacterTypeSelectionHandler(SecuredBaseHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), '../views/select-type.html')
        self.response.out.write(template.render(path, None))

class CharacterPageHandler(SecuredBaseHandler):
    def get(self, character_type):
        path = os.path.join(os.path.dirname(__file__), '../views/select-character.html')
        self.response.out.write(template.render(path, {'characterType': character_type}))

class PopulateHandler(webapp2.RequestHandler):
    def get(self):
        ConstructData.setup_data_structure()

class SecretIdentitiesHandler(BaseHandler):
    def get(self):
        participant = self.get_participant()
        template_values = {'secretIdentity': 'null'}

        if participant is not None:
            secret_identity = SecretIdentityFactory.get_participant_secret_identity(participant)
            template_values = {'secretIdentity': json.dumps(secret_identity.__dict__)}

        path = os.path.join(os.path.dirname(__file__), '../views/secret-identities.html')
        self.response.out.write(template.render(path, template_values))

app = webapp2.WSGIApplication([
    webapp2.Route('/u/<url_safe_participant_key>', SetParticipantHandler),
    webapp2.Route('/populate', PopulateHandler),
    webapp2.Route('/select', CharacterTypeSelectionHandler),
    webapp2.Route('/<character_type:hero|villain>', CharacterPageHandler),
    webapp2.Route('/', SecretIdentitiesHandler)
], debug=True)
