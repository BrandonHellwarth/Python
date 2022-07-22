var pokiform = document.querySelector('.pokiform');
pokiform.addEventListener('submit', function(e){
    e.preventDefault(); //prevents form submission from refreshing the page
    console.log(pokiform.children[1].value);//same as logging pokiname
    let pokiname = document.querySelector('#pokiname').value
    fetch(`https://pokeapi.co/api/v2/pokemon/${pokiname}`)
    .then(resp => resp.json())
    .then(data => {
        console.log(data);
        //do something with the data below
        var pokihead = document.querySelector('.pokihead');
        var pokimg = document.querySelector('.pokimg');
        pokihead.textContent = data.name;
        pokimg.innerHTML = `<img src="${data.sprites.front_default}" alt="">`;
    })
.catch(err => console.log(err));
})


