function deletePlatform(platformId) {
  fetch("/delete-platform", {
    method: "POST",
    body: JSON.stringify({ platformId: platformId }),
  }).then((_res) => {
    window.location.href = "/add-platform";
  });
}