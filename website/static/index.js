function deletePlatform(platformId) {
  fetch("/delete-platform", {
    method: "POST",
    body: JSON.stringify({ platformId: platformId }),
  }).then((_res) => {
    window.location.href = "/platforms";
  });
}

function deleteGame(gameId) {
  fetch("/delete-game", {
    method: "POST",
    body: JSON.stringify({ gameId: gameId }),
  }).then((_res) => {
    window.location.href = "/gaming-backlog-manager";
  });
}

function toggleBacklogged(gameId) {
  fetch("/toggle-backlogged", {
    method: "POST",
    body: JSON.stringify({ gameId: gameId }),
  }).then((_res) => {
    window.location.href = "/gaming-backlog-manager";
  });
}

function toggleBacklogList(isListed) {
  fetch("/toggle-backlog-list", {
    method: "POST",
    body: JSON.stringify({ isListed: isListed }),
  }).then((_res) => {
    window.location.href = "/gaming-backlog-manager";
  });
}

function getRandomGame() {
  rows = document.getElementById("gamesTable").rows;
  randomIndex = Math.floor(Math.random() * rows.length);
  fetch("/get-random-game", {
    method: "POST",
    body: JSON.stringify({ randomIndex: randomIndex}),
  }).then((_res) => {
    window.location.href = "/gaming-backlog-manager";
  });
}