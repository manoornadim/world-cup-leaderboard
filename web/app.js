async function loadLeaderboard() {
    try {
        const response = await fetch("/api/leaderboard");
        const data = await response.json();

        const table = document.getElementById("leaderboard");
        const updated = document.getElementById("lastUpdated");

        table.innerHTML = "";

        data.forEach((player, index) => {

            const row = document.createElement("tr");

            // Highlight top 3
            if (index === 0) row.classList.add("gold");
            if (index === 1) row.classList.add("silver");
            if (index === 2) row.classList.add("bronze");

            row.innerHTML = `
                <td>${index + 1}</td>
                <td>${player.name}</td>
                <td>${player.points}</td>
            `;

            table.appendChild(row);
        });

        const now = new Date();
        updated.innerText = "Last updated: " + now.toLocaleTimeString();

    } catch (error) {
        console.error("Error loading leaderboard:", error);
    }
}

// Initial load
loadLeaderboard();

// Auto refresh every 30 seconds
setInterval(loadLeaderboard, 30000);