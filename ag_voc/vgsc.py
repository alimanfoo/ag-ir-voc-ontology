from textwrap import dedent

from .abc import (
    Haplotype,
    HaplotypeOfConcern,
    HaplotypeOfInterest,
    Locus,
    LocusOfConcern,
    ag_voc_ontology,
    haplotype_locus,
    haplotype_variant,
)

with ag_voc_ontology:

    vgsc_locus = Locus(
        "AGAP004707", label="Vgsc (AGAP004707)", locus_coords="2L:2,358,158-2,431,617"
    )

    class VgscHaplotype(Haplotype):
        label = "Vgsc Haplotype"
        comment = dedent(
            """
            Any haplotype spanning the Vgsc locus.
        """
        )
        equivalent_to = [Haplotype & haplotype_locus.value(vgsc_locus)]

    class Vgsc_L995S(VgscHaplotype):
        label = "Vgsc+L995S"
        comment = dedent(
            """
            Any haplotype spanning the Vgsc locus and carrying the L995S amino
            acid substitution.
        """
        )
        equivalent_to = [VgscHaplotype & haplotype_variant.value("AGAP004707-RD:L995S")]

    class Vgsc_L995F(VgscHaplotype):
        label = "Vgsc+L995F"
        comment = dedent(
            """
            Any haplotype spanning the Vgsc locus and carrying the L995F amino
            acid substitution.
        """
        )
        equivalent_to = [VgscHaplotype & haplotype_variant.value("AGAP004707-RD:L995F")]

    class Vgsc_L995F_N1570Y(VgscHaplotype):
        label = "Vgsc+L995F+N1570Y"
        comment = dedent(
            """
            Any haplotype spanning the Vgsc locus and carrying the L995F and
            N1570Y amino acid substitutions.
        """
        )
        equivalent_to = [Vgsc_L995F & haplotype_variant.value("AGAP004707-RD:N1570Y")]

    class Vgsc_V402L_I1527T(VgscHaplotype):
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

    class Vgsc_F1(VgscHaplotype):
        label = "Vgsc/F1"
        comment = dedent(
            """
            Haplotypes belonging to the F1 group as defined by Clarkson et
            al. (2021). All members of this group carry the L995F amino acid
            substitution by definition.
        """
        )
        equivalent_to = [
            Vgsc_L995F
            & haplotype_variant.value("2L:2,422,611:A>T")  # TODO use real variants
            & haplotype_variant.value("2L:2,422,699:C>G")  # TODO use real variants
            # TODO fill in all known variants
        ]

    class Vgsc_F1_N1570Y(VgscHaplotype):
        label = "Vgsc/F1+N1570Y"
        comment = dedent(
            """
            Haplotypes belonging to the F1 group as defined by Clarkson et
            al. (2021) and carrying the N1570Y substitution. All members of
            the F1 group carry the L995F amino acid substitution by definition.
        """
        )
        equivalent_to = [Vgsc_F1 & Vgsc_L995F_N1570Y]

    # status
    vgsc_locus.is_a.append(LocusOfConcern)
    Vgsc_L995F.is_a.append(HaplotypeOfConcern)
    Vgsc_L995S.is_a.append(HaplotypeOfConcern)
    Vgsc_V402L_I1527T.is_a.append(HaplotypeOfInterest)
