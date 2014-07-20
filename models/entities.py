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
from google.appengine.api import memcache
from google.appengine.ext.webapp import template

class Character(ndb.Model):
    name = ndb.StringProperty()
    type = ndb.StringProperty(choices=['hero', 'villain'])
    theme = ndb.StringProperty()
    taken = ndb.BooleanProperty()

    def get_image_url(self):
        return self.name.replace(' ', '-').lower() + '.jpg'

    @classmethod
    def get_all_characters(cls, character_type):
        return cls.query(cls.type == character_type)

class Participant(ndb.Model):
    name = ndb.StringProperty()
    catchphrase = ndb.StringProperty()
    character_key = ndb.KeyProperty(kind=Character)
    image_url = ndb.StringProperty()
    character_name = ndb.StringProperty()

    def get_character(self):
        if self.character_key is None:
            return None
        return self.character_key.get()

    def associate_character(self, character, catchphrase):
        self.character_key = character.key
        self.image_url = character.get_image_url()
        self.character_name = character.name
        self.catchphrase = catchphrase
        self.put()
        character.taken = True
        character.put()
        if (character.type == 'hero'):
            Counter.increment(TAKEN_HERO_COUNTER_KEY)
        else:
            Counter.increment(TAKEN_VILLAIN_COUNTER_KEY)

    def unassociate_character(self):
        current_character = self.character_key.get()
        self.character_key = None
        self.image_url = None
        self.character_name = None
        self.catchphrase = None
        self.put()
        current_character.taken = False
        current_character.put()
        if (current_character.type == 'hero'):
            Counter.decrement(TAKEN_HERO_COUNTER_KEY)
        else:
            Counter.decrement(TAKEN_VILLAIN_COUNTER_KEY)

    @classmethod
    def get_all_participants(cls):
        return cls.query()

    def _pre_put_hook(self):
        logging.warning(self.key.id())
        if self.key.id() is None:
            Counter.increment(PARTICIPANT_COUNTER_KEY)

PARTICIPANT_COUNTER_KEY = 'counter'
TAKEN_HERO_COUNTER_KEY = 'taken_heroes'
TAKEN_VILLAIN_COUNTER_KEY = 'taken_villains'

class Counter(ndb.Model):
    total = ndb.IntegerProperty(default=0)
    
    @classmethod
    def get_total(cls, name):
        total = memcache.get(name)
        if total is None:
            counterKey = ndb.Key(cls, name)
            counter = counterKey.get()
            if counter is not None:
                total = counter.total
            else:
                total = 0
            memcache.add(name, total, 60)
        return total
    
    @classmethod
    def increment(cls, name):
        cls._update(name, 1)
        memcache.incr(name)
            
    @classmethod
    def decrement(cls, name):
        cls._update(name, -1)
        memcache.decr(name)
        
    @classmethod
    @ndb.transactional
    def _update(cls, name, i):
        counterKey = ndb.Key(cls, name)
        counter = counterKey.get()
        if counter is None:
            counter = Counter(id=name, total=i)
        else:
            counter.total += i
        counter.put()