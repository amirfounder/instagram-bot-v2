export const buildMessageDto = (m_type, m_value) => ({
  type: m_type || null,
  value: m_value || null,
})