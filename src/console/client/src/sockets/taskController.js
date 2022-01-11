import socket from "./socket"


export const createTask = (data) => {
  const payload = ({
    type: 'task',
    method: 'save',
    data: data
  })

  const message = JSON.stringify(payload)
  socket.send(message)
}

export const updateTask = (data) => {
  const payload = ({
    type: 'task',
    method: 'update',
    data: data
  })

  const message = JSON.stringify(payload)
  socket.send(message)
}