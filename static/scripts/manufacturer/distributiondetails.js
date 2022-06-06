distdetails = () => {
    fetch(`${window.location.origin}/manufacturer/distributiondetails/`)
        .then(res => res.json())
        .then(data => document.getElementById("distributiondetails").innerHTML = data.map((val, k) =>

            `<tr >
                <td>${val['id']}</td>
                <td>${val['product_id']}</td>
                <td>${val['product_name']}</td>
                <td>${val['product_quantity']}</td>
                <td>${val['total_price']}</td>

            </tr>   
            `
        ))
        .catch(err => console.log(err))


}
distdetails()

//function deletes() {
//console.log('hi')

//}

//window.addEventListener('click', deletes())