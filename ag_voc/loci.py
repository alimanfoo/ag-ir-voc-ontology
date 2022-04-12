from .abc import LocusOfConcern, ag_voc_ontology  # Locus,; LocusOfInterest,

with ag_voc_ontology:

    vgsc_locus = LocusOfConcern(
        "AGAP004707", label="Vgsc (AGAP004707)", locus_coords="2L:2,358,158-2,431,617"
    )
