import { startProgram } from "../../../../sockets/controller"

export const startAgentService = () => {
  startProgram({
    name: 'InstagramAgent'
  })
}