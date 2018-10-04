#!/usr/bin/env python3
# encoding: utf-8
import os
import sys
import xml.etree.cElementTree as etree

def parse_file(name):
    xmlDoc = open(name, 'r')
    xmlDocData = xmlDoc.read()
    xmlDocTree = etree.XML(xmlDocData)

    golds = []
    hyps = []

    # for trans in xmlDocTree.iter('asr_transcription'):
    #     transs.append(trans.text)

    for turn in xmlDocTree.iter('turn'):
        hyp = None 
        gold = None
        for child in turn:
            if child.tag == 'asr' and child[0].text is not None:
                print child
                hyp = child[0].text
            if child.tag == 'asr_trascription' and child.text is not None:
                gold = child.text
        if gold is not None and hyp is not None:
            hyps.append(hyp)
            golds.append(gold)
            
    return hyps, golds

def find_all(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result

if __name__ == '__main__':
    d = sys.argv[1]
    out_h = sys.argv[2]
    out_t = sys.argv[3]
    asr_trans = find_all('asr_transcribed.xml', d)
    with open(out_h, 'w') as h:
        with open(out_t, 'w') as t:
            for f in asr_trans:
                print('parsing file ', f)
                hs, gs = parse_file(f) 
                h.write('\n'.join(hs))
                t.write('\n'.join(gs))
