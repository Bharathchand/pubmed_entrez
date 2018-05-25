from Bio import Entrez
from Bio import Entrez, Medline
import urllib2
import socket

y = raw_input("Enter the keyword: \n")

Entrez.email = "Your.Name.Here@example.org"
term = y

handle = Entrez.esearch(db="pubmed", retmax = 2, term=term)
record = Entrez.read(handle)
recount = record['Count']
handle = Entrez.esearch(db="pubmed",retmax = recount , term=term)
record = Entrez.read(handle)

for ref in record['IdList']:
    handle = Entrez.efetch(db="pubmed", id=ref, rettype="Medline", retmode="text")
    paper = Medline.read(handle)
    try:
        print 'TITLE:    ', paper['TI']
        print 'AUTHOR:    ', paper['AU']
        
    except Exception:
        pass
    print '\n'
    
