get = () => {

    fetch(`${window.location.origin}/manufacturer/distribute/`)
        .then(res => res.json())
        .then(data => document.getElementById("distribution").innerHTML = data.map((val, k) =>

            `<tr >
                    <td>${val['userid']}</td>
                    <td>${val['name']}</td>
                    <td>${val['contact']}</td>
                    <td>${val['whatsapp']}</td>
                    <td>${val['email']}</td>

                </tr>   
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

    fetch(`${window.location.origin}/manufacturer/distribute/`)
        .then(res => res.json())
        .then(data => document.getElementById('users').innerHTML = data.map((val, k) =>
                `<option value=${val['userid']}>${val['userid']}</option>`

            )



        )
}
dropdown()