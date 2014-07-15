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
from models.characterfactory import CharacterFactory

class AvailableTypesHandler(webapp2.RequestHandler):
    def post(self):
        #todo get actual availability
        result = {
            'heroes': True,
            'villains': False
        }
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(result))

class CharacterHandler(webapp2.RequestHandler):
    def post(self):
        characterType = json.loads(self.request.body)['characterType']
        logging.warning(characterType)
        result = {}
        characters = CharacterFactory.GetAllCharacters(characterType)
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(characters))

class SelectionHandler(webapp2.RequestHandler):
    def post(self):
        params = json.loads(self.request.body)
        userId = params['userId']
        characterId = params['characterId']
        CharacterFactory.AssociateParticipant(userId, characterId)

app = webapp2.WSGIApplication([
    ('/ajax/availableTypes', AvailableTypesHandler),
    ('/ajax/characters', CharacterHandler),
    ('/ajax/select', SelectionHandler)
], debug=True)
