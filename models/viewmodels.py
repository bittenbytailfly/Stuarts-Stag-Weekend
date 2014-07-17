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


class CharacterViewModel:
    def  __init__(self, url_safe_key, name, image, type, theme, taken, eligible):
        self.url_safe_key = url_safe_key
        self.name = name
        self.image = image
        self.type = type
        self.theme = theme
        self.taken = taken
        self.eligible = eligible
        
class SecretIdentityViewModel:
    def __init__(self, name, character_name, image_url, catchphrase):
        self.name = name
        self.character_name = character_name
        self.image_url = image_url
        self.catchphrase = catchphrase