const siteUrl = "//127.0.0.1:8000/";
const minWidth = 150;
const minHeight = 150;

function downloaderLaunch() {
  images = document.querySelectorAll('img[src$=".jpg"], img[src$=".jpeg"], img[src$=".png"]');
  images.forEach((image) => {
    if (image.naturalWidth >= minWidth && image.naturalHeight >= minHeight) {
      const imageFound = document.createElement("img");
      imageFound.src = image.src;
      imagesFound.append(imageFound);
    }
  });

  imagesFound.querySelectorAll("img").forEach((image) => {
    image.addEventListener("click", (event) => {
      imageSelected = event.target;
      bookmarklet.style.display = "none";
      window.open(`${siteUrl}images/create/?url=${encodeURIComponent(imageSelected.src)}&title=${encodeURIComponent(document.title)}`, "_blank");
    });
  });
}

bookmarkletLaunch();
