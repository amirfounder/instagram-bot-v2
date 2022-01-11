export default Object.freeze({
  CONSOLE_SERVER_SOCKET_URL: 'ws://localhost:8001',
  SOCKET_MESSAGE_TYPES: {
    PROGRAM: 'program',
    TASKS: 'tasks'
  },
  SOCKET_MESSAGE_ACTIONS: {
    START_PROGRAM: 'start_program',
    END_PROGRAM: 'end_program'
  }
});
