get = () => {

    fetch(`${window.location.origin}/administrator/api/`)
        .then(res => res.json())
        .then(data => document.getElementById("dog").innerHTML = data.map((val, k) =>

            `<tr >
                    <td>${val['number']}</td>
                    <td>${val['name']}</td>
                    <td>${val['email']}</td>
                    <td>${val['contact']}</td>
                    <td>${val['whatsapp']}</td>
                    <td>${val['role']}</td>

                </tr>   
                `
        ))
        .catch(err => console.log(err))
}
get()

dropdown = () => {
    fetch(`${window.location.origin}/administrator/api/`)
        .then(res => res.json())
        .then(data => document.getElementById('role').innerHTML = data.map((val, k) =>
                `<option value=${val['number']}>${val['number']}</option>`

            )



        )

    fetch(`${window.location.origin}/administrator/api/`)
        .then(res => res.json())
        .then(data => document.getElementById('approved').innerHTML = data.map((val, k) =>
                `<option value=${val['number']}>${val['number']}</option>`

            )



        )
}
dropdown()