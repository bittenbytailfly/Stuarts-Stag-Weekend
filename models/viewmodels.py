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

    def increment(self, character, takenCharacterKeys):
        if character.type == 'hero':
            self.heroCount = self.heroCount + 1
            if character.key in takenCharacterKeys:
                self.takenHeroCount = self.takenHeroCount + 1
        else:
            self.villainCount = self.villainCount + 1
            if character.key in takenCharacterKeys:
                self.takenVillainCount = self.takenVillainCount + 1

class CharacterViewModel:
    def  __init__(self, url_safe_key, name, image, type, theme, taken, eligible):
        self.url_safe_key = url_safe_key
        self.name = name
        self.image = image
        self.type = type
        self.theme = theme
        self.taken = taken
        self.eligible = eligible
        
    @staticmethod
    def GetAllCharacters(characterType):
        characters = []
        themes = {}
        takenCharacterKeys = []
        eligibleThemes = []

        participants = Participant.get_all_participants()
        for cp in participants:
            if cp.characterKey is not None:
                takenCharacterKeys.append(cp.characterKey)
                eligibleThemes.append(cp.get_character().theme)
        
        characterRecords = Character.get_all_characters()
        
        lockdown = len(takenCharacterKeys) == 12

        #first pass - get all themes and establish eligibility
        for character in characterRecords:

            if character.theme in themes:
                themes[character.theme].increment(character, takenCharacterKeys)
            else:
                themes[character.theme] = Theme()
                themes[character.theme].increment(character, takenCharacterKeys)

        #second pass - establish individual characters
        for character in characterRecords:

            if (character.type == characterType):

                eligible = False
                if character.type == 'hero':
                    eligible = themes[character.theme].eligibleHeroes()
                else:
                    eligible = themes[character.theme].eligibleVillains()

                characters.append(CharacterViewModel(character.key.urlsafe(),
                        character.name,
                        (character.name.replace(' ','-') + '.png').lower(),
                        character.type,
                        character.theme,
                        character.key in takenCharacterKeys,
                        eligible or (lockdown and character.theme in eligibleThemes)))

        return characters