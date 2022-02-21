const axios = require('axios')
const { get } = axios
const { io } = require("socket.io-client")

const getQuote = () => {
  get('https://zenquotes.io/api/random')
    .then(res => socket.emit(input, { type: 'quote', quote:`${res.data.q} - ${res.data.a}`}))
}

const socket = io('http://localhost:3000')

setInterval(getQuote, 10*1000)