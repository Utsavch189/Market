get = () => {

    fetch(`${window.location.origin}/distributor/getmanufacturers/`)
        .then(res => res.json())
        .then(data => document.getElementById("manufacturers").innerHTML = data.map((val, k) =>

            `
            <tr>
            <td>${val['userid']}</td>
            <td>${val['username']}</td>
            <td>${val['email']}</td>
            <td>${val['conatact']}</td>
            <td>${val['whatsapp']}</td>
          
            </tr>


`

        ))
        .catch(err => console.log(err))





}
get()