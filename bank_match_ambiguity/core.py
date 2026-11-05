import math,itertools
from decimal import Decimal
from fractions import Fraction
from .common import integer,identifier,unique_ids
def run(d):
 invoices=d['invoices'];payments=d['payments'];unique_ids(invoices);unique_ids(payments)
 if len(invoices)>12 or len(payments)>5:raise ValueError('bounds')
 amounts=[integer(r['cents'],1,10**9)for r in invoices];targets=[integer(r['cents'],1,10**9)for r in payments];matches=[]
 for target in targets:
  matches.append([mask for mask in range(1,1<<len(invoices))if sum(v for i,v in enumerate(amounts)if mask>>i&1)==target])
 solutions=[];visited=0;truncated=False
 def search(j,used,path):
  nonlocal visited,truncated
  visited+=1
  if visited>200000:truncated=True;return
  if j==len(payments):solutions.append(path);return
  for mask in matches[j]:
   if not used&mask:search(j+1,used|mask,path+[mask])
   if truncated:return
 search(0,0,[])
 def assignment(path):return {p['id']:[r['id']for i,r in enumerate(invoices)if path[j]>>i&1]for j,p in enumerate(payments)}
 return dict(allocations_found=len(solutions),complete=not truncated,visited=visited,examples=[assignment(s)for s in solutions[:20]],unique_proven=not truncated and len(solutions)==1,per_payment_subset_counts={p['id']:len(m)for p,m in zip(payments,matches)})
