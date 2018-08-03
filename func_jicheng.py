#!/usr/bin/env python
# coding=utf-8

class animal():

    def __init__(self,name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self,value):
        self._name = value

    def bark(self):
        pass

class dog(animal):

    def bark(self):
        print(self.get_name()+' is making sound w w w ')

class cat(animal):

    def bark(self):
        print(self.get_name()+' is making sound m m m  ')

if __name__ == '__main__':
    Dog = dog('wang cai')
    Cat = cat('kitty')
    Dog.bark()
    Cat.bark()
