import constants from "./constants";

const socket = new WebSocket(constants.CONSOLE_SERVER_SOCKET_URL)

const onWebSocketOpen = (e) => {
  console.log(e)
}

const onWebSocketClose = (e) => {
  console.log(e)
}

const onWebSocketError = (e) => {
  console.log(e)
}

const onWebSocketMessage = (e) => {
  console.log(e)
}

socket.addEventListener('close', onWebSocketClose)
socket.addEventListener('error', onWebSocketError)
socket.addEventListener('message', onWebSocketMessage)
socket.addEventListener('open', onWebSocketOpen)

export default socket;