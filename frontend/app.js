async function analyzeText() {
    const text = document.getElementById("textInput").value;

    const res = await fetch("http://localhost:8000/analyze-text?input_text=" + text, {
        method: "POST"
    });

    const data = await res.json();
    document.getElementById("result").innerText = JSON.stringify(data, null, 2);
}

async function analyzeAudio() {
    const file = document.getElementById("audioFile").files[0];
    const formData = new FormData();
    formData.append("file", file);

    const res = await fetch("http://localhost:8000/analyze-audio", {
        method: "POST",
        body: formData
    });

    const data = await res.json();
    document.getElementById("result").innerText = JSON.stringify(data, null, 2);
}
