export default Object.freeze({
  CONSOLE_SERVER_SOCKET_URL: 'ws://localhost:8001',
  TYPES: {
    PROGRAM: 'program',
    TASK: 'task'
  },
  STATUSES: {
    QUEUED: 'queued',
    RUNNING: 'running',
    ABORTED: 'aborted',
    COMPLETED: 'completed',
    PAUSED: 'paused'
  },
  METHODS: {
    ABORT: 'abort',
    PAUSE: 'pause',
    START: 'start',
    SAVE: '',
    UPDATE: ''
  },
});
