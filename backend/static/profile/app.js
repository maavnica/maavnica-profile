(function () {
  "use strict";

  document.querySelectorAll(".js-track").forEach(function (el) {
    el.addEventListener("click", function () {
      el.dataset.clickedAt = String(Date.now());
    });
  });

  var shareBtn = document.querySelector(".js-share");
  if (!shareBtn) return;

  var hint = shareBtn.querySelector(".js-share-hint");
  var status = document.getElementById("share-status");
  var defaultHint = shareBtn.getAttribute("data-share-default") || "ce profil";
  var copiedMsg = shareBtn.getAttribute("data-share-copied") || "Lien copié";
  var sharedMsg = shareBtn.getAttribute("data-share-shared") || "Profil partagé";
  var resetTimer;

  function feedback(message) {
    if (hint) hint.textContent = message;
    shareBtn.classList.add("is-copied");
    if (status) status.textContent = message;
    clearTimeout(resetTimer);
    resetTimer = setTimeout(function () {
      shareBtn.classList.remove("is-copied");
      if (hint) hint.textContent = defaultHint;
      if (status) status.textContent = "";
    }, 2200);
  }

  function copyUrl() {
    var url = window.location.href;
    if (navigator.clipboard && navigator.clipboard.writeText) {
      return navigator.clipboard.writeText(url).then(function () {
        feedback(copiedMsg);
        shareBtn.dataset.clickedAt = String(Date.now());
      });
    }
    return Promise.reject();
  }

  shareBtn.addEventListener("click", function () {
    var url = window.location.href;
    var title = document.title;

    if (navigator.share) {
      navigator
        .share({ title: title, url: url })
        .then(function () {
          feedback(sharedMsg);
          shareBtn.dataset.clickedAt = String(Date.now());
        })
        .catch(function (err) {
          if (err && err.name === "AbortError") return;
          copyUrl().catch(function () {
            feedback("Copiez l’URL");
          });
        });
      return;
    }

    copyUrl().catch(function () {
      feedback("Copiez l’URL dans la barre d’adresse");
    });
  });
})();
