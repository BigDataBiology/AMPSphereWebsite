<template>
<div id="BarPlot"></div>
</template>

<script>
import Plotly from 'plotly.js/dist/plotly';
import events from './events'
// import {nextTick} from 'vue'


console.log('component inited')
var layout = {
  // title: 'Colored Bar Chart',
  barmode: 'stack'
};

export default {
  name: "BarPlot",
  props: {
    distribution: {
      type: Object,
    }
  },
  data () {
    return {
    }
  },
  mounted() {
    // console.log('distribution data received.')
    Plotly.newPlot('BarPlot', this.distribution, layout)
    events.forEach(evt => {
      this.$el.on(evt.completeName, evt.handler(this));
    });
  },
  watch:{
    distribution:{
      handler() {
        this.$nextTick(() => {
        Plotly.newPlot('BarPlot', this.distribution, layout)
        console.log('distribution data received.')
        })
      },
      immediate: true
    }
  },
  methods:{

  }
}
</script>

<style scoped>

</style>