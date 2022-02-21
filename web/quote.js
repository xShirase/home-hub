const axios = require('axios')
const { get } = axios
const { io } = require("socket.io-client")

const getQuote = () => {
  try{
    get('https://zenquotes.io/api/random')
      .then(res => socket.emit('input', { type: 'quote', quote:`${res.data[0].a} - ${res.data[0].q}`}))
      .then(()=>console.log('ok'))
    }
  catch(err){
    console.log('error')
  }
}

const socket = io('http://localhost:3000')
getQuote()
setInterval(getQuote, 10*60*1000)
