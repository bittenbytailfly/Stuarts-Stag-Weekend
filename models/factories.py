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
from models.entities import Participant
from models.entities import Character
from models.viewmodels import SecretIdentityViewModel
from models.viewmodels import CharacterViewModel
from models.entities import Counter
from models.entities import PARTICIPANT_COUNTER_KEY
from models.entities import TAKEN_VILLAIN_COUNTER_KEY
from models.entities import TAKEN_HERO_COUNTER_KEY
import logging

class SecretIdentityFactory:
    @staticmethod
    def get_participant_secret_identity(participant):
        image_url = participant.image_url or 'unknown.jpg'
        character_name = participant.character_name or 'unknown'

        return SecretIdentityViewModel(participant.name, character_name, image_url,
                                       participant.catchphrase)

    @staticmethod
    def get_all_participants():
        
        secret_identities = []
        participants = Participant.query().order(Participant.name)
        
        for p in participants:
            image_url = p.image_url or 'unknown.jpg'
            character_name = p.character_name or 'unknown'
            secret_identities.append(SecretIdentityViewModel(p.name, character_name, image_url, p.catchphrase))
                
        return secret_identities


class CharacterFactory:
    @staticmethod
    def get_character_selection_viewmodel(character_type):

        character_viewmodels = []

        characters = Character.get_all_characters(character_type)
        total_participants = Counter.get_total(PARTICIPANT_COUNTER_KEY)
        taken_heroes = Counter.get_total(TAKEN_HERO_COUNTER_KEY)
        taken_villains = Counter.get_total(TAKEN_VILLAIN_COUNTER_KEY)

        heroes_eligible = taken_villains <= int(total_participants / 2)
        villains_eligible = taken_heroes <= int(total_participants / 2)

        for c in characters:
            if c.type == character_type:
                eligible = False
                if c.type == 'hero':
                    eligible = heroes_eligible
                else:
                    eligible = villains_eligible

                character_viewmodels.append(CharacterViewModel(c.key.urlsafe(), c.name, c.get_image_url(), c.type,
                                                               c.theme, c.taken, eligible))

        return character_viewmodels