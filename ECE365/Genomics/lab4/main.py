import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
class Lab4(object):

    def _E_step(self, abundances, read_mapping):
        '''
        Input - abundances array(n_transcripts)
              - read_mapping list(n_reads, n_transcripts) (concise way)
        Output - Z_mapping array(n_reads, n_transcripts)
        '''
        n_reads = len(read_mapping)
        n_transcripts = 30
        Z_mapping = np.zeros((n_reads, n_transcripts))
        for i, read in enumerate(read_mapping):
            for idx in read:
                Z_mapping[i, idx] = abundances[idx]
            Z_mapping[i] /= np.sum(Z_mapping[i])
        return Z_mapping

    def _M_step(self, Z_mapping, tr_lengths, n_reads):
        '''
        Output - abundances array(n_transcripts)
        '''
        abundances = np.sum(Z_mapping, axis=0) / n_reads
        for i in range(len(abundances)):
            abundances[i] /= tr_lengths[i]
        abundances /= np.sum(abundances)
        return abundances

    def expectation_maximization(self,read_mapping,tr_lengths,n_iterations) :
        '''
        Input - read_mapping (n_reads, n_transcripts) (concise way)
        Output - history (n_transcripts, n_iterations+1)
        '''
        #start code here
        n_transcripts = 30
        history = np.zeros((n_transcripts, n_iterations+1))
        # init the abundance
        abundances = np.ones(n_transcripts) / n_transcripts
        history[:, 0] = np.copy(abundances)

        # iterate
        for i in range(n_iterations):
            Z_mapping = self._E_step(abundances, read_mapping)
            abundances = self._M_step(Z_mapping, tr_lengths, len(read_mapping))
            history[:, i+1] = np.copy(abundances)
        
        return history.tolist()
        #end code here

    def prepare_data(self,lines_genes) :
        '''
        Input - list of strings where each string corresponds to expression levels of a gene across 3005 cells
        Output - gene expression dataframe
        '''
        #start code here
        n_genes = len(lines_genes)
        df = pd.DataFrame()
        for i in range(n_genes):
            col = lines_genes[i].strip().split()
            col = np.array([int(j) for j in col])
            col = np.log(1 + col)
            df['Gene_{}'.format(i)] = col
        
        return df.round(5)

        #end code here
    
    def identify_less_expressive_genes(self,df) :
        '''
        Input - gene expression dataframe
        Output - list of column names which are expressed in less than 25 cells
        '''
        #start code here
        n_cells, n_genes = df.shape
        ret = []
        for i in range(n_genes):
            if np.sum(df['Gene_{}'.format(i)] > 0) < 25:
                ret.append('Gene_{}'.format(i))
        return ret
        #end code here
    
    
    def perform_pca(self,df) :
        '''
        Input - df_new
        Output - numpy array containing the top 50 principal components of the data.
        '''
        #start code here
        pca = PCA(n_components=50, svd_solver='randomized', random_state=365)
        return np.round(pca.fit_transform(df), 5)
        #end code here
    
    def perform_tsne(self,pca_data) :
        '''
        Input - pca_data
        Output - numpy array containing the top 2 tsne components of the data.
        '''
        #start code here
        enc = TSNE(n_components=2, perplexity=50, random_state=1000)
        return enc.fit_transform(pca_data)
        #end code here