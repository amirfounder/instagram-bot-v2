import constants from "../utils/constants"
import socket from "./socket"


const {
  TYPES: {
    PROGRAM,
    TASK,
  },
  METHODS: {
    SAVE,
    START,
    UPDATE,
  }
} = constants


export const createTask = (data) => {
  const payload = {
    type: TASK,
    method: SAVE,
    data
  }

  const message = JSON.stringify(payload)
  socket.send(message)
}

export const updateTask = (data) => {
  const payload = {
    type: TASK,
    method: UPDATE,
    data
  }

  const message = JSON.stringify(payload)
  socket.send(message)
}

export const startProgram = (data) => {
  const payload = {
    type: PROGRAM,
    method: START,
    data
  }

  const message = JSON.stringify(payload)
  socket.send(message)
}