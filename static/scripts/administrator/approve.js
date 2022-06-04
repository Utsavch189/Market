get = () => {

    fetch(`${window.location.origin}/administrator/approve/`)
        .then(res => res.json())
        .then(data => document.getElementById("dog").innerHTML = data.map((val, k) =>

            `<tr >
                    <td>${val['userid']}</td>
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
    fetch(`${window.location.origin}/administrator/approve/`)
        .then(res => res.json())
        .then(data => document.getElementById('role').innerHTML = data.map((val, k) =>
                `<option value=${val['userid']}>${val['userid']}</option>`

            )



        )


}
dropdown()