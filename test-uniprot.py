import uniprot
from pprint import pprint

seqids, fastas = uniprot.read_fasta('target.fasta')

pprint(seqids)
pprint(fastas)

seqids = "NP_000508.1  NP_001018081.3".split()
pairs = uniprot.batch_uniprot_id_mapping_pairs('P_REFSEQ_AC', 'ACC', seqids)
pprint(pairs, indent=2)
    




