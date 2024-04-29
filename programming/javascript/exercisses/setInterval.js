function main() {
  const intervalId = setInterval(logMessage, 2000)

  setTimeout(function () {
    clearInterval(intervalId)
    console.log('Logging stopped after 10 seconds')
  }, 10000)
}

function logMessage() {
  console.log('Logging message at regular intervals')
}

main()
