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
from models.viewmodels import CharacterViewModel
from google.appengine.ext import ndb


class CharacterHandler(webapp2.RequestHandler):
    def post(self):
        characterType = json.loads(self.request.body)['characterType']
        characters = CharacterViewModel.GetAllCharacters(characterType)
        result = []
        for c in characters:
            result.append(c.__dict__)
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(result))

class SelectionHandler(webapp2.RequestHandler):
    def post(self):
        params = json.loads(self.request.body)
        participantKey = params['participantKey']
        characterKey = params['characterKey']
        
        character = ndb.Key(urlsafe=characterKey).get()
        participant = ndb.Key(urlsafe=participantKey).get()

        #todo need to ensure character is not taken
        if character is not None and participant is not None and participant.characterKey is None:
            participant.characterKey = character.key
            participant.put()

app = webapp2.WSGIApplication([
    ('/ajax/characters', CharacterHandler),
    ('/ajax/select', SelectionHandler)
], debug=True)
