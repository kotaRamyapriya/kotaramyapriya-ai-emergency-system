console.log("Frontend JS loaded!");

// Analyze Text
document.getElementById("textBtn").addEventListener("click", async () => {
    const text = document.getElementById("textInput").value;

    if (!text.trim()) {
        alert("Please enter emergency text!");
        return;
    }

    const res = await fetch("http://20.205.25.216:8000/analyze-text", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text })
    });

    const data = await res.json();
    document.getElementById("result").textContent = JSON.stringify(data, null, 2);
});

// Analyze Audio
document.getElementById("audioBtn").addEventListener("click", async () => {
    const audioFile = document.getElementById("audioFile").files[0];

    if (!audioFile) {
        alert("Please upload an audio file!");
        return;
    }

    const formData = new FormData();
    formData.append("file", audioFile);

    const res = await fetch("http://20.205.25.216:8000/analyze-audio", {
        method: "POST",
        body: formData
    });

    const data = await res.json();
    document.getElementById("result").textContent = JSON.stringify(data, null, 2);
});

