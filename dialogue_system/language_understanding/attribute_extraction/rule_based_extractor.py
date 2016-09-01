# -*- coding: utf-8 -*-
import re


#from dialogue_system.knowledge.reader import read_names, read__private_comments, read_lectures
from dialogue_system.knowledge.reader import read_names, read_private_comment_from_tutor, read_class_comment_from_teacher, read_condition

import MeCab


class RuleBasedAttributeExtractor(object):

    def __init__(self):
        self.__names = read_names()

    def extract(self, bot, text):
        name = self.__extract_name(text)
        attribute = {
                'NAME': name, 
                'PRIVATE_COMMENT_FROM_TUTOR': read_private_comment_from_tutor(name),
                'CLASS_COMMENT_FROM_TEACHER': read_class_comment_from_teacher(name),
                'CONDITION':self.__extract_condition(text, bot),
                }
        print(attribute)

        return attribute

    def __extract_name(self, text):
        names = [name for name in self.__names if name in text]
        names.sort(key=len, reverse=True)
        name = names[0] if len(names) > 0 else ''
        return name
    
    def __extract_condition(self, text, bot):
        if bot.manager.dialogue_state.get_name() != '' and not bot.manager.dialogue_state.has('IS_ASKED_CONDITION'):
            bot.manager.dialogue_state.update({'IS_ASKED_CONDITION':True})
            print('a')
            return read_condition(text)
        else:
            print('b')
            return ''
