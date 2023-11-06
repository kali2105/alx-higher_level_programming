#!/usr/bin/python3
'''A fct defining a class MyInt that inherits from int'''


class MyInt(int):
    '''Invert int operators '==' and '!=' '''

    def __eq__(self, value):
        '''Override '==' opeartor with '!=' behavior'''
        return self.real != value

    def __ne__(self, value):
        '''override '!=' operator with '==' behavior'''
        return self.real == value
