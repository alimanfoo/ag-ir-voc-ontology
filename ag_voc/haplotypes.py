from textwrap import dedent

from .abc import (  # HaplotypeOfInterest,
    Haplotype,
    HaplotypeOfConcern,
    ag_voc_ontology,
    haplotype_locus,
    haplotype_variant,
)
from .loci import vgsc_locus

with ag_voc_ontology:

    class VgscHaplotype(Haplotype):
        label = "Vgsc Haplotype"
        comment = dedent(
            """
            Any haplotype spanning the Vgsc locus.
        """
        )
        equivalent_to = [Haplotype & haplotype_locus.value(vgsc_locus)]

    class Vgsc_L995S(HaplotypeOfConcern):
        label = "Vgsc+L995S"
        comment = dedent(
            """
            Any haplotype spanning the Vgsc locus and carrying the L995S amino
            acid substitution.
        """
        )
        equivalent_to = [VgscHaplotype & haplotype_variant.value("AGAP004707-RD:L995S")]

    class Vgsc_L995F(HaplotypeOfConcern):
        label = "Vgsc+L995F"
        comment = dedent(
            """
            Any haplotype spanning the Vgsc locus and carrying the L995F amino
            acid substitution.
        """
        )
        equivalent_to = [VgscHaplotype & haplotype_variant.value("AGAP004707-RD:L995F")]

    class Vgsc_L995F_N1570Y(HaplotypeOfConcern):
        label = "Vgsc+L995F+N1570Y"
        comment = dedent(
            """
            Any haplotype spanning the Vgsc locus and carrying the L995F and
            N1570Y amino acid substitutions.
        """
        )
        equivalent_to = [
            VgscHaplotype
            & haplotype_variant.value("AGAP004707-RD:L995F")
            & haplotype_variant.value("AGAP004707-RD:N1570Y")
        ]

    class Vgsc_V402L_I1527T(HaplotypeOfConcern):
        label = "Vgsc+V402L+I1527T"
        comment = dedent(
            """
            Any haplotype spanning the Vgsc locus and carrying the V402L and
            I1527T amino acid substitutions.
        """
        )
        equivalent_to = [
            VgscHaplotype
            & haplotype_variant.value("AGAP004707-RD:V402L")
            & haplotype_variant.value("AGAP004707-RD:I1527T")
        ]
