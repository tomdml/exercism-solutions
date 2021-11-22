def chunks(strand):
    for i in range(0, len(strand), 3):
        yield strand[i:i + 3]

def proteins(strand):
    proteins = {
        ('AUG',): 'Methionine',
        ('UUU', 'UUC'): 'Phenylalanine',
        ('UUA', 'UUG'): 'Leucine',
        ('UCU', 'UCC', 'UCA', 'UCG'): 'Serine',
        ('UAU', 'UAC'): 'Tyrosine',
        ('UGU', 'UGC'): 'Cysteine',
        ('UGG',): 'Tryptophan',
        ('UAA', 'UAG', 'UGA'): 0
    }

    proteindict = {}
    for (key, value) in proteins.items():
        proteindict.update(dict.fromkeys(key, value))

    res = [proteindict[codon] for codon in chunks(strand)]
    if 0 in res:
        return res[:res.index(0)]
    else:
        return res
