const state = {
  dataLakeAnalyticsView: ''
}


const toggleLogRow = (e) => {
  e.classList.add('x-log-row-show-full')
}

const renderLogRow = () => {
  div = document.createElement('div')
  div.addAttribute('class', 'x-log-row')
  div.addEventListener('click', toggleLogRow)
}