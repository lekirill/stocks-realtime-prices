<template>
  <div id="app">
    <Dropdown
        :options=this.tickers
        :disabled="false"
        :maxItem="100"
        v-on:selected="changeSelectedTicker"
        placeholder="Please select ticker">
    </Dropdown>
    <LineChart
        v-bind:dataForRendering="this.dataForRendering"
        v-bind:key="selectedTicker"
    >

    </LineChart>
  </div>
</template>

<script>
import LineChart from './components/LineChart'
import Dropdown from 'vue-simple-search-dropdown'
import axios from 'axios'

axios.defaults.baseURL = process.env.VUE_APP_BASE_URL;
axios.defaults.headers = {'Content-Type': 'application/json;charset=UTF-8'};

export default {
  name: 'app',
  components: {
    LineChart,
    Dropdown,
  },
  data() {
    return {
      labels: [],
      data: {},
      tickers: [],
      realtimeData: {},
      dataForRendering: {},
      connection: null,
      selectedTicker: 0,
    }
  },
  methods :{
      searchTicker: function () {
      axios
          .get(axios.defaults.baseURL + '/tickers/')
          .then((response) => {
            this.tickers = [];
            response.data['ticker_list'].forEach(ticker => {
                this.tickers.push({'id': parseInt(ticker.split('_')[1]), 'name': ticker});
            })
          })

    },
    changeSelectedTicker: function (selection) {
      this.selectedTicker = selection.name;
      if (this.selectedTicker !== undefined){
        this.selectedTicker = selection.name;
        this.dataForRendering = JSON.parse(this.realtimeData)[this.selectedTicker];
      } else {
        this.dataForRendering = JSON.parse(this.realtimeData)[this.tickers[0].name];
      }
    },
  },
  created() {
    this.searchTicker();
    console.log("Starting connection to WebSocket Server")
    this.connection = new WebSocket("ws://0.0.0.0:8081/realtime")

    let self = this
    this.connection.onmessage = function(event) {
      self.realtimeData = event.data;
    }

    this.connection.onopen = function(event) {
      console.log(event)
      console.log("Successfully connected to the echo websocket server...")
    }
  }
}
</script>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }
</style>