""" index all of your bams, now in PARALLEL! """
import os
import multiprocessing as mp


def samtools_index(subdir):
	""" run samtools_index, for a given cell """
	print(subdir)
	cmd = 'samtools index ' + subdir + '/*.bam'
	#print(cmd)
	os.system(cmd)



""" main """
cwd = os.getcwd()
subdirs = os.listdir(cwd)

p = mp.Pool(processes=16)

try:
	cells_list = p.map(samtools_index, subdirs, chunksize=1) # default chunksize=1
finally:
	p.close()
	p.join()

