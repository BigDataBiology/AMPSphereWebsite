<template>
  <div style="width:auto;margin:auto;height:auto;" id="BubbleMap"></div>
</template>

<script>
import Plotly from 'plotly.js/dist/plotly';


var data = [{
  type: 'scattergeo',
  mode: 'markers',
  locations: ['FRA', 'DEU', 'RUS', 'ESP', 'CHN'],
  marker: {
    size: [20, 30, 15, 10, 40],
    color: [100,100,100,100,100],
    cmin: 0,
    cmax: 100,
    colorscale: 'Reds',
    // colorbar: {
    //   title: 'Distribution',
    //   ticksuffix: '%',
    //   showticksuffix: 'last'
    // },
    line: {
      color: 'black'
    }
  },
}];

var layout = {
  // 'title': {
  //   'text': 'Geographical distribution',
  //   'side': 'bottom',
  // },
  'geo': {
    'scope': 'global',
    'resolution': 50,
    'showland': true,
    'landcolor': 'rgb(217, 217, 217)',
    'subunitwidth': 1,
    'countrywidth': 1,
    'subunitcolor': 'rgb(255,255,255)',
    'countrycolor': 'rgb(255,255,255)'
  },
  'margin': {
    'l': 30,
    'r': 30,
    't': 30,
    'b': 30
  }
};

export default {
  name: 'BubbleMap',
  // props: {
  //   data: Object,
  // },
  mounted() {
    Plotly.newPlot('BubbleMap', data, layout);
  }
}
</script>

<style scoped>

</style>