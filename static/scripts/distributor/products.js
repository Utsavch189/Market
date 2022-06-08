get = () => {

    fetch(`${window.location.origin}/distributor/getproducts/`)
        .then(res => res.json())
        .then(data => document.getElementById("products").innerHTML = data.map((val, k) =>

            `
            <tr>
            <td>${val['p_id']}</td>
            <td>${val['p_name']}</td>
            <td>${val['p_price']}</td>
            <td>${val['p_desc']}</td>
            <td>${val['p_in_stock']}</td>
            <td>${val['distributor']}</td>
            </tr>


`

        ))
        .catch(err => console.log(err))





}
get()