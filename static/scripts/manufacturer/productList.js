get = () => {

    fetch(`${window.location.origin}/administrator/seeproducts/`)
        .then(res => res.json())
        .then(data =>
            document.getElementById("production").innerHTML = data.map((val, k) =>

                `
                <tr>
                <td>${val['name']}</td>
                <td>${val['price']}</td>
                <td>${val['desc']}</td>
                </tr>
                `

            )
        )
        .catch(err => console.log(err))

}
get()