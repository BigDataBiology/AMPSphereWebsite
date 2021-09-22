<template>
  <div id="SearchResult">

  </div>
</template>

<script>
export default {
  name: "SearchResult",
  data() {
    return {
      job: '',
      method: '',
      result: {
        info: {
          pageSize: 5,
          totalPage: 1,
          totalRow: 1,
          currentPage: 1,
        },
        data: [],
      },
      loading: false
    }
  },
  created(){

  },
  mounted(){

  },
  computed(){

  },
  methods: {
    getSearchResult(){
      return [
        {
          // text search result
          "accession": "AMP10.000_000",
          "sequence": "KKVKSIFKKALAMMGENEVKAWGIGIK",
          "family": "SPHERE-III.001_396",
          "features": {
            "MW": 3005.685,
            "Length": 27,
            "Molar_extinction": {
              "cysteines_reduced": 5500,
              "cystines_residues": 5500
            },
            "Aromaticity": 0.074,
            "GRAVY": -0.111,
            "Instability_index": -18.348,
            "Isoelectric_point": 10.126,
            "Charge_at_pH_7": 4.759,
            "Secondary_structure": {
              "helix": 0.2962962962962963,
              "turn": 0.18518518518518517,
              "sheet": 0.2962962962962963
            },
            //...
          }
        },
        {
          // hmmsearch result
          "query_accession": "-",
          "query_length": 27,
          "query_name": "SPHERE-III.001_396",
          "target_accession": "-",
          "target_length": 27,
          "target_name": "submitted_sequence",
          "E_value": 7.1e-25,
          "acc": 0.99,
          "bias": 9.2,
          "c_Evalue": 7.399999999999999e-25,
          "i_Evalue": 7.399999999999999e-25,
          "num_domain": 1,
          "domain_index": 1,
          "score": 72.6,
          "from_ali": 1,
          "from_env": 1,
          "from_hmm": 1,
          "to_ali": 27,
          "to_env": 27,
          "to_hmm": 27,
          "description_of_target": "-"
        },
        {
          // mmseqs result
          "query_identifier": "submitted_sequence",
          "target_identifier": "AMP10.000_000",
          "sequence_identity": 0.942,
          "alignment_length": 27,
          "number_mismatches": 2,
          "number_gap_openings": 0,
          "domain_start_position_query": 1,
          "domain_end_position_query": 27,
          "domain_start_position_target": 1,
          "domain_end_position_target": 27,
          "E_value": 2.42e-11,
          "bit_score": 56
        }
      ]
    }
  }
}
</script>

<style scoped>

</style>