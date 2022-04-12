from owlready2 import *

# TODO change IRI to a PURL
ag_voc_ontology = get_ontology("http://example.org/ag_voc/ontology")

with ag_voc_ontology:

    class Locus(Thing):
        label = "Locus"
        comment = """
            A genome region defined by a specified contig with start and stop
            coordinates.
        """

    class LocusOfConcern(Locus):
        label = "Locus of Concern"
        comment = """
            A locus within which sequence variants are known to occur that
            alter the mosquito phenotype in a way that could impact public
            health and may require mitigating action.
        """

    class LocusOfInterest(Locus):
        label = "Locus of Interest"
        comment = """
            A locus within which sequence variants may occur that alter the
            mosquito phenotype in a way that could impact public health, but
            which requires further investigation.
        """

    AllDisjoint([LocusOfConcern, LocusOfInterest])

    class Haplotype(Thing):
        label = "Haplotype"
        comment = """
            A DNA sequence spanning a locus and possibly carrying one or more
            sequence variants.
        """

    class HaplotypeOfConcern(Haplotype):
        label = "Haplotype of Concern"
        comment = """
            A haplotype which carries sequence variants that alter the mosquito
            phenotype in a way that could impact public health and may require
            mitigating action.
        """

    class HaplotypeOfInterest(Haplotype):
        label = "Haplotype of Interest"
        comment = """
            A haplotype which may carry sequence variants that alter the
            mosquito phenotype in a way that could impact public health but
            which requires further investigation.
        """

    AllDisjoint([HaplotypeOfConcern, HaplotypeOfInterest])

    class locus_region(DataProperty, FunctionalProperty):
        domain = [Locus]
        range = [str]

    class haplotype_locus(ObjectProperty, FunctionalProperty):
        domain = [Haplotype]
        range = [Locus]

    class haplotype_variant(ObjectProperty):
        domain = [Haplotype]
        range = [str]
