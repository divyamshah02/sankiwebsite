document.addEventListener("DOMContentLoaded", () => {
  // Quantity selector functionality
  const quantitySelectors = document.querySelectorAll(".quantity-selector")

  quantitySelectors.forEach((selector) => {
    const minusBtn = selector.querySelector(".minus")
    const plusBtn = selector.querySelector(".plus")
    const input = selector.querySelector("input")

    minusBtn.addEventListener("click", () => {
      const value = Number.parseInt(input.value)
      if (value > Number.parseInt(input.min)) {
        input.value = value - 1
      }
    })

    plusBtn.addEventListener("click", () => {
      const value = Number.parseInt(input.value)
      if (value < Number.parseInt(input.max)) {
        input.value = value + 1
      }
    })
  })

  // Event gallery modal functionality
  const galleryItems = document.querySelectorAll(".gallery-item a")
  const modalImage = document.getElementById("eventGalleryModalImage")

  galleryItems.forEach((item) => {
    item.addEventListener("click", function (e) {
      e.preventDefault()
      const imageUrl = this.getAttribute("data-image")
      modalImage.src = imageUrl
    })
  })

  // Smooth scroll for ticket section link
  const ticketLink = document.querySelector('a[href="#ticket-section"]')

  if (ticketLink) {
    ticketLink.addEventListener("click", (e) => {
      e.preventDefault()

      const targetSection = document.getElementById("ticket-section")

      window.scrollTo({
        top: targetSection.offsetTop - 100,
        behavior: "smooth",
      })
    })
  }

  // Related events hover effect
  const relatedEvents = document.querySelectorAll(".related-event-item")

  relatedEvents.forEach((event) => {
    event.addEventListener("click", () => {
      window.location.href = "event-detail.html"
    })
  })
})

