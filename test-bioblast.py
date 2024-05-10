from Bio.Blast import NCBIWWW

# Your protein sequence
protein_sequence = "MLLLPLPLLLFLLCSRAEAGEIIGGTESKPHSRPYMAYLEIVTSNGPSKFCGGFLIRRNFVLTAAHCAGRSITVTLGAHNITEEEDTWQKLEVIKQFRHPKYNTSTLHHDIMLLKLKEKASLTLAVGTLPFPSQKNFVPPGRMCRVAGWGRTGVLKPGSDTLQEVKLRLMDPQACSHFRDFDHNLQLCVGNPRKTKSAFKGDSGGPLLCAGVAQGIVSYGRSDAKPPAVFTRISHYRPWINQILQAN"

# Perform BLAST search
result_handle = NCBIWWW.qblast("blastp", "nr", protein_sequence)

# Save the result to a file (optional)
with open("my_blast_result.xml", "w") as out_handle:
    out_handle.write(result_handle.read())
