function deletePlatform(platformId) {
  fetch("/delete-platform", {
    method: "POST",
    body: JSON.stringify({ platformId: platformId }),
  }).then((_res) => {
    window.location.href = "/add-platform";
  });
}

function deleteGame(gameId) {
  fetch("/delete-game", {
    method: "POST",
    body: JSON.stringify({ gameId: gameId }),
  }).then((_res) => {
    window.location.href = "/home";
  });
}