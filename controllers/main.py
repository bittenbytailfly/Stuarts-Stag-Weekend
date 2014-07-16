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
import json
import logging

from models.setup import ConstructData
from models.participantfactory import Participant
from models.participantfactory import ParticipantFactory
from google.appengine.ext import ndb
from google.appengine.ext.webapp import template
from webapp2_extras import routes


class MainHandler(webapp2.RequestHandler):
    def get(self, url_safe_participant_key):
        participant_key = ndb.Key(urlsafe=url_safe_participant_key or '')
        participant = participant_key.get()
        if participant is None:
            self.redirect('/')
        path = os.path.join(os.path.dirname(__file__), '../views/select-type.html')
        self.response.out.write(template.render(path, {'participantKey': url_safe_participant_key}))

class CharacterPageHandler(webapp2.RequestHandler):
    def get(self, url_safe_participant_key, character_type):
        path = os.path.join(os.path.dirname(__file__), '../views/select-character.html')
        self.response.out.write(template.render(path, {'participantKey': url_safe_participant_key, 'characterType': character_type}))

class PopulateHandler(webapp2.RequestHandler):
    def get(self):
        ConstructData.SetupDataStructures()

class SecretIdentitiesHandler(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), '../views/secret-identities.html')
        self.response.out.write(template.render(path, None))

app = webapp2.WSGIApplication([
    webapp2.Route('/populate', PopulateHandler),
    webapp2.Route('/<url_safe_participant_key>', MainHandler),
    webapp2.Route('/<url_safe_participant_key>/<character_type:hero|villain>', CharacterPageHandler),
    webapp2.Route('/', SecretIdentitiesHandler)
], debug=True)
