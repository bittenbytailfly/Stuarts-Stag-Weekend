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

    def increment(self, character):
        if character.type == 'hero':
            self.heroCount = self.heroCount + 1
            if character.taken:
                self.takenHeroCount = self.takenHeroCount + 1
        else:
            self.villainCount = self.villainCount + 1
            if character.taken:
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
        eligibleThemes = []
        taken_character_count = 0
        
        characterRecords = Character.get_all_characters()
        participant_count = Participant.get_all_participants().count()
        
        #first pass - get all themes and establish eligibility
        for character in characterRecords:
            if character.theme not in themes:
                themes[character.theme] = Theme()
            themes[character.theme].increment(character)
            if character.taken:
                taken_character_count = taken_character_count + 1
                if character.theme not in eligibleThemes:
                    eligibleThemes.append(character.theme)

        lockdown = taken_character_count == int(participant_count / 2)

        #second pass - establish individual characters
        for character in characterRecords:
            if (character.type == characterType):
                eligible = False
                if lockdown:
                    eligible = character.theme in eligibleThemes
                else:
                    if character.type == 'hero':
                        eligible = themes[character.theme].eligibleHeroes()
                    else:
                        eligible = themes[character.theme].eligibleVillains()

                characters.append(CharacterViewModel(character.key.urlsafe(),
                        character.name,
                        (character.name.replace(' ','-') + '.png').lower(),
                        character.type,
                        character.theme,
                        character.taken,
                        eligible))

        return characters
        
class SecretIdentityViewModel:
    def __init__(self, name, character_name, image_url, catch_phrase):
        self.name = name
        self.character_name = character_name
        self.image_url = image_url
        self.catch_phrase = catch_phrase