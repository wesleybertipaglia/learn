function main() {
  fetchData().then((data) => {
    console.log(data)
  })
}

function fetchData() {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve('Data fetched successfully')
    }, 2000)
  })
}

main()
