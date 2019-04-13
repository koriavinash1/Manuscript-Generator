import pandas as pd
import numpy as np

abstracts = pd.read_csv('../data/Arxiv_Text_Data_CS_QBIO_STAT_LARGE.csv')['abstract'].as_matrix()

unconditional = open('../data/unconditional_gpt2.txt', 'w')
for i, abstract in enumerate(abstracts):
	unconditional.write("======================================== SAMPLE " + str(i+1) + " ========================================")
	unconditional.write("\n")
	unconditional.write(abstract)
	unconditional.write("\n")

unconditional.close()

