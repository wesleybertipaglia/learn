let breeds = []

async function main() {
  const breedsUrl = 'https://dog.ceo/api/breed/hound/list'
  breeds = await fetchMessage(breedsUrl)
}

async function fetchMessage(url) {
  const response = await fetch(url)
  const { message } = await response.json()
  return message
}

await main()
