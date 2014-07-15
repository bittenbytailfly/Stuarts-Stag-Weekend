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

class MainHandler(webapp2.RequestHandler):
    def get(self):
        userId = self.request.get('id')
        logging.warning(self.request)
        participant = ParticipantFactory.GetParticipantById(userId)
        path = os.path.join(os.path.dirname(__file__), '../views/select-type.html')
        self.response.out.write(template.render(path, {'userId': userId}))

class CharacterPageHandler(webapp2.RequestHandler):
    def get(self):
        userId = self.request.get('id')
        characterType = self.request.get('type')
        path = os.path.join(os.path.dirname(__file__), '../views/select-character.html')
        self.response.out.write(template.render(path, {'userId': userId, 'characterType': characterType}))

class PopulateHandler(webapp2.RequestHandler):
    def get(self):
       ConstructData.SetupDataStructures()

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/populate', PopulateHandler),
    ('/character', CharacterPageHandler)
], debug=True)
