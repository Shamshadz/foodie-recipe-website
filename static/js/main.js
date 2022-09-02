function reload_javascript(){
  // # for populating home page with card

  for (let x = 0; x < 9; x++) {

    const options = {
      method: 'GET',
      headers: {
        'X-RapidAPI-Key': ' ',
        'X-RapidAPI-Host': 'random-recipes.p.rapidapi.com'
      }
    };
    
    fetch('https://random-recipes.p.rapidapi.com/ai-quotes/100', options)
      .then(response => response.json())
      .then((response) => {let resp = response[0];
              const div = document.createElement("div");
              div.className = 'card1';

              div.innerHTML = `<div class="card-header1">
                                <img src="${resp.image}" alt="rover" />
                              </div>
                              <div class="card-body1">
                                <h4>
                                    <a href="/article/" style="text-decoration: none; color: inherit; " >${resp.title}</a>
                                </h4>
                                <p>
                                    An exploration into the truck's polarising design
                                </p>
                                <div class="user1">
                                    <div class="user-info1">
                                        <strong>By</strong>
                                        <a href="">Rachel Lucas</a>
                                    </div>
                                </div>
                              </div>`;

              document.getElementById('card').appendChild(div);
      
      })
      .catch(err => console.error(err));
      console.log("hello")
  }
}