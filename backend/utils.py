def get_features(seq):
    """
    @Celio.
    :param seq:
    :return:
        Dict{
            MW: ...,
            Length: ...,
            Molar_extinction: [..., ...],
            Aromaticity: ...,
            GRAVY: ...,
            Instability_index: ...,
            Isoeletric_point: ...,
            Charget_at_pH_7: ...,
            Secondary_structure: [..., ..., ...],
        }
    """
    pass


def get_enzyme_energy(seq):
    """
    @Celio
    :param seq:
    :return: a dict representing the coordinate of data points on the enzyme energy graph.
        Dict{
            x: [..., ..., ..., ...]
            y: [..., ..., ..., ...]
        }
    """
    pass


def get_hydrophobicity_parker(seq):
    """
    @Celio
    :param seq:
    :return: a dict representing the coordinate of data points on the hydrophobicity_parker graph.
        Dict{
            x: [..., ..., ..., ...]
            y: [..., ..., ..., ...]
        }
    """
    pass


def get_surface_accessibility(seq):
    """
    @Celio
    :param seq:
    :return: a dict representing the coordinate of data points on the surface_accessibility graph.
        Dict{
            x: [..., ..., ..., ...]
            y: [..., ..., ..., ...]
        }
    """
    pass


def get_flexibility(seq):
    """
    @Celio
    :param seq:
    :return: a dict representing the coordinate of data points on the flexibility graph.
        Dict{
            x: [..., ..., ..., ...]
            y: [..., ..., ..., ...]
        }
    """
    pass


def get_geo_distribution(data):
    pass


def get_habitat_distribution(data):
    pass


def get_host_distribution(data):
    pass


def get_origin_distribution(data):
    pass


def get_search_results(seq, search_using):
    """

    :param seq: sequence
    :param search_using: {mmSeqs, HMMsearch}
    :return:
    """
    pass

