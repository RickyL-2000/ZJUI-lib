import numpy as np
from collections import OrderedDict

class Lab2(object):
    
    def smith_waterman_alignment(self, s1, s2, penalties) :
        '''
        Input - two sequences and a dictionary with penalities for match, mismatch and gap
        Output - an integer value which is the maximum smith waterman alignment score
        '''
        #start code here
        m, n = len(s1), len(s2)
        dp = np.zeros((m+1, n+1), dtype=np.int32)
        max_score = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i, j] = max(dp[i-1, j-1] + penalties['match'], 
                                   dp[i-1, j] + penalties['gap'],
                                   dp[i, j-1] + penalties['gap'],
                                   0)
                else:
                    dp[i, j] = max(dp[i-1, j-1] + penalties['mismatch'], 
                                   dp[i-1, j] + penalties['gap'],
                                   dp[i, j-1] + penalties['gap'],
                                   0)
                if dp[i, j] > max_score:
                    max_score = dp[i, j]
        return max_score
        #end code here

    def print_smith_waterman_alignment(self,s1,s2,penalties) :
        '''
        Input - two sequences and a dictionary with penalities for match, mismatch and gap
        Output - a tuple with two strings showing the two sequences with '-' representing the gaps
        '''
        #start code here
        # if (len(s1) == 0):

        m, n = len(s1), len(s2)
        dp = np.zeros((m+1, n+1), dtype=np.int32)
        prev = [[-1 for j in range(n+1)] for i in range(m+1)]
        max_score = -1
        max_i, max_j = 0, 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                candidates = [(dp[i-1, j-1] + penalties['match'] if s1[i-1] == s2[j-1]
                                            else dp[i-1, j-1] + penalties['mismatch']), 
                              dp[i-1, j] + penalties['gap'],
                              dp[i, j-1] + penalties['gap'],
                              0]
                dp[i, j] = max(candidates)
                prev[i][j] = np.argmax(candidates)
                if dp[i, j] > max_score:
                    max_i, max_j = i, j
                    max_score = dp[i, j]
        # print(dp)
        # print(np.array(prev))
        # reconstruction
        res1, res2 = "", ""
        i, j = max_i, max_j
        while i > 0 and j > 0 and dp[i, j] > 0:
            direction = prev[i][j]
            if direction == 0:
                res1 = s1[i-1] + res1
                res2 = s2[j-1] + res2
                i, j = i-1, j-1
            elif direction == 1:
                res1 = s1[i-1] + res1
                res2 = '-' + res2
                i -= 1
            elif direction == 2:
                res1 = '-' + res1
                res2 = s2[j-1] + res2
                j -= 1
            else:
                break

        return res1, res2

        #end code here

    def find_exact_matches(self,list_of_reads,genome):
        
        '''
        Input - list of reads of the same length and a genome fasta file (converted into a single string)
        Output - a list with the same length as list_of_reads, where the ith element is a list of all locations (starting positions) in the genome where the ith read appears. The starting positions should be specified using the "chr2:120000" format
        '''
        
        #start code here
        if len(list_of_reads) == 0:
            return []
        if len(list_of_reads[0]) == 0:
            return [[] for _ in range(len(list_of_reads))]

        positions = self._find_exact_matches(list_of_reads, genome)

        # print(positions)

        ret = [[] for _ in range(len(list_of_reads))]
        for i in range(len(positions)):
            for pos in positions[i]:
                ret[i].append("chr{}:{}".format(pos[0], pos[1]))

        return ret
        #end code here


    def _find_exact_matches(self, list_of_reads, genome):
        """
        return value: a list of positions, where a position is a tuple with (chrN, idx)
        """
        L = len(list_of_reads[0])
        indexing = {}

        # process the genome data
        temp = genome.split('\n')[:-1]
        data = []
        cur = ""
        for i in range(len(temp)):
            if temp[i][0] == ">":
                if cur != "":
                    data.append(cur)
                    cur = ""
                continue
            cur = cur + temp[i]
        data.append(cur)

        # building dictionary
        for i in range(len(data)):
            for j in range(len(data[i]) - L + 1):
                if data[i][j: j+L] in indexing:
                    indexing[data[i][j: j+L]].append((i+1, j+1))
                else:
                    indexing[data[i][j: j+L]] = [(i+1, j+1)]

        # indexing
        ret = []
        for read in list_of_reads:
            if read in indexing:
                ret.append(indexing[read])
            else:
                ret.append([])

        return ret

    def _smith_waterman_alignment(self, s1, s2, penalties) :
        '''
        Input - two sequences and a dictionary with penalities for match, mismatch and gap
        Output - a tuple (start, end, score) where start and end are matched in s2 (0-based)
        '''
        m, n = len(s1), len(s2)
        dp = np.zeros((m+1, n+1), dtype=np.int32)
        prev = [[-1 for j in range(n+1)] for i in range(m+1)]
        max_score = -1
        max_i, max_j = 0, 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                candidates = [(dp[i-1, j-1] + penalties['match'] if s1[i-1] == s2[j-1]
                                            else dp[i-1, j-1] + penalties['mismatch']), 
                              dp[i-1, j] + penalties['gap'],
                              dp[i, j-1] + penalties['gap'],
                              0]
                dp[i, j] = max(candidates)
                prev[i][j] = np.argmax(candidates)
                if dp[i, j] > max_score:
                    max_i, max_j = i, j
                    max_score = dp[i, j]
        # print(dp)
        # print(np.array(prev))
        # reconstruction
        i, j = max_i, max_j
        start, end = 1, j
        while i > 0 and j > 0 and dp[i, j] > 0:
            direction = prev[i][j]
            start = j
            if direction == 0:
                i, j = i-1, j-1
            elif direction == 1:
                i -= 1
            elif direction == 2:
                j -= 1
            else:
                break
        # start = j

        return start-1, end-1, max_score
        #end code here

    
    def find_approximate_matches(self,list_of_reads,genome):
        '''
        Input - list of reads of the same length and a genome fasta file (converted into a single string)
        Output -  a list with the same length as list_of_reads, where the ith element is a list of all locations (starting positions) in the genome which have the highest smith waterman alignment score with ith read in list_of_reads
        '''
        
        #start code here
        if len(list_of_reads) == 0:
            return []
        if len(list_of_reads[0]) == 0:
            return [[] for _ in range(len(list_of_reads))]

        # data = genome.split('>chr')[1:]
        # for i in range(len(data)):
        #     data[i] = data[i][2:-1]

        # process the genome data
        temp = genome.split('\n')[:-1]
        data = []
        cur = ""
        for i in range(len(temp)):
            if temp[i][0] == ">":
                if cur != "":
                    data.append(cur)
                    cur = ""
                continue
            cur = cur + temp[i]
        data.append(cur)


        L = len(list_of_reads[0])
        k = L // 4
        penalities = {'match':1, 'mismatch':-1, 'gap':-1}
        threshold = 3   # the offset of start and end of reference

        ret = []
        scores = []
        for read in list_of_reads:
            score = []  # (chrN, idx, cur_score)
            sublist = [read[i: i+k] for i in range(len(read) - k + 1)]
            candidates = self._find_exact_matches(sublist, genome)
            for i in range(len(candidates)):
                for pos in candidates[i]:   # 1-based
                    # print("read len: {}; data len: {}".format(len(read), len(data[pos[0]-1])))
                    if len(read) > len(data[pos[0]-1]):   # read cannot be longer then genome
                        continue
                    # print("running here!")
                    if (i > 0) and ((pos[0], pos[1]-1) in candidates[i-1]):    # continuous index, checked last time
                        continue
                    # this is a first-time-shown-up index
                    start = max(0, pos[1]-1-i - threshold)  # 0-based
                    end = min(len(data[pos[0]-1]), pos[1]-1-i+L + threshold)  # 0-based
                    ref = data[pos[0]-1][start: end]
                    res = self._smith_waterman_alignment(read, ref, penalities) # 0-based
                    if (pos[0], start + res[0] + 1, res[2]) not in score:
                        score.append((pos[0], start + res[0] + 1, res[2]))
            scores.append(score)
            # find the max scores
            ret.append([])
            if len(score) == 0:
                continue
            score.sort(reverse=True, key=lambda x: x[2])
            ret[-1].append("chr{}:{}".format(score[0][0], score[0][1]))
            for i in range(1, len(score)):
                if score[i][2] != score[i-1][2]:
                    break
                ret[-1].append("chr{}:{}".format(score[i][0], score[i][1]))

        # print(scores)
        
        return ret

        #end code here

# module = Lab2()
# fakegenome_file=""
# with open(r"D:\GitHub\ZJUI-lib\ECE365\Genomics\lab2\fakegenome.fasta") as file:
#     fakegenome_file=file.read()
# penalties={'match':1,'mismatch':-1,'gap':-1}
# res = module.find_approximate_matches(["GATTACAT","CACAAACA"],fakegenome_file)
# print(res)
