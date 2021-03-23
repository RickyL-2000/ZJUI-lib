import pandas as pd
import statsmodels.api as sm 
import numpy as np
import statsmodels

class Lab3(object):
    
    def create_data(self,snp_lines) :
        '''
        Input - the snp_lines parsed at the beginning of the notebook
        Output - You should return the 53 x 3902 dataframe
        '''
        #start code here

        df = pd.DataFrame()
        for each in snp_lines:
            line = each.strip().split('\t')
            col_name = line[0] + ':' + line[1]
            line = line[9:]
            col = np.zeros(53)
            for i in range(53):
                if line[i][0] == '.':
                    col[i] = np.nan
                else:
                    col[i] = int(line[i][0]) + int(line[i][2])
            df[col_name] = col

        return df
        #end code here

    def create_target(self,header_line) :
        '''
        Input - the header_line parsed at the beginning of the notebook
        Output - a list of values(either 0 or 1)
        '''
        #start code here

        line = header_line.strip().split('\t')[9:]
        ret = []
        for dog in line:
            if dog[:4] == 'dark':
                ret.append(0)
            elif dog[:6] == 'yellow':
                ret.append(1)
        return ret

        #end code here
    
    def logistic_reg_per_snp(self,df) :
        '''
        Input - snp_data dataframe
        Output - list of pvalues and list of betavalues
        '''
        #start code here
        
        pvalues = []
        betavalues = []
        col_names = df.columns.tolist()[:-1]
        for i in range(len(col_names)):
            clf = sm.Logit(df['target'], sm.add_constant(df[col_names[i]]), missing='drop')
            res = clf.fit(method='bfgs', disp=False)
            betavalues.append(round(res.params[1], 5))
            pvalues.append(round(res.pvalues[1], 9))

        return pvalues, betavalues
        #end code here
    
    
    def get_top_snps(self,snp_data,p_values) :
        '''
        Input - snp dataframe with target column and p_values calculated previously
        Output - list of 5 tuples, each with chromosome and position
        '''
        #start code here
        
        #end code here