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
import logging

from google.appengine.ext import ndb
from models.entities import Participant
from models.entities import Character
from models.viewmodels import SecretIdentityViewModel


class SecretIdentityFactory:
    @staticmethod
    def get_all_participants:
        
        secret_identities = []
        participants = Participant.query().sort(Participant.name)
        
        for p in participants:
            
            image_url = 'unknown.png'
            character_name = 'unknown'
            
            if p.characterKey is not None:
                character = p.characterKey.get()
                image_url = character.name.replace(' ','-') + '.png'
                character_name = character.name
                
            secret_identities.append(
                    SecretIdentity(p.name, character_name, image_url, p.catch_phrase)
                )
                
        return participants