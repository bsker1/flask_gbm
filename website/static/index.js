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