#!usr/bin/python3

def _kmers(sequence, k):
    """Return every k-mer in order, including repeated k-mers."""
    if k <= 0 or k > len(sequence):
        return []
    list_kmers =[]
    for i in range(len(sequence) - k + 1):
        list_kmers.append(sequence[i:i + k])
    return list_kmers


def _lowest_common_ancestor(taxa, taxonomy):
    """Return the most specific ancestor shared by all taxa."""
    if len(taxa) == 0:
        return None
    # Build a lineage for each taxon.
    lineages = []
    for taxon in taxa:
        ancestors = []
        while taxon is not None:
            ancestors.append(taxon)
            taxon = taxonomy[taxon]
        lineages.append(ancestors)
    # Find the first ancestor shared by every lineage.
    for ancestor in lineages[0]:
        shared = True
        for lineage in lineages:
            if ancestor not in lineage:
                shared = False
                break
        if shared:
            return ancestor
    return "root"


def build_kmer_taxon_index(reference_sequences, k):
    """Connect every reference k-mer to the taxa containing it."""
    index = {}
    for taxon, sequence in reference_sequences.items():
        list_kmers = _kmers(sequence, k)
        for kmer in list_kmers:
            if kmer not in index:
                index[kmer] = set()
            index[kmer].add(taxon)
    return index


def classify_read(read, k, kmer_index, taxonomy):
    """Let matching k-mers vote for taxa or shared ancestors."""
    votes = {}
    list_kmers = _kmers(read, k)
    for kmer in list_kmers:
        matching_taxa = kmer_index.get(kmer, set())
        if matching_taxa:
            taxon = _lowest_common_ancestor(matching_taxa, taxonomy)
            votes[taxon] = votes.get(taxon, 0) + 1

    return votes


taxonomy = {"root": None, "Bacteria": "root", "E_coli": "Bacteria", "S_enterica": "Bacteria"}

k=2
references = {"E_coli": "ATGC", "S_enterica": "ATGA"}


kmer_index = build_kmer_taxon_index(references, k)
results = classify_read("ATGC", k, kmer_index, taxonomy)
kmer_ii={}

while k <= 4:
    kmer_ii=(build_kmer_taxon_index(references, k))
    print(kmer_ii)
    results=classify_read("ATGC", k, kmer_ii, taxonomy)
    k += 1


# 1.2
# {'AT': {'S_enterica', 'E_coli'}, 'TG': {'S_enterica', 'E_coli'}, 'GC': {'E_coli'}, 'GA': {'S_enterica'}}
# {'ATG': {'S_enterica', 'E_coli'}, 'TGC': {'E_coli'}, 'TGA': {'S_enterica'}}
# {'ATGC': {'E_coli'}, 'ATGA': {'S_enterica'}}

# 1.3
# k=3 sequence = 'ATGA'
# {'ATG': {'S_enterica', 'E_coli'}, 'TGC': {'E_coli'}, 'TGA': {'S_enterica'}}
# {'Bacteria': 1, 'S_enterica': 1}