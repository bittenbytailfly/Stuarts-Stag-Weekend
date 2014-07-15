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

from models.entities import CharacterEntity
from models.entities import ParticipantEntity

class ConstructData:
    @staticmethod
    def SetupDataStructures():
        batman = CharacterEntity(name = 'Batman', type = 'hero', theme = 'batman')
        batman.put()
        robin = CharacterEntity(name = 'Robin', type = 'hero', theme = 'batman')
        robin.put()
        joker = CharacterEntity(name = 'Joker', type='villain', theme='batman')
        joker.put()

        superman = CharacterEntity(name='Superman', type='hero', theme='superman')
        superman.put()
        lex = CharacterEntity(name='Lex Luthor', type='villain', theme='superman')
        lex.put()
        zod = CharacterEntity(name='General Zod', type='villain', theme='superman')
        zod.put()

        ed = ParticipantEntity(name='Ed Carter')
        ed.put()