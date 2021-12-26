import { buildStartActivityMessageDto } from "../../../utils/dtos"
import constants from "../../../utils/constants"
import socket from "../../../utils/sockets"

const {
  SOCKET_MESSAGE_TYPES: {
    START_ACTIVITY
  }
} = constants;


export const startInstagramAgent = (rootHashtag) => {
  const message = buildStartActivityMessageDto(START_ACTIVITY, rootHashtag)
  const json = JSON.stringify(message)

  socket.send(json)
}