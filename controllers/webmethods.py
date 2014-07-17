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
from models.viewmodels import SecretIdentityViewModel
from models.factories import SecretIdentityFactory
from models.factories import CharacterFactory
from google.appengine.ext import ndb
from controllers.main import BaseHandler


class BaseAjaxHandler(BaseHandler):
    def dispatch(self):
        if self.get_participant() is None:
            self.abort(403)
        else:
            super(BaseAjaxHandler, self).dispatch()

class CharacterHandler(BaseAjaxHandler):
    def post(self):
        character_type = json.loads(self.request.body)['characterType']
        characters = CharacterFactory.get_character_selection_viewmodel(character_type)
        result = []
        for c in characters:
            result.append(c.__dict__)
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(result))

class GetSecretIdentitiesHandler(BaseHandler):
    def post(self):
        participant = self.get_participant()

        result = {}

        if participant is not None:
            secret_identity = SecretIdentityFactory.get_participant_secret_identity(participant)
            result['secretIdentity'] = secret_identity.__dict__

        all_identities_dict = []
        secret_identities = SecretIdentityFactory.get_all_participants()

        for i in secret_identities:
            all_identities_dict.append(i.__dict__)

        result['participants'] = all_identities_dict
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(result))

app = webapp2.WSGIApplication([
    ('/ajax/characters', CharacterHandler),
    ('/ajax/get-identities', GetSecretIdentitiesHandler)
], debug=True)
