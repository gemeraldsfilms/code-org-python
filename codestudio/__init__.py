r"""The `codestudio` module contains all the <http://studio.code.org>
challenges and code to complete, extend, and add to them. Each challenge
is created in JSON and stored in `challenges`. Students complete the
challenges by completing the missing portions of the stub `py` files for
each challenge and then running them until they succeed. Challenges can
also be created using the `challenge.save(fname)` method. Successful
completions can optionally be reported to any accessible web site
supporting the `codestudio.progress` web API.

The only dependency is that standard Python 3 be installed from
<http://python.org>. This absence of other dependencies is by design to
best enable students, teachers, and developers to get up and running as
quickly as possible. This module requires only Python 3 with `tkinter`
and the standard sound libraries for each operating system from Multimedia
Services as described on <https://docs.python.org/3/library/mm.html>.

The implementation in `tkinter` has been abstracted away sufficient to be
replaced by other graphics libaries. This also allows the model itself to
be used to teach object-oriented programming without the distraction of
the graphics package implementation, which can later be taught through
its use as a graphics engine for this project. It also allows the base
`codestudio` domain and object model to be easily ported between different
object-oriented languages.

"""
__version = '1.0.1'
__author__ = 'Rob Muhlestein <rob@skilstak.com>'

import json
from .artist import ArtistChallenge
from .maze import MazeChallenge
from .farmer import FarmerChallenge
from os import path

def load(uid):
    '''Loads an artist challenge config (json) file'''
    fname = path.join('challenges',uid+'.json')
    assert path.isfile(fname), 'Challenge {} not yet ready.'.format(uid) 
    with open(fname, 'r') as f:
        config = json.load(f)
        if not 'uid' in config.keys(): config['uid'] = uid
        ctype = config['type']
        if ctype == 'artist':
            challenge = ArtistChallenge(config)
        elif ctype == 'maze':
            challenge = MazeChallenge(config)
        elif ctype == 'farmer':
            challenge = FarmerChallege(config)
        else:
            raise Exception('Invalid or missing challenge type')
    challenge.speed = 'fastest'
    challenge.setup()
    challenge.speed = 'normal'
    return challenge

def create(uid,ctype,start_direction=0):
    '''Combine with `save_as_solution()` to create new challenges'''
    fname = path.join('challenges',uid+'.json')
    assert not path.isfile(fname), '{} already exists'.format(fname)
    config = {
        'uid': uid,
        'start-direction': start_direction
    }
    if ctype == 'artist':
        challenge = ArtistChallenge(config)
    elif ctype == 'maze':
        challenge = MazeChallenge(config)
    elif ctype == 'farmer':
        challenge = FarmerChallege(config)
    return challenge
