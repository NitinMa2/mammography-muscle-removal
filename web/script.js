// function to test a random api call
async function fetchData() {
    let response = await fetch('https://catfact.ninja/fact')
    let data = await response.json()

    return data;
}

// handles the upload button click event
const handleUpload = () => {
    const elem = document.getElementById("fact");
    fetchData().then(data => elem.innerHTML = data.fact)
}