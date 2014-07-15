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
from models.dbaccess import DataAccess
from google.appengine.ext import ndb
from models.entities import ParticipantEntity
from models.helpers import NumberHelper

class Participant:
    def  __init__(self, name, character):
        self.name = name
        self.character = character

class ParticipantFactory:
    @staticmethod
    def GetParticipantById(id):
        userId = NumberHelper.ConvertToInt(id, 0)
        userKey = ndb.Key(ParticipantEntity, userId)

        user = userKey.get()
        if user is None:
            return None

        character = DataAccess.GetCharacterByParticipantKey(userKey)

        charactername = 'unknown'
        if character is not None:
            charactername = character.name

        return Participant(user.name, charactername)