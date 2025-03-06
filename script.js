function analyzeNumber() {
  const input = document.getElementById("numberInput").value;
  if (!input || isNaN(input)) {
    alert("Please enter a valid number!");
    return;
  }

  const number = parseFloat(input);
  fetch("/analyze", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ number }),
  })
    .then((response) => response.json())
    .then((data) => {
      document.getElementById("result").innerHTML = `
        <p><strong>Number:</strong> ${data.number}</p>
        <p><strong>Even/Odd:</strong> ${data.even_odd}</p>
        <p><strong>Prime:</strong> ${data.prime}</p>
        <p><strong>Armstrong:</strong> ${data.armstrong}</p>
        <p><strong>Integer:</strong> ${data.integer}</p>
        <p><strong>Rational/Irrational:</strong> ${data.rational_irrational}</p>
        <p><strong>Square:</strong> ${data.square}</p>
        <p><strong>Cube:</strong> ${data.cube}</p>
        <p><strong>Roman Form:</strong> ${data.roman}</p>
        <p><strong>In Words:</strong> ${data.words}</p>
        <p><strong>Binary Form:</strong> ${data.binary}</p>
        <p><strong>Exponents:</strong> ${data.exponents}</p>
        <p><strong>Divisible By:</strong> ${data.divisible_by}</p>
        <p><strong>Table:</strong> ${data.table}</p>
      `;
    })
    .catch((error) => console.error("Error:", error));
}
