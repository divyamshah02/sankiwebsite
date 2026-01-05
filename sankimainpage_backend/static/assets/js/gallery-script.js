// Gallery functionality
function initGallery() {
  // Gallery modal functionality
  const galleryItems = document.querySelectorAll(".view-gallery")
  const modalImage = document.getElementById("galleryModalImage")
  const modalTitle = document.getElementById("galleryModalTitle")

  galleryItems.forEach((item) => {
    item.addEventListener("click", function (e) {
      e.preventDefault()
      const imageUrl = this.getAttribute("data-image")
      const imageTitle = this.getAttribute("data-title")
      modalImage.src = imageUrl
      modalTitle.textContent = imageTitle
    })
  })

  // Load more gallery items
  const loadMoreGallery = document.getElementById("load-more-gallery")

  if (loadMoreGallery) {
    loadMoreGallery.addEventListener("click", function () {
      // Simulate loading more gallery items
      const galleryGrid = document.getElementById("gallery-grid")

      // Clone existing gallery items for demo purposes
      const existingItems = document.querySelectorAll(".gallery-item")

      // Only add more if we have less than 16 visible items
      if (existingItems.length < 16) {
        for (let i = 0; i < 4 && i < existingItems.length; i++) {
          const clone = existingItems[i].cloneNode(true)
          galleryGrid.appendChild(clone)
        }

        // Reinitialize event listeners for new items
        initGalleryEventListeners()
      } else {
        this.textContent = "No More Photos"
        this.disabled = true
      }
    })
  }
}

// Initialize gallery event listeners
function initGalleryEventListeners() {
  const newGalleryItems = document.querySelectorAll(".view-gallery")
  const modalImage = document.getElementById("galleryModalImage")
  const modalTitle = document.getElementById("galleryModalTitle")

  newGalleryItems.forEach((item) => {
    item.addEventListener("click", function (e) {
      e.preventDefault()
      const imageUrl = this.getAttribute("data-image")
      const imageTitle = this.getAttribute("data-title")
      modalImage.src = imageUrl
      modalTitle.textContent = imageTitle
    })
  })
}

// Call gallery initialization when DOM is loaded
document.addEventListener("DOMContentLoaded", () => {
  // Initialize existing functions

  // Initialize gallery functionality
  initGallery()
})

