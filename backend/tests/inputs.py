is_case_nonsensitive = True  # TODO fixhere.
AMP_accessions = {'AMP10.000.000'}
family_accessions = {'SPHERE-III.000.000', 'SPHERE-II.000.000'}
hosts = {'Sus scrofa', 'Zea mays', 'Homo sapiens'}
habitats = {'host-associated:animal host:digestive tract:intestine', 'host-associated:plant host:rhizosphere'}
samples = {'haib18CEM5332_HMGW3CCXY_SL342458', 'orion-mom_HD.S47-x-224-x-ST'}  # TODO test with empty value ('')?
origins = {'root', 'Zoogloea', 'Xanthobacteraceae', 'unclassified'}
sequences = {'KKVKSIFKKALAMMGENEVKAWGIGIK', 'LLLVLVLVVLCLCLCL', 'WRWRWRRRRWRWRGIK'}
unexpected_inputs = {'foo', 'bar', 'null', 'none', ' '}


# TODO update: send right http response code.
# TODO test: input url, see if response status code is what we expect.