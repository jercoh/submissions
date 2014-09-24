import thinkstats as ths
import first, survey
import math, operator

weights = [1,2,3,4,5,3,3,3,3]

def pumkin(t):
	variance = ths.Var(t)
	return ths.Mean(t), variance, math.sqrt(variance) 

def ex2_1():
	table = survey.Pregnancies()
	table.ReadRecords('.')
	firsts, others = first.PartitionRecords(table)
	lengths_firsts = [p.prglength for p in firsts.records]
	lengths_others = [p.prglength for p in others.records]
	return [pumkin(lengths_firsts),pumkin(lengths_others)]

def mode(hist):
	return max(hist.Items(), key=operator.itemgetter(1))

def all_modes(hist):
	return sorted(hist.Items(), key=operator.itemgetter(1),reverse=True)

def pmf_mean(pmf):
	return sum([t[0]*t[1] for t in pmf.Items()])

def pmf_var(pmf):
	return sum([t[1]*(t[0]-pmf_mean(pmf))**2 for t in pmf.Items()])



