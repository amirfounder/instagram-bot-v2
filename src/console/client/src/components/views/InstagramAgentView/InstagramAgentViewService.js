import { buildMessageDto } from "../../../dtos/messageDto"
import socket from "../../../utils/sockets"

export const startInstagramAgent = (rootHashtag) => {
  const message = buildMessageDto('start_activityz', rootHashtag)
  const json = JSON.stringify(message)
  socket.send(json)
}