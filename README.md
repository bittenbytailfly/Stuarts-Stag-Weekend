Stuart's Stag Weekend
=====================

As best (and arguably most geeky) man at my friend Stuart's wedding, it's my duty to organise 24 people for a superhero themed stag weekend.

The plan is to have everyone select a hero, ensuring the following:

    * Characters must be chosen from an approved list
    * There are to be no duplicates

Trying to arrange this via email was proving problematic (given the distributed nature of people) so I decided to create an application for it.

The finished product will eventually be hosted here:

<http://cardiffcapers.ejcarter.com> (NOTE: you will not be enter the selection process unless you have the keys for participants - emailed individually)

## Technology

Along with being a useful tool to help with organisation, it's been an excuse to use the following technology, and may serve as a reference for anyone building a site in similar technology at a later date:

    * Google App Engine (Python)
    * ndb Data Storage
    * AngularJs
    * CSS3 Animations
    * Google Fonts

## Usage

Should you wish to use this yourself (maybe you're doing something similar) - you'll need to run the setup process first. Simply modify the `setup.py` file in the models folder (should be self explanatory) and then run the application, hitting the URL `/populate` to populate the datastore.

##License

MIT license - [http://www.opensource.org/licenses/mit-license.php](http://www.opensource.org/licenses/mit-license.php)