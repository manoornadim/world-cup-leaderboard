async function loadPredictions() {

    const response = await fetch("/api/todays-predictions");
    const data = await response.json();

    const container = document.getElementById("predictions-container");

    container.innerHTML = "";

    for (const player in data) {

        const section = document.createElement("div");

        section.innerHTML = `<h2>${player}</h2>`;

        const table = document.createElement("table");

        table.innerHTML = `
            <tr>
                <th>Match</th>
                <th>Prediction</th>
            </tr>
        `;

        data[player].forEach(match => {

            const row = document.createElement("tr");

            row.innerHTML = `
                <td>${match["Home Team"]} v ${match["Away Team"]}</td>
                <td>${match["Pred Home"]} - ${match["Pred Away"]}</td>
            `;

            table.appendChild(row);
        });

        section.appendChild(table);
        container.appendChild(section);
    }
}

loadPredictions();