#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Wordfence (Defiant)'


def is_waf(self):
    if self.matchHeader(('Server', r'wf[_\-]?WAF')):
        return True

    if self.matchContent(r"Generated by Wordfence"):
        return True

    if self.matchContent(r'broke one of (the )?Wordfence (advanced )?blocking rules'):
        return True

    if self.matchContent(r"/plugins/wordfence"):
        return True

    return False
