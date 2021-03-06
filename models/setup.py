#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from models.entities import Character
from models.entities import Participant


class ConstructData:
    @staticmethod
    def setup_data_structure():
        batman = Character(name='Batman', type='hero', theme='batman', taken=False)
        robin = Character(name='Robin', type='hero', theme='batman', taken=False)
        joker = Character(name='Joker', type='villain', theme='batman', taken=False)
        penguin = Character(name='Penguin', type='villain', theme='batman', taken=False)
        bane = Character(name='Bane', type='villain', theme='batman', taken=False)
        riddler = Character(name='Riddler', type='villain', theme='batman', taken=False)
        twoface = Character(name='Two Face', type='villain', theme='batman', taken=False)
        superman = Character(name='Superman', type='hero', theme='superman', taken=False)
        lexluthor = Character(name='Lex Luthor', type='villain', theme='superman', taken=False)
        generalzod = Character(name='General Zod', type='villain', theme='superman', taken=False)
        greenlantern = Character(name='Green Lantern', type='hero', theme='green lantern', taken=False)
        sinestro = Character(name='Sinestro', type='villain', theme='green lantern', taken=False)
        captainamerica = Character(name='Captain America', type='hero', theme='captain america', taken=False)
        redskull = Character(name='Red Skull', type='villain', theme='captain america', taken=False)
        thor = Character(name='Thor', type='hero', theme='thor', taken=False)
        loki = Character(name='Loki', type='villain', theme='thor', taken=False)
        wolverine = Character(name='Wolverine', type='hero', theme='xmen', taken=False)
        sabretooth = Character(name='Sabretooth', type='villain', theme='xmen', taken=False)
        professorx = Character(name='Professor X', type='hero', theme='xmen', taken=False)
        cyclops = Character(name='Cyclops', type='hero', theme='xmen', taken=False)
        megneto = Character(name='Magneto', type='villain', theme='xmen', taken=False)
        mrfantastic = Character(name='Mr Fantastic', type='hero', theme='fantastic four', taken=False)
        thing = Character(name='Thing', type='hero', theme='fantastic four', taken=False)
        drdoom = Character(name='Dr Doom', type='villain', theme='fantastic four, hulk', taken=False)
        ironman = Character(name='Iron Man', type='hero', theme='iron man', taken=False)
        mandarin = Character(name='Mandarin', type='villain', theme='iron man', taken=False)
        spiderman = Character(name='Spiderman', type='hero', theme='spiderman', taken=False)
        venom = Character(name='Venom', type='villain', theme='spiderman', taken=False)
        greengoblin = Character(name='Green Goblin', type='villain', theme='spiderman', taken=False)
        theincrediblehulk = Character(name='The Incredible Hulk', type='hero', theme='hulk', taken=False)
        abomination = Character(name='Abomination', type='villain', theme='hulk', taken=False)
        deadpool = Character(name='Deadpool', type='villain', theme='hulk', taken=False)
        punisher = Character(name='Punisher', type='villain', theme='hulk', taken=False)
        splinter = Character(name='Splinter', type='hero', theme='tmnt', taken=False)
        leonardo = Character(name='Leonardo', type='hero', theme='tmnt', taken=False)
        shredder = Character(name='Shredder', type='villain', theme='tmnt', taken=False)
        rorshach = Character(name='Rorschach', type='hero', theme='watchmen', taken=False)
        nightowl = Character(name='Night Owl', type='hero', theme='watchmen', taken=False)
        ozymandis = Character(name='Ozymandias', type='villain', theme='watchmen', taken=False)
        kickass = Character(name='Kick Ass', type='hero', theme='kick ass', taken=False)
        redmist = Character(name='Red Mist', type='villain', theme='kick ass', taken=False)
        flashgordon = Character(name='Flash Gordon', type='hero', theme='flash gordon', taken=False)
        mingthemerciless = Character(name='Ming the Merciless', type='villain', theme='flash gordon', taken=False)
        bananaman = Character(name='Bananaman', type='hero', theme='bananaman', taken=False)
        gerneralblight = Character(name='General Blight', type='villain', theme='bananaman', taken=False)
        superted = Character(name='Superted', type='hero', theme='superted', taken=False)
        texaspete = Character(name='Texas Pete', type='villain', theme='superted', taken=False)
        greenarrow = Character(name='Green Arrow', type='hero', theme='green arrow', taken=False)
        heman = Character(name='He-Man', type='hero', theme='heman', taken=False)
        skeletor = Character(name='Skeletor', type='villain', theme='heman', taken=False)

        batman.put()
        robin.put()
        joker.put()
        penguin.put()
        bane.put()
        riddler.put()
        twoface.put()
        superman.put()
        lexluthor.put()
        generalzod.put()
        greenlantern.put()
        sinestro.put()
        captainamerica.put()
        redskull.put()
        thor.put()
        loki.put()
        wolverine.put()
        sabretooth.put()
        professorx.put()
        cyclops.put()
        megneto.put()
        mrfantastic.put()
        thing.put()
        drdoom.put()
        ironman.put()
        mandarin.put()
        spiderman.put()
        venom.put()
        greengoblin.put()
        theincrediblehulk.put()
        abomination.put()
        deadpool.put()
        punisher.put()
        splinter.put()
        leonardo.put()
        shredder.put()
        rorshach.put()
        nightowl.put()
        ozymandis.put()
        kickass.put()
        redmist.put()
        flashgordon.put()
        mingthemerciless.put()
        bananaman.put()
        gerneralblight.put()
        superted.put()
        texaspete.put()
        greenarrow.put()
        heman.put()
        skeletor.put()

        aaronb = Participant(name='Aaron B', catchphrase='')
        andrewh = Participant(name='Andrew H', catchphrase='')
        brens = Participant(name='Bren S', catchphrase='')
        christ = Participant(name='Chris T', catchphrase='')
        dana = Participant(name='Dan A', catchphrase='')
        dang = Participant(name='Dan G', catchphrase='')
        edc = Participant(name='Ed C', catchphrase='')
        garyp = Participant(name='Gary P', catchphrase='')
        garys = Participant(name='Gary S', catchphrase='')
        grantw = Participant(name='Grant W', catchphrase='')
        ianc = Participant(name='Ian C', catchphrase='')
        jamesh = Participant(name='James H', catchphrase='')
        jasont = Participant(name='Jason T', catchphrase='')
        jonh = Participant(name='Jon H', catchphrase='')
        karls = Participant(name='Karl S', catchphrase='')
        kevinh = Participant(name='Kevin H', catchphrase='')
        lees = Participant(name='Lee S', catchphrase='')
        liamc = Participant(name='Liam C', catchphrase='')
        markh = Participant(name='Mark H', catchphrase='')
        martinb = Participant(name='Martin B', catchphrase='')
        mikep = Participant(name='Mike P', catchphrase='')
        timp = Participant(name='Tim P', catchphrase='')

        aaronb.put()
        andrewh.put()
        brens.put()
        christ.put()
        dana.put()
        dang.put()
        edc.put()
        garyp.put()
        garys.put()
        grantw.put()
        ianc.put()
        jamesh.put()
        jasont.put()
        jonh.put()
        karls.put()
        kevinh.put()
        lees.put()
        liamc.put()
        markh.put()
        martinb.put()
        mikep.put()
        timp.put()

        edc.associate_character(joker, 'Ever toast with a Breville in the pale moonlight?')
        andrewh.associate_character(superted, 'I\'m from Build-a-Bear workshop')
        garys.associate_character(batman, 'I\'m Batman!')
        grantw.associate_character(theincrediblehulk, 'Hulk Smashed!')
        jasont.associate_character(bananaman, 'I\'ll show you mine if you show me yours ...')
        liamc.associate_character(spiderman, 'Your Friendly neighbourhood butt grabber')
