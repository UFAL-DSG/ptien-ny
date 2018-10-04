#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open('./key_transcriptions.txt') as r:
    for line in r:
        arr = line.split(' ')
        print arr
        with open('tmp/%s.wav.trn' % arr[0], 'w') as w:
            w.write(' '.join(arr[1:]))
