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
from google.appengine.ext.webapp import template

class Character(ndb.Model):
    name = ndb.StringProperty()
    type = ndb.StringProperty(choices=['hero', 'villain'])
    theme = ndb.StringProperty()
    taken = ndb.BooleanProperty()

    @classmethod
    def get_all_characters(cls):
        return cls.query()

class Participant(ndb.Model):
    name = ndb.StringProperty()
    catchphrase = ndb.StringProperty()
    characterKey = ndb.KeyProperty(kind=Character)

    def get_character(self):
        return self.characterKey.get()

    @classmethod
    def get_all_participants(cls):
        return cls.query()