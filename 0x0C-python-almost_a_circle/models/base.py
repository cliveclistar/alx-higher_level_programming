#!/usr/bin/python3
'''Module for Base Class.'''


class Base:
    '''A representation of the base of our OOP hierarchy.'''

    _nb_objects = 0

    def_init_(self, id=None):
        '''Constructor.'''
        if id is not None:
            self.id = id
        else:
            Base._nb_objects += 1
            self.id = Base._ab_object
