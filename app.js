const { createServer } = require('http')
const { Server } = require('socket.io')
const format = require('date-fns/format')


const httpServer = createServer()
const io = new Server(httpServer, {
  // options
})

io.on('connection', (socket) => {
  console.log('connected')

  socket.on('input', ({type, ...msg}) => {
    io.emit(type, msg);
  })
})

setInterval(()=>{
  const time = format(new Date(),'HH:mm')
  io.emit('clock', time)
}, 5*1000)

httpServer.listen(3000)