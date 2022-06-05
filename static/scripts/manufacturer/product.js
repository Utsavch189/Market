get = () => {

    fetch(`${window.location.origin}/manufacturer/seeproducts/`)
        .then(res => res.json())
        .then(data => document.getElementById("product").innerHTML = data.map((val, k) =>

            ` <div class="card my-4" style="width: 18rem;">
            <div class="card-body">
                <h5 class="card-title">${val['name']}</h5>
                <h6 class="card-subtitle mb-2 text-muted">${val['price']} Rs.</h6>
                <p class="card-text">${val['desc']}</p>
    
            </div>
        </div> 
                `
        ))
        .catch(err => console.log(err))





}
get()

dropdown = () => {

    fetch(`${window.location.origin}/manufacturer/seeproducts/`)
        .then(res => res.json())
        .then(data => document.getElementById('pro').innerHTML = data.map((val, k) =>

                `<option value=${val['name']}>${val['name']}</option>`


            )



        )


}
dropdown()