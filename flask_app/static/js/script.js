function liveSearch() {
    // Locate the card elements
    let cards = document.querySelectorAll('.card-body')
    let cardsHead = document.querySelectorAll('.card')
    // Locate the search input
    let search_query = document.getElementById("searchbox").value;
    // Loop through the cards
    // Check if the search box is empty
    if (search_query === "") {
      // Loop through the cards and remove the `.is-hidden` class
        for (var i = 0; i < cards.length; i++) {
            cards[i].classList.remove("is-hidden");
            cardsHead[i].classList.remove("is-hidden");
    }
}   else {
      // Loop through the cards
        for (var i = 0; i < cards.length; i++) {
          // If the text is within the card...
            if(cards[i].innerText.toLowerCase()
          // ...and the text matches the search query...
            .includes(search_query.toLowerCase())) {
              // ...remove the `.is-hidden` class.
                cards[i].classList.remove("is-hidden");
        } else {
              // Otherwise, add the class.
            cards[i].classList.add("is-hidden");
            cardsHead[i].classList.add("is-hidden");
        }
    }
}
}

function addHoverEffect() {
    // Locate the card elements
    let cards = document.querySelectorAll('.card')

    // Loop through the cards
    for (var i = 0; i < cards.length; i++) {
        // Add a hover event listener to the card
        cards[i].addEventListener("mouseover", function() {
            // When the user's mouse is over the card, add the `.hover` class
            // to the card, which will trigger the upward transition
            this.classList.add("hover");
        });

        // Add another event listener to remove the `.hover` class when the
        // user's mouse leaves the card
        cards[i].addEventListener("mouseout", function() {
            this.classList.remove("hover");
        });
    }
}

function hideDescription() {
    // Locate the description div
    let description = document.querySelector('.description')

    // Add a click event listener to the button
    document.querySelector('button').addEventListener('click', function() {
        // Check if the description div already has the `.is-hidden` class
        if (description.classList.contains('is-hidden')) {
            // If the description div has the `.is-hidden` class, remove it
            description.classList.remove('is-hidden')
        } else {
            // Otherwise, add the `.is-hidden` class to the description div
            description.classList.add('is-hidden')
        }
    });
}
