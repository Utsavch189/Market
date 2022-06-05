get = () => {

    fetch(`${window.location.origin}/manufacturer/seeproducts/`)
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


}
get()