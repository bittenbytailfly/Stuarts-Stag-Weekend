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
from models.dbaccess import CharacterEntity
from models.dbaccess import ParticipantEntity
from models.participantfactory import ParticipantFactory
from google.appengine.ext import ndb

class Theme:
    def __init__(self):
        self.heroCount = 0
        self.takenHeroCount = 0
        self.villainCount = 0
        self.takenVillainCount = 0

    def eligibleHeroes(self):
        return self.takenHeroCount < self.villainCount

    def eligibleVillains(self):
        return self.takenVillainCount < self.heroCount

    def increment(self, character):
        if character.type == 'hero':
            self.heroCount = self.heroCount + 1
            if character.participant is not None:
                self.takenHeroCount = self.takenHeroCount + 1
        else:
            self.villainCount = self.villainCount + 1
            if character.participant is not None:
                self.takenVillainCount = self.takenVillainCount + 1

class CharacterFactory:
    @staticmethod
    def GetAllCharacters(characterType):
        characters = []
        themes = {}

        characterRecords = DataAccess.GetAllCharacters()

        #first pass - get all themes and establish eligibility
        for character in characterRecords:

            if character.theme in themes:
                themes[character.theme].increment(character)
            else:
                themes[character.theme] = Theme()
                themes[character.theme].increment(character)

        #second pass - establish individual characters
        for character in characterRecords:

            if (character.type == characterType):

                eligible = False
                if character.type == 'hero':
                    eligible = themes[character.theme].eligibleHeroes()
                else:
                    eligible = themes[character.theme].eligibleVillains()

                characters.append({
                        'id': character.key.id(),
                        'name': character.name,
                        'image': (character.name.replace(' ','-') + '.png').lower(),
                        'type': character.type,
                        'theme': character.theme,
                        'taken': character.participant is not None,
                        'eligible': eligible
                    })

        return characters

    @staticmethod
    def AssociateParticipant(userId, characterId):
        user = ParticipantFactory.GetParticipantById(userId)

        logging.warning(user.character)

        if user is not None and user.character == 'unknown':
            selectedCharacter = CharacterEntity.get_by_id(characterId)

            logging.warning(selectedCharacter)

            if selectedCharacter is not None and selectedCharacter.participant is None:
                selectedCharacter.participant = ndb.Key(ParticipantEntity, userId)
                selectedCharacter.put()
