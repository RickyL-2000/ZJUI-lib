import numpy as np
from collections import OrderedDict

class Lab1(object):
    def parse_reads_illumina(self,reads: str) :
        '''
        Input - Illumina reads file as a string
        Output - list of DNA reads
        '''
        #start code here
        rows = reads.split('\n')
        return [rows[i] for i in range(1, len(rows), 4)]
        #end code here

    def unique_lengths(self,dna_reads) :
        '''
        Input - list of dna reads
        Output - set of counts of reads
        '''
        #start code here
        ret = set()
        for dna in dna_reads:
            ret.add(len(dna))
        return ret
        #end code here

    def check_impurity(self,dna_reads) :
        '''
        Input - list of dna reads
        Output - list of reads which have impurities, a set of impure chars 
        '''
        #start code here
        impure_reads_illumina = []
        impure_chars_illumina = set()
        for dna in dna_reads:
            for symbol in 'BDEFHIJKLMNOPQRSUVWXYZ':
                if symbol in dna:
                    impure_reads_illumina.append(dna)
                    impure_chars_illumina.add(symbol)
                    break
        return impure_reads_illumina, impure_chars_illumina
        #end code here

    def get_read_counts(self,dna_reads) :
        '''
        Input - list of dna reads
        Output - dictionary with key as read and value as the no. of times it occurs
        '''
        #start code here
        ret = {}
        for dna in dna_reads:
            if dna in ret:
                ret[dna] += 1
            else:
                ret[dna] = 1
        return ret
        #end code here

    def parse_reads_pac(self,reads_pac: str):
        '''
        Input - pac bio reads file as a string
        Output - list of dna reads
        '''
        #start code here
        lines = reads_pac.split('\n')
        ret = []
        cur_dna = ''
        for line in lines:
            if len(line) == 0:
                continue
            if line[0] == '>' and cur_dna != '':
                ret.append(cur_dna)
                cur_dna = ''
                continue
            if line[0] != '>':
                cur_dna = cur_dna + line
        if cur_dna != '':
            ret.append(cur_dna)
        return ret
        #end code here
