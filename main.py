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

from google.appengine.ext import ndb
from google.appengine.ext.webapp import template

class Participant(ndb.Model):
	name = ndb.StringProperty()

class Character(ndb.Model):
    name = ndb.StringProperty()
    type = ndb.StringProperty(choices=['hero', 'villain'])
    theme = ndb.StringProperty()
    participant = ndb.KeyProperty(kind=Participant)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'views/select-type.html')
        self.response.out.write(template.render(path, None))

class AjaxAvailableTypesHandler(webapp2.RequestHandler):
    def post(self):
        #todo get actual availability
        result = {
            'heroes': True,
            'villains': False
        }
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(result))

class HomePageHandler(webapp2.RequestHandler):
    def get(self):
        heroCount = 0
        heroTakenCount = 0
        villainCount = 0
        villainTakenCount = 0

        themeCount = DataAccess.GetThemeCount()
        characters = DataAccess.GetAllCharacters()
        for character in characters:
            if character.type == 'hero':
                heroCount = heroCount + 1
                if character.participant is not None:
                    heroTakenCount = heroTakenCount + 1
            if character.type == 'villain':
                villainCount = villainCount + 1
                if character.participant is not None:
                    villainTakenCount = villainTakenCount + 1

        result = {
                'totalHeroes' : heroCount,
                'totalVillains': villainCount,
                'heroesTaken': heroTakenCount,
                'villainsTaken': villainTakenCount,
                'totalThemes': themeCount
            }
        
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(result))

class CharacterPageHandler(webapp2.RequestHandler):
    def get(self):
        result = []
        
        characters = DataAccess.GetAllCharactersWithEligibility()
        for character in characters:
            if character['type'] ==  self.request.get('type'):
                result.append(character)

        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(result))
 
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

class DataAccess:

    @staticmethod
    def GetThemeCount():
        return Character.query(projection=['theme'], distinct=True).count()

    @staticmethod
    def GetAllCharacters():
        return Character.query().fetch()

    @staticmethod
    def GetAllCharactersByType(type):
        return Character.query(Character.type == type).fetch()

    @staticmethod
    def GetAllCharactersWithEligibility():
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


        logging.warning(themes)


        #second pass - establish individual characters
        for character in characterRecords:

            eligible = False
            if character.type == 'hero':
                eligible = themes[character.theme].eligibleHeroes()
            else:
                eligible = themes[character.theme].eligibleVillains()

            characters.append({
                    'id': character.key.id(),
                    'name': character.name,
                    'type': character.type,
                    'theme': character.theme,
                    'taken': character.participant is not None,
                    'eligible': eligible
                })

        return characters

class PopulateHandler(webapp2.RequestHandler):
    def get(self):
        # number of 'taken' heroes must not exceed number of available villains
        batman = Character(name = 'Batman', type = 'hero', theme = 'batman')
        batman.put()
        robin = Character(name = 'Robin', type = 'hero', theme = 'batman')
        robin.put()
        joker = Character(name = 'Joker', type='villain', theme='batman')
        joker.put()

        superman = Character(name='Superman', type='hero', theme='superman')
        superman.put()
        lex = Character(name='Lex Luthor', type='villain', theme='superman')
        lex.put()
        zod = Character(name='General Zod', type='villain', theme='superman')
        zod.put()

        ed = Participant(name='Ed Carter')
        ed.put()

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/populate', PopulateHandler),
    ('/homepage', HomePageHandler),
    ('/character', CharacterPageHandler),
    ('/ajax/availableTypes', AjaxAvailableTypesHandler)
], debug=True)
